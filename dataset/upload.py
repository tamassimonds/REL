from datasets import Dataset, DatasetDict
import json
import glob
import os
from tqdm import tqdm
import random
from huggingface_hub import login, DatasetCard

# Remove the hardcoded token and use login() instead
login("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")  # This will use the token from HF_TOKEN environment variable

def load_reasonset_data(directory_path):
    """
    Load all JSON files from the ReasonSet directory and normalize their structure.
    """
    all_data = []
    empty_working_count = 0
    
    # Get all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, "*.json"))
    
    for file_path in tqdm(json_files, desc="Loading files"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Modified to handle different solution formats
                if isinstance(data['solution'], str):
                    example = {
                        'problem': data['problem'],
                        'working_out': '',  # Empty string since no working out in this case
                        'provided_solution': data['ground_truth']
                    }
                else:
                    # Get working_out, falling back to final_solution if working_out is empty
                    working_out = data['solution'].get('working_out', '')
                    if not working_out:
                        working_out = data['solution'].get('final_solution', '')
                        if not working_out:
                            empty_working_count += 1
                            print(f"Warning: Empty working_out in {file_path}")
                    
                    example = {
                        'problem': data['problem'],
                        'working_out': working_out,
                        'provided_solution': data['ground_truth']
                    }
                all_data.append(example)
                
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            continue
    
    print(f"\nTotal files with empty working_out: {empty_working_count}")
    return all_data

def split_data(data, train_ratio=1, val_ratio=0, test_ratio=0):
    """
    Split data into train, validation and test sets.
    """
    # Since we only want training data, just return all data as train
    return data, [], []

def create_dataset(directory_path):
    """
    Create and return a DatasetDict object.
    """
    # Load all data
    all_data = load_reasonset_data(directory_path)
    print(f"Loaded {len(all_data)} examples")
    
    # Split data (will return all data as train)
    train_data, _, _ = split_data(all_data)
    print(f"Using all {len(train_data)} examples for training")
    
    # Create dataset
    train_dataset = Dataset.from_list(train_data)
    
    # Create dataset dictionary with only train split
    dataset_dict = DatasetDict({
        'train': train_dataset
    })
    
    return dataset_dict

def main():
    # Set paths
    directory_path = "ReasonSet"
    
    # Create dataset
    print("Creating dataset...")
    dataset = create_dataset(directory_path)
    
    # Push to hub
    print("Pushing to Hugging Face Hub...")
    dataset.push_to_hub(
        "TamasSimonds/ReasonSet",
        private=False
    )
    print("Upload complete!")

if __name__ == "__main__":
    main()
