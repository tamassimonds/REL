from datasets import load_dataset
import json

def get_unique_gpqa_questions():
    # Load both datasets
    gpqa_diamond = load_dataset("Idavidrein/gpqa", "gpqa_diamond")
    gpqa_extended = load_dataset("Idavidrein/gpqa", "gpqa_extended")

    # Convert to sets of Record IDs for comparison
    diamond_ids = set(gpqa_diamond['train']['Record ID'])
    extended_ids = set(gpqa_extended['train']['Record ID'])

    # Find questions that are in extended but not in diamond
    unique_ids = extended_ids - diamond_ids

    # Create a list to store the unique questions with their answers and explanations
    unique_questions = []

    # Iterate through extended dataset to find matching questions
    for item in gpqa_extended['train']:
        if item['Record ID'] in unique_ids:
            # Create list of options and shuffle them
            options = [
                item['Correct Answer'],
                item['Incorrect Answer 1'],
                item['Incorrect Answer 2'],
                item['Incorrect Answer 3']
            ]
            
            # Create formatted question with options
            formatted_question = f"Question: {item['Question']}\n\nOptions:\n"
            for i, option in enumerate(options):
                formatted_question += f"({chr(65+i)}) {option}\n"

            unique_questions.append({
                'id': item['Record ID'],
                'question': formatted_question.strip(),
                'correct_answer': item['Correct Answer'],
                'explanation': item['Explanation']
            })

    # Save to JSON file
    output_path = 'unique_gpqa_questions.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(unique_questions, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(unique_questions)} unique questions to {output_path}")

if __name__ == "__main__":
    get_unique_gpqa_questions()
