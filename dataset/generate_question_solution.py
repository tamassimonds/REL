import random
import json
from datasets import load_dataset
from functools import lru_cache

@lru_cache(maxsize=1)
def load_cached_competition_dataset():
    """
    Load and cache the competition math dataset from Hugging Face.
    Uses lru_cache to prevent reloading the dataset on subsequent calls.
    
    Returns:
        Dataset: The competition math dataset from hendrycks/competition_math
    """
    return load_dataset("hendrycks/competition_math", split="train", trust_remote_code=True)

def generate_competition_math_questions(n_questions):
    """
    Generate n_questions from the competition math dataset and format them for fine-tuning.
    Returns a list of dictionaries in the format required for fine-tuning.
    """
    # Load the competition math dataset
    dataset = load_cached_competition_dataset()
    
    # Randomly sample n questions
    selected_indices = random.sample(range(len(dataset)), min(n_questions, len(dataset)))
    formatted_data = []
    
    for idx in selected_indices:
        question = dataset[idx]
        
        # Format the data as required for fine-tuning
        formatted_example = {
            "messages": [
                {"role": "user", "content": question['problem']},
                {"role": "assistant", "content": question['solution']}
            ]
        }
        formatted_data.append(formatted_example)
    
    # Save to JSONL file
    output_file = "competition_math_questions.jsonl"
    with open(output_file, 'w') as f:
        for item in formatted_data:
            f.write(json.dumps(item) + '\n')
    
    return formatted_data

# Example usage
if __name__ == "__main__":
    # Generate 100 competition math questions
    questions = generate_competition_math_questions(1000)
    print(f"Generated {len(questions)} competition math questions")
