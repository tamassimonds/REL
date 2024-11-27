import random
from datasets import load_dataset
from functools import lru_cache
import json

@lru_cache(maxsize=1)
def load_cached_dataset():
    return load_dataset("lighteval/MATH", split="train")

@lru_cache(maxsize=1)
def load_cached_competition_dataset():
    return load_dataset("hendrycks/competition_math", split="train", trust_remote_code=True)



def get_random_math_question():
    # Load the MATH dataset from LightEval (cached)
    dataset = load_cached_dataset()
    

    
    # Get a random index
    random_index = random.randint(0, len(dataset) - 1)
    
    # Get the random question
    random_question = dataset[random_index]
    
    # Extract the problem and solution from the question
    problem = random_question['problem']
    solution = random_question['solution']
    
    return problem, solution

def get_hard_math_question():
    # Load the MATH dataset from LightEval (cached)
    dataset = load_cached_dataset()
    
    # Filter the dataset for Level 5 questions
    hard_questions = [q for q in dataset if q["level"] == "Level 5"]
    
    if not hard_questions:
        raise ValueError("No Level 5 questions found in the dataset")
    
    # Get a random hard question
    random_question = random.choice(hard_questions)
    
    # Extract the problem and solution from the question
    problem = random_question['problem']
    solution = random_question['solution']
    
    return problem, solution


def get_medium_math_question():
    # Load the MATH dataset from LightEval (cached)
    dataset = load_cached_dataset()
    
    # Filter the dataset for Level 5 questions
    hard_questions = [q for q in dataset if q["level"] in ["Level 3", "Level 4", "Level 5"]]
    
    if not hard_questions:
        raise ValueError("No Level 5 questions found in the dataset")
    
    # Get a random hard question
    random_question = random.choice(hard_questions)
    
    # Extract the problem and solution from the question
    problem = random_question['problem']
    solution = random_question['solution']
    
    return problem, solution

def get_competition_math_problem():
    # Load the competition math dataset (cached)
    dataset = load_cached_competition_dataset()
    
    # Get a random index
    random_index = random.randint(0, len(dataset) - 1)
    
    # Get the random question
    random_question = dataset[random_index]
    
    # Extract the problem and solution from the question
    problem = random_question['problem']
    solution = random_question['solution']
    
    return problem, solution

def get_hard_competition_math_problem():
    # Load the competition math dataset (cached)
    dataset = load_cached_competition_dataset()
    
    # Filter the dataset for Level 5 questions
    hard_questions = [q for q in dataset if q["level"] == "Level 5"]
    
    if not hard_questions:
        raise ValueError("No Level 5 questions found in the dataset")
    
    # Get a random hard question
    random_question = random.choice(hard_questions)
    
    # Extract the problem and solution from the question
    problem = random_question['problem']
    solution = random_question['solution']
    
    return problem, solution

def get_gpqa_question():
    # Load the GPQA questions from JSON file
    with open('lib/unique_gpqa_questions.json', 'r') as f:
        questions = json.load(f)
    
    # Get a random question
    random_question = random.choice(questions)
    
    # Extract the problem and solution from the question
    problem = random_question['question']
    solution = random_question['correct_answer']
    explanation = random_question['explanation']
    returned_solution = f"{solution}\n\n{explanation}"
    return problem, returned_solution


def get_custom_question():
    # Load the custom questions from JSON file
    try:
        with open('lib/custom_questions.json', 'r') as f:
            data = json.load(f)
            questions = data['questions']
            problem = random.choice(questions)
            solution = "No solution provided. Please verify your answer independently."
        
        return problem, solution
    except FileNotFoundError:
        raise FileNotFoundError("custom_questions.json not found in lib directory")
    except KeyError:
        raise KeyError("custom_questions.json must contain a 'questions' array")
    except json.JSONDecodeError:
        raise ValueError("custom_questions.json is not valid JSON")

# Example usage
if __name__ == "__main__":
    random_problem, random_solution = get_random_math_question()
    print("Random MATH question:")
    print("Problem:", random_problem)
    print("\nSolution:", random_solution)

    print("\nHard MATH question:")
    hard_problem, hard_solution = get_hard_math_question()
    print("Problem:", hard_problem)
    print("\nSolution:", hard_solution)

    print("\nCompetition MATH question:")
    comp_problem, comp_solution = get_competition_math_problem()
    print("Problem:", comp_problem)
    print("\nSolution:", comp_solution)

    print("\nHard Competition MATH question:")
    hard_comp_problem, hard_comp_solution = get_hard_competition_math_problem()
    print("Problem:", hard_comp_problem)
    print("\nSolution:", hard_comp_solution)




    print("\nCustom question:")
    custom_problem, custom_solution = get_custom_question()
    print("Problem:", custom_problem)
    print("\nSolution:", custom_solution)
