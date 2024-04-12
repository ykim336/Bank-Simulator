import json
import csv
import tiktoken
import numpy as np
from collections import defaultdict

encoding = tiktoken.get_encoding("cl100k_base")

def csv_to_json(csv_file_path, json_file_path, prompt):
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file: # Read CSV file
        csv_reader = csv.reader(csv_file)
        with open(json_file_path, 'w', encoding='utf-8') as json_file: # Iterate over rows in the CSV file
            for row in csv_reader: # Extract data from CSV columns
                title = row[0]  # Assuming the title is in the first column
                message_set = [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": "Default"},
                    {"role": "assistant", "content": title}
                ] # Create JSON messages for each title

                json.dump({"messages": message_set}, json_file, ensure_ascii=False) # Write the JSON structure followed by a newline
                json_file.write('\n')

def load_data(data_path):
    # Load the dataset
    with open(data_path, 'r', encoding='utf-8') as f:
        dataset = [json.loads(line) for line in f]
    return dataset

def format_validation(dataset):
    # Format error checks
    format_errors = defaultdict(int)

    # Data Type Check: Checks whether each entry in the dataset is a dictionary (dict). 
    for ex in dataset:
        if not isinstance(ex, dict):
            format_errors["data_type"] += 1
            continue
            
    # Presence of Message List: Checks if a messages list is present in each entry. 
        messages = ex.get("messages", None)
        if not messages:
            format_errors["missing_messages_list"] += 1
            continue
    
    # Message Keys Check: Validates that each message in the messages list contains the keys role and content. 
        for message in messages:
            if "role" not in message or "content" not in message:
                format_errors["message_missing_key"] += 1
            
        # Unrecognized Keys in Messages: Logs if a message has keys other than role, content, and name.
            if any(k not in ("role", "content", "name", "function_call") for k in message):
                format_errors["message_unrecognized_key"] += 1
            
        # Role Validation: Ensures the role is one of "system", "user", or "assistant". 
            if message.get("role", None) not in ("system", "user", "assistant", "function"):
                format_errors["unrecognized_role"] += 1

        # Content Validation: Verifies that content has textual data and is a string.         
            content = message.get("content", None)
            function_call = message.get("function_call", None)
            
            if (not content and not function_call) or not isinstance(content, str):
                format_errors["missing_content"] += 1
    
    # Assistant Message Presence: Checks that each conversation has at least one message from the assistant. 
        if not any(message.get("role", None) == "assistant" for message in messages):
            format_errors["example_missing_assistant_message"] += 1

    if format_errors:
        print("Found errors:")
        for k, v in format_errors.items():
            print(f"{k}: {v}")
    else:
        print("No errors found")

def num_tokens_from_messages(messages, tokens_per_message=3, tokens_per_name=1):
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens

def num_assistant_tokens_from_messages(messages):
    num_tokens = 0
    for message in messages:
        if message["role"] == "assistant":
            num_tokens += len(encoding.encode(message["content"]))
    return num_tokens

def print_distribution(values, name):
    print(f"\n#### Distribution of {name}:")
    print(f"min / max: {min(values)}, {max(values)}")
    print(f"mean / median: {np.mean(values)}, {np.median(values)}")
    print(f"p5 / p95: {np.quantile(values, 0.1)}, {np.quantile(values, 0.9)}")

def add_spaces(input_file, output_file):
    # Open the CSV file for reading
    with open(input_file, 'r') as file:
        # Read the CSV content
        csv_content = list(csv.reader(file))

    # Add spaces and quotes to each string in the CSV
    csv_content_with_spaces_and_quotes = ['"' + ', '.join(s.strip() for s in row[0].split(',')) + '"' for row in csv_content]

    # Open the CSV file for writing
    with open(output_file, 'w', newline='') as file:
        # Write the modified content back to the CSV
        file.write('\n'.join(csv_content_with_spaces_and_quotes))
