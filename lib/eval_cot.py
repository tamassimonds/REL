from lib.inference import generate_text
import re



# Updated evaluation prompt
# EVAL_PROMPT = """
# You are an expert Marker, evaluating at the level of a university professor. Your job is to evaluate the model's solution based on the question and the correct solution provided.

# Question:
# {question}

# Model's solution:
# {model_solution}

# Correct solution:
# {correct_solution}

# Evaluate the model's solution:
# 1. Is the solution correct overall?
# 2. If there's an error, at which step does it first occur? (Provide the step number)
# 3. What is the nature of the error?


# If the answer is correct but not simplified mark it as correct

# Don't point out error that the model corrects later in the solution. Just focus on errors in the final solution.
# If a model correct a solution later on don't point it out.

# In the error description, be very specific about the error and explain how to fix it. 
# Don't tell the model the correct final answer though just how to fix the error.

# It's still correct if the model's solution is correct but uses a different method than the provided sample solution.

# Then Provide your evaluation in the following format:
# CORRECT: [Yes/No]
# ERROR_STEP: [Step number where the error first occurs, or N/A if correct]
# ERROR_DESCRIPTION: [Long Description of the error, or N/A if correct]
# """

EVAL_PROMPT = """
You are an expert Marker, evaluating at the level of a university professor. Your job is to evaluate the model's solution based on the question and the correct solution provided.

Question:
{question}

Model's solution:
{model_solution}

Correct solution:
{correct_solution}

I want you to return if the model's solution is correct or not.
Just check the final answer not the working out.
If it is formatted differently or not fully simplified still mark it as correct.

If the model doesn't clearly state the final answer, don't mark it as correct.

CORRECT: [Yes/No]
ERROR_DESCRIPTION: [Long Description of the error, or N/A if correct]
"""

async def evaluate_solution(model, question, model_solution, correct_solution):
    eval_prompt = EVAL_PROMPT.format(
        question=question,
        model_solution=model_solution,
        correct_solution=correct_solution
    )
    evaluation = await generate_text(model, eval_prompt)
    

    # print(evaluation)
    # Extract evaluation results
    correct_match = re.search(r'CORRECT:\s*(Yes|No)', evaluation)
    error_step_match = re.search(r'ERROR_STEP:\s*(\d+|N/A)', evaluation)
    error_description_match = re.search(r'ERROR_DESCRIPTION:\s*(.+)', evaluation, re.DOTALL)
    
    is_correct = correct_match.group(1) == 'Yes' if correct_match else False
    error_step = int(error_step_match.group(1)) if error_step_match and error_step_match.group(1) != 'N/A' else None
    error_description = error_description_match.group(1).strip() if error_description_match else None
    
    return is_correct, error_step, error_description, evaluation

# This function replaces the previous score_solution_steps function
async def evaluate_cot_solution(model, question, model_solution, correct_solution):
    is_correct, error_step, error_description, raw_text = await evaluate_solution(model, question, model_solution, correct_solution)
    return is_correct, error_step, error_description, raw_text
