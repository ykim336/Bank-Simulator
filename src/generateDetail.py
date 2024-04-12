from .datasetManager import *
from openai import *
import json

PROMPT_FILEPATH = "dataset\primedPrompts.json"
client = OpenAI()

# Generates a string response of the specific model
def generator(model_version, prompt, user_input):
    completion = client.chat.completions.create(
        model=model_version,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return (completion.choices[0].message.content)

# Tests the database
def test_dataset(filename="blankets_titles.jsonl"):
    dataset=load_data(filename)
    format_validation(dataset)

# Extracts prompts from a .json file in the statics folder
def extract_prompts(filename=PROMPT_FILEPATH):
    with open(filename, "r") as f:
        return json.load(f)

# Generates the details for the listing based on the product type and user input. 
def generate_details(shopname, user_input):
    load = extract_prompts()
    previous_response = ""
    while True:
        title = generator(load["shopnames"][shopname]["models"][0], load["prompts"]["title"], f"Theme: {user_input, shopname} + Previous Response: {previous_response}")
        if 135 <= len(title) <= 140:
            break
    while True:
        tag = generator(load["shopnames"][shopname]["models"][1], load["prompts"]["tag"], f"Theme: {user_input, shopname} + Title: {title} + Previous Response: {previous_response}")
        commas = tag.split(', ')
        if len(commas) == 13:
            character_check = True
            for i in commas:
                if len(i) > 20:
                    character_check = False
            if character_check:
                break
    description = generator(load["shopnames"][shopname]["models"][2], load["prompts"]["description"], f"Theme: {user_input, shopname} + Title: {title} + Tags: {tag}")
    return {"title":title, "tag":tag, "description":description}

def testing_functions():
    user_input = input("Theme: ")
    print(generate_details("customblankets4u", user_input))

