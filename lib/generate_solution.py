from lib.inference import generate_text
from lib.eval_cot import evaluate_cot_solution
from lib.solution_logger import SolutionLogger
from dataclasses import dataclass
from typing import Tuple, Optional

PROMPT = """
Question: {{question}}

Your previous working out:
{{working_out}}

The correct solution is:
{{solution}}

Please explain how to arrive at this solution in a clear, step-by-step manner.
Make sure to show your calculations and reasoning at each step.

STATE YOUR ANSWER CLEARLY AT THE END in format <ANSWER> solution</ANSWER>
"""

@dataclass
class IterationResult:
    is_correct: bool
    error_step: Optional[str]
    error_description: Optional[str]
    raw_eval: str

class PromptManager:
    @staticmethod
    def create_improvement_prompt(question: str, working_out: str, error_description: str) -> str:
        return f"""Your previous answer was incorrect.

Question: {question}

Your working out:
{working_out}

Error: {error_description}

Please provide a corrected solution, showing your work step-by-step.
STATE YOUR ANSWER CLEARLY AT THE END in format <ANSWER> solution</ANSWER>
"""

    @staticmethod
    def create_final_prompt(question: str, working_out: str, solution: str) -> str:
        return f"""Question: {question}

Your previous working:
{working_out}

The correct solution is:
{solution}

Please provide a clear explanation of how to reach this solution, step by step.
STATE YOUR ANSWER CLEARLY AT THE END in format <ANSWER> solution</ANSWER>
"""

    @staticmethod
    def create_review_prompt(working_out: str) -> str:
        return f"""Please review and summarize this solution clearly and concisely:
{working_out}

Keep the same final answer but make the explanation more coherent."""

async def generate_cot_solution(model: str, formatted_prompt: str, temperature: float = 1.0) -> Tuple[str, str]:
    working_out = await generate_text(model, formatted_prompt, temperature=temperature)
    working_out = working_out['text'] if isinstance(working_out, dict) else working_out
    
    review_prompt = PromptManager.create_review_prompt(working_out)
    final_solution = await generate_text(model, review_prompt, temperature=temperature)
    final_solution = final_solution['text'] if isinstance(final_solution, dict) else final_solution
    return final_solution, working_out

async def generate_cot_solution_simple(model: str, formatted_prompt: str, temperature: float = 1.0) -> str:
    working_out = await generate_text(model, formatted_prompt, temperature=temperature)
    return working_out['text'] if isinstance(working_out, dict) else working_out

async def evaluate_iteration(marker_model: str, question: str, response: str, solution: str) -> IterationResult:
    is_correct, error_step, error_description, raw_eval = await evaluate_cot_solution(
        marker_model, question, response, solution
    )
    return IterationResult(is_correct, error_step, error_description, raw_eval)

async def generate_iterative_solution(
    model: str,
    question: str,
    solution: str,
    max_iterations: int = 3,
    marker_model: str = "gpt-4o",
    generate_final: bool = True
) -> dict:
    logger = SolutionLogger(question, solution, max_iterations, marker_model, model)
    

    formatted_prompt = PROMPT.replace("{{question}}", question)
    # Initial attempt
    temperature = 1.0
    working_out = await generate_cot_solution_simple(model, formatted_prompt, temperature)
    logger.log_initial_attempt(working_out, working_out, temperature)
    
    # Keep track of all working out
    full_working_out = working_out
    
    # Iteration loop
    for iteration in range(max_iterations):
        result = await evaluate_iteration(marker_model, question, full_working_out, solution)
        logger.log_evaluation(iteration + 1, result.is_correct, result.error_step, 
                            result.error_description, result.raw_eval)
        
        if result.is_correct:
            break
            
        # If we've reached the last iteration and it's still not correct, return empty strings
        if iteration == max_iterations - 1:
            return logger.log_final_results(
                "",             # working out
                "",            # final solution
                False,         # is correct
                iteration + 1, # iterations
                result.error_description  # error description
            )
            
        temperature *= 0.9
        update_prompt = PromptManager.create_final_prompt(
                question, full_working_out, solution)

        # Generate new solution and append to full working out
        new_working_out = await generate_cot_solution_simple(
            model, update_prompt, temperature)
        # full_working_out = f"{full_working_out}\n\n{new_working_out}"
        full_working_out = new_working_out

        logger.log_iteration(iteration + 1, update_prompt, new_working_out, 
                           full_working_out)
    
    # After the iteration loop, add final review step only if generate_final is True
    final_solution = None
    if generate_final:
        review_prompt = PromptManager.create_review_prompt(full_working_out)
        final_solution = await generate_text(model, review_prompt, temperature=temperature)
    else:
        final_solution = ""
    
    return logger.log_final_results(
        full_working_out,    # working out
        final_solution,      # final solution (either reviewed or raw working out)
        result.is_correct,   # is correct
        iteration + 1,       # iterations
        result.error_description  # error description
    )