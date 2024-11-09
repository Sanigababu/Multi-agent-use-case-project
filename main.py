from dotenv import load_dotenv
import os
import sys

# Set up paths for utils and agents folders
sys.path.append('C:/Users/HP/OneDrive/Desktop/Multi Agent_use case project/utils')
sys.path.append('C:/Users/HP/OneDrive/Desktop/Multi Agent_use case project/agents')

# Load API keys from .env file
load_dotenv()
serper_api_key = os.getenv("SERPER_API_KEY")

# Import necessary functions
from agents.industry_research_agent import research_workflow
from utils.web_scraping_utils import search_ai_trends
from agents.use_case_generation import generate_use_cases
from agents.search_kaggle import search_kaggle_datasets

# Define functions directly in main.py if they are not available elsewhere

def save_use_cases_to_json(use_cases, industry):
    import json
    with open(f"{industry}_use_cases.json", "w") as f:
        json.dump(use_cases, f, indent=4)
    print(f"Use cases for {industry} saved to {industry}_use_cases.json.")

def save_datasets_to_markdown(datasets, industry):
    with open(f"{industry}_datasets.md", "w") as f:
        for dataset in datasets:
            f.write(f"- [{dataset['name']}]({dataset['link']})\n")
    print(f"Datasets for {industry} saved to {industry}_datasets.md.")

def save_tools_to_markdown(tools, industry):
    with open(f"{industry}_tools.md", "w") as f:
        for tool in tools:
            f.write(f"- {tool}\n")
    print(f"Tools for {industry} saved to {industry}_tools.md.")

def suggest_tools_for_use_case(industry):
    tools = []

    # Example: Suggest tools based on industry
    if industry.lower() == "retail":
        tools = [
            "AI-powered Analytics Tools", 
            "Personalization Engines", 
            "Customer Sentiment Analysis Tools"
        ]
    elif industry.lower() == "healthcare":
        tools = [
            "AI Diagnostics Tools",
            "Patient Data Management Systems",
            "Medical Imaging Analysis Tools"
        ]
    elif industry.lower() == "finance":
        tools = [
            "Fraud Detection Tools",
            "Algorithmic Trading Systems",
            "Risk Assessment Tools"
        ]
    # Add more industries as needed
    else:
        tools = ["General-purpose AI Tools", "Data Analysis Tools"]

    print(f"Suggested tools for {industry}: {tools}")  # For debugging

    return tools


def main(industry="Retail", company_name="ExampleCompany"):
    print("Starting market research...")

    # Research industry and company info
    research_data = research_workflow(company_name, industry)
    print(f"Research data for {company_name} in {industry}: {research_data}")

    # Step 1: Search for AI trends in the given industry
    trends_data = search_ai_trends(industry)

    # Step 2: Generate use cases based on the trends
    use_cases = generate_use_cases(trends_data, industry)

    # Step 3: Save the use cases to a JSON file
    save_use_cases_to_json(use_cases, industry)
    print(f"Generated and saved use cases for {industry}.")

    # Collect relevant Kaggle datasets
    kaggle_datasets = search_kaggle_datasets(f"{industry} dataset")
    datasets = [{"name": dataset.title, "link": dataset.url} for dataset in kaggle_datasets]
    save_datasets_to_markdown(datasets, industry)
    print(f"Kaggle datasets for {industry} saved successfully.")

    # Suggest tools for the generated use cases and save to Markdown
    tools = suggest_tools_for_use_case(industry)
    save_tools_to_markdown(tools, industry)
    print(f"Tools for {industry} saved successfully.")

    print("Process completed.")

if __name__ == "__main__":
    main()
