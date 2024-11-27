import asyncio
import json
import os
from pathlib import Path
from lib.inference import generate_text
from lib.get_dataset_question import get_gpqa_question as get_question, get_random_math_question, get_hard_math_question, get_medium_math_question, get_competition_math_problem, get_hard_competition_math_problem, get_test_math_question, get_custom_question
from lib.eval_response import evaluate_text
from lib.generate_cot_solution import generate_iterative_solution as generate_iterative_COT_solution
from lib.generate_solution import generate_iterative_solution as generate_iterative_solution
from datetime import datetime
import uuid

CONCURRENT_TASKS = 100
NUM_SAMPLES = 1000

# Chain of Thought prompt template
COT_PROMPT = """
{problem}
"""

# GENERATOR_MODEL = "ft:gpt-4o-2024-08-06:inspire-robotics:cot-dataset-5:ATM7SY2i"
GENERATOR_MODEL = "ft:gpt-4o-2024-08-06:inspire-robotics:rel-humantrainingbase-synthetic-100:AVck0nLv"


# GENERATOR_MODEL = "gpt-4o-mini"
# EVAL_MODEL = "gpt-4o-mini"
EVAL_MODEL = "gpt-4o"

if GENERATOR_MODEL == "gpt-4o" or GENERATOR_MODEL == "gpt-4o-mini":
    generation_func = generate_iterative_solution
else:
    generation_func = generate_iterative_COT_solution

# Add this enum-like class at the top
class DatasetType:
    GPQA = "gpqa"
    MATH_RANDOM = "math_random"
    MATH_HARD = "math_hard"
    MATH_MEDIUM = "math_medium"
    COMPETITION_MATH = "competition_math"
    COMPETITION_MATH_HARD = "competition_math_hard"
    MATH_TEST = "math_test"
    CUSTOM = "custom"
DATASET = DatasetType.CUSTOM

# Add this mapping
DATASET_FUNCTIONS = {
    DatasetType.GPQA: get_question,
    DatasetType.MATH_RANDOM: get_random_math_question,
    DatasetType.MATH_HARD: get_hard_math_question,
    DatasetType.MATH_MEDIUM: get_medium_math_question,
    DatasetType.COMPETITION_MATH: get_competition_math_problem,
    DatasetType.COMPETITION_MATH_HARD: get_hard_competition_math_problem,
    DatasetType.MATH_TEST: get_test_math_question,
    DatasetType.CUSTOM: get_custom_question,
}

async def generate_single_sample(
    inference_model: str,
    eval_model: str,
    output_dir: str,
    sample_index: int,
    dataset_type: str,
    validate_solutions: bool = False
) -> bool:
    try:
        get_question_func = DATASET_FUNCTIONS.get(dataset_type)
        if not get_question_func:
            raise ValueError(f"Invalid dataset type: {dataset_type}")
            
        problem, ground_truth = get_question_func()
        prompt = COT_PROMPT.format(problem=problem)
        
        model_solution = await generation_func(
            model=inference_model,
            question=prompt,
            solution=ground_truth
        )
        
        # Handle case where model_solution is a dictionary
        if isinstance(model_solution, dict):
            model_solution = model_solution.get('final_solution', '')
        
        if not model_solution or model_solution.strip() == "":
            print(f"Sample {sample_index}: Generated solution was empty, skipping...")
            return False
        
        if validate_solutions:
            is_correct, is_bad_response = await evaluate_text(
                eval_model=eval_model,
                modelAnswer=model_solution,
                groundTruthAnswer=ground_truth
            )
            if not (is_correct and not is_bad_response):
                print(f"Sample {sample_index}: Generated solution was incorrect or invalid, trying again...")
                return False
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        output_file = os.path.join(output_dir, f"synthetic_{timestamp}_{unique_id}_{sample_index}.json")
        data = {
            "problem": problem,
            "solution": model_solution,
            "ground_truth": ground_truth
        }
        
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Successfully generated sample {sample_index}")
        return True
        
    except Exception as e:
        print(f"Error generating sample {sample_index}: {e}")
        return False

async def generate_synthetic_data(
    inference_model: str,
    eval_model: str,
    num_samples: int,
    dataset_type: str,
    output_dir: str = "dataset/synthetic",
    concurrent_tasks: int = CONCURRENT_TASKS,
    validate_solutions: bool = True
):
    # Create dataset-specific subfolder
    output_dir = os.path.join(output_dir, dataset_type)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    semaphore = asyncio.Semaphore(concurrent_tasks)
    tasks = set()
    successful_generations = 0
    current_index = 0

    async def wrapped_generate_sample(index):
        async with semaphore:
            return await generate_single_sample(
                inference_model,
                eval_model,
                output_dir,
                index,
                dataset_type,
                validate_solutions
            )

    while successful_generations < num_samples:
        # Start new tasks if we're under the limit
        while len(tasks) < concurrent_tasks and current_index < num_samples:
            task = asyncio.create_task(wrapped_generate_sample(current_index))
            tasks.add(task)
            current_index += 1

        # Wait for at least one task to complete
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        
        # Process completed tasks
        for task in done:
            tasks.remove(task)
            if await task:
                successful_generations += 1
                print(f"Progress: {successful_generations}/{num_samples}")

        # If we failed to generate some samples, create new tasks to replace them
        if successful_generations + len(tasks) < num_samples:
            continue

if __name__ == "__main__":
    # Example usage
    asyncio.run(generate_synthetic_data(
        inference_model=GENERATOR_MODEL,
        eval_model=EVAL_MODEL,
        num_samples=NUM_SAMPLES,
        dataset_type=DATASET  # or any other dataset type
    ))