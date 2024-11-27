import json
import random

# Read the original training data
with open('training_data.jsonl', 'r', encoding='utf-8') as f:
    training_data = [json.loads(line) for line in f]

# Read the synthetic training data
with open('synthetic_training_data.jsonl', 'r', encoding='utf-8') as f:
    synthetic_data = [json.loads(line) for line in f]

with open('synthetic_training_data2.jsonl', 'r', encoding='utf-8') as f:
    synthetic_data2 = [json.loads(line) for line in f]
# Duplicate training data 4x
training_data_4x = training_data * 2
# Duplicate synthetic data 4x
synthetic_data_4x = synthetic_data * 1
synthetic_data2_4x = synthetic_data2 * 1

# Combine the datasets
combined_data = training_data_4x + synthetic_data_4x + synthetic_data2_4x

# Shuffle the combined data
random.shuffle(combined_data)

# Write the combined data to a new file
with open('combined_training_data.jsonl', 'w', encoding='utf-8') as f:
    for item in combined_data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"Combined {len(training_data)} original examples (duplicated 4x = {len(training_data_4x)}) with "
      f"{len(synthetic_data)} synthetic examples (duplicated 2x = {len(synthetic_data_4x)}) and "
      f"{len(synthetic_data2)} synthetic2 examples (duplicated 2x = {len(synthetic_data2_4x)}).")
print(f"Total examples in combined dataset: {len(combined_data)}")
