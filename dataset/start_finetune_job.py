import os
import pandas as pd
from pathlib import Path
from openai import OpenAI
import json

# Initialize OpenAI client (replace with your API key or use environment variable)
client = OpenAI()

def load_ai_questions():
    # Get the path to the ai questions directory
    ai_dir = Path("ai")
    
    # Check if directory exists
    if not ai_dir.exists():
        raise FileNotFoundError(f"Directory not found: {ai_dir}")
    
    questions = []
    answers = []
    
    # Iterate through all markdown files in the directory and its subdirectories
    for file_path in ai_dir.rglob("*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Split the content by "Question:" and take everything after it
                parts = content.split("Question:")
                if len(parts) > 1:
                    qa_part = parts[1]
                    # Split by "Answer:" to separate question and answer
                    qa_split = qa_part.split("Answer:")
                    
                    if len(qa_split) > 1:
                        question = qa_split[0].strip()
                        answer = qa_split[1].strip()
                        
                        if question and answer:
                            questions.append(question)
                            answers.append(answer)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            continue
    
    # Create a DataFrame
    df = pd.DataFrame({
        'question': questions,
        'answer': answers
    })
    
    return df

def create_fine_tuning_job(df):
    # Convert DataFrame to the required format
    training_data = []
    for _, row in df.iterrows():
        training_example = {
            "messages": [
                {"role": "user", "content": row['question']},
                {"role": "assistant", "content": row['answer']}
            ]
        }
        training_data.append(training_example)
    
    # Save the formatted data
    output_file = "training_data.jsonl"
    with open(output_file, 'w') as f:
        for item in training_data:
            f.write(json.dumps(item) + '\n')
    
    # Upload the training file
    with open(output_file, 'rb') as f:
        training_file = client.files.create(
            file=f,
            purpose="fine-tune"
        )
    
    # Create fine-tuning job
    job = client.fine_tuning.jobs.create(
        training_file=training_file.id,
        model="gpt-3.5-turbo",  # or your preferred model
        hyperparameters={
            "n_epochs": 3
        }
    )
    
    return job

if __name__ == "__main__":
    # Load the dataset
    df = load_ai_questions()
    print(f"Loaded {len(df)} question-answer pairs")
    
    # Start fine-tuning
    job = create_fine_tuning_job(df)
    print(f"\nFine-tuning job created successfully!")
    print(f"Job ID: {job.id}")
    print(f"Status: {job.status}")
