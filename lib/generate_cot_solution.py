from lib.inference import generate_text
from lib.eval_cot import evaluate_cot_solution
from lib.solution_logger import SolutionLogger
from dataclasses import dataclass
from typing import Tuple, Optional

# COT_PROMPT = """
# Let's approach this problem step by step. For each step, provide your thoughts and calculations on a new line.

# Question: {{question}}

# Solve the following problem step-by-step. 
# Respond to the following user query in a comprehensive and detailed way. Think step by step.
# Write down your thought process before responding for each step. 

# Start off by really understanding the question. 

# Before solving the problem list out a few different possible ways you could solve the problem then pick the best way.

# After each step reflect on the step and the result and check if it is correct.
# Insert lots of thinking words like hmm, wait, but, however, etc.
# If you are confused at any point try and take a step back and think about the problem.
# To get full marks you must show your thought process aswell.
# Reflect often if it's correct, check often if your approach is corret and if not change your approach. After every few steps naturally check like a human would if the answer is correct before continueing 

# Remember to separate each step and sub-step with a new line for clarity.

# Once you solve it verify it by trying another method
# """

COT_PROMPT = """
Let's approach this problem step by step. For each step, provide your thoughts and calculations on a new line.

Question: {{question}}

Solve the following problem step-by-step. 
Respond to the following user query in a comprehensive and detailed way. Think step by step.
Write down your thought process before responding for each step. 

Start off by really understanding the question. 
To get full marks you must show your thought process aswell. First show you exploring a range of different stratergies. If one doesn't work show it and then use another method. Brainstorm at first how to solve it. I want you to write it like a human as in start off by brainstorming. Reflect often if it's correct, check often if your approach is corret and if not change your approach. After every few steps naturally check like a human would if the answer is correct before continueing


First thoughts are important - write down what initially comes to mind, even if it seems messy or incomplete. Like when you first see a problem and think 'This looks similar to something I've done before...' or 'I have no idea where to start...'

Let your thinking flow naturally:

- If you suddenly realize something isn't working: "Wait, that can't be right because..."
- When you get stuck: "Hmm, maybe I need to back up and try..."
- When something clicks: "Oh! This reminds me of..."

Check your work like you naturally would:

- Sometimes quick checks: "That number seems too big..."
- Sometimes deeper reflection: "Let me think about whether this approach makes sense..."
- Random insights: "Actually, there might be an easier way..."

Don't be afraid to:

- Show your mistakes and dead ends
- Change direction when something feels off
- Think out loud about your confusion or uncertainty
- Have "aha moments" in the middle of working

The key is writing it out like you're really thinking through it - messy parts, realizations, doubts and all. Not every problem needs every type of thinking - let it flow based on what the specific problem brings up for you."

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
        return f"""<SYSTEM>We provided your previous answer into a Marker and you received this feedback:

Your answer:
The user request was: <USER> {question} </USER>

Your response was: {working_out}

Marker feedback: INCORRECT: {error_description}


write it out like a contiuation from your previous incorrect solution like you are a human. 
Don't repeat the working out you wrote in your previous incorrect solution just continue on from it.
Show your process of discovering the last solution is wrong and show your working out in leading to new correct solution
Then insert a CoT phrase like "Ahh, I appear to have made an error" and describe the error WHERE THE error occured.
Make sure to write out solution before the error identically and only change where the error occured
Include the error and the part of you correcting it
If you approach is incorrect all together include the incorrect approach and the point towards the end where you corrected it
Based off the error maybe consider trying a different path way 
Show the process of you discovering the error and correcting it. 
Then continue generating a new solution.
Once you solve it verify it by trying another method


</SYSTEM><ASSISTANT>"""

    @staticmethod
    def create_final_prompt(question: str, working_out: str, solution: str) -> str:
        return f"""<SYSTEM>We provided your previous answer into a Marker and you received this feedback:

Your answer:
The user request was: <USER> {question} </USER>

Your response was: {working_out}

The marker said your answer was incorrect.

I want you to rewrite your working our keeping the orginal ideas but correcting the errors in your thought process.

You might say things like:
- "Wait a minute, I think I see where I went wrong..."
- "Actually, looking at this again..."
- "Hmm, let me double-check my reasoning here..."

Rewrite your working out from the start again. 
Don't acknowledge that you are given a sample solution. Just naturally intergrate it into your previous working out

Remember to:
- Keep your original good insights
- Show your thought process as you realize what needs adjustment
- Demonstrate how you arrive at better understanding
- Validate your new approach by trying different methods

Remember
First thoughts are important - write down what initially comes to mind, even if it seems messy or incomplete. Like when you first see a problem and think 'This looks similar to something I've done before...' or 'I have no idea where to start...'

Let your thinking flow naturally:

- If you suddenly realize something isn't working: "Wait, that can't be right because..."
- When you get stuck: "Hmm, maybe I need to back up and try..."
- When something clicks: "Oh! This reminds me of..."

Check your work like you naturally would:

- Sometimes quick checks: "That number seems too big..."
- Sometimes deeper reflection: "Let me think about whether this approach makes sense..."
- Random insights: "Actually, there might be an easier way..."

Don't be afraid to:

- Show your mistakes and dead ends
- Change direction when something feels off
- Think out loud about your confusion or uncertainty
- Have "aha moments" in the middle of working

Here's a sample solution: <SAMPLE_SOLUTION> {solution} </SAMPLE_SOLUTION>

STATE YOUR ANSWER CLEARLY AT THE END in format <ANSWER> solution</ANSWER>

</SYSTEM><ASSISTANT>"""

    @staticmethod
    def create_review_prompt(working_out: str) -> str:
        return f"""Based on this working out:
        {working_out}
        
        Please put it together into a coherent and complete solution. Don't change the final answer."""
async def generate_cot_solution(model: str, formatted_prompt: str, temperature: float = 1.0) -> Tuple[str, str]:
    working_out = await generate_text(model, formatted_prompt, temperature=temperature)
    review_prompt = PromptManager.create_review_prompt(working_out)
    final_solution = await generate_text(model, review_prompt, temperature=temperature)
    return final_solution, working_out
async def generate_cot_solution_simple(model: str, formatted_prompt: str, temperature: float = 1.0) -> str:
    working_out = await generate_text(model, formatted_prompt, temperature=temperature)
    return working_out

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
    

    formatted_prompt = COT_PROMPT.replace("{{question}}", question)
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
        
        # Use improvement_prompt for all iterations except the last one
        if iteration < max_iterations - 2:
            update_prompt = PromptManager.create_improvement_prompt(
                question, full_working_out, result.error_description)
        else:
            update_prompt = PromptManager.create_final_prompt(
                question, full_working_out, solution)

        # Generate new solution and append to full working out
        new_working_out = await generate_cot_solution_simple(
            model, update_prompt, temperature)
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