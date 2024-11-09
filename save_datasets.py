# save_datasets.py
def save_datasets_to_markdown(datasets, industry):
    filename = f"{industry}_datasets.md"
    markdown_content = f"# {industry.capitalize()} Datasets\n\n"
    
    for dataset in datasets:
        markdown_content += f"- [{dataset['name']}]({dataset['link']})\n"
    
    # Open the file with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as file:
        file.write(markdown_content)
    print(f"Saved datasets to {filename}")

