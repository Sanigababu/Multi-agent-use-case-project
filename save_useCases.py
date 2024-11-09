import json

def save_use_cases_to_json(use_cases, industry):
    output_data = {
        "industry": industry,
        "use_cases": use_cases
    }
    
    # Save the generated use cases to a JSON file
    with open(f"data/{industry}_use_cases.json", "w") as file:
        json.dump(output_data, file, indent=4)

def load_use_cases_from_json(industry):
    try:
        with open(f"data/{industry}_use_cases.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"No use cases found for {industry}.")
        return None
