def generate_use_cases(trends_data, industry):
    use_cases = []

    # Example: Generate use cases for Healthcare Industry
    if industry.lower() == "healthcare":
        use_cases.append({
            "name": "AI-driven Diagnostics",
            "description": "Use AI algorithms to analyze medical images and diagnose diseases."
        })
        use_cases.append({
            "name": "Patient Management System",
            "description": "Implement AI to manage patient information and predict treatment plans."
        })
    elif industry.lower() == "retail":
        use_cases.append({
            "name": "AI Inventory Management",
            "description": "Use AI for demand forecasting to optimize stock levels."
        })
        use_cases.append({
            "name": "Customer Recommendation System",
            "description": "ML models to personalize shopping recommendations based on customer behavior."
        })
    # Add other industries here
    
    
    # Save the use cases to the markdown file
    with open(f"data/{industry}_use_cases.md", "w") as file:
        for case in use_cases:
            file.write(f"### {case['name']}\n{case['description']}\n\n")
    print(f"Use cases for {industry} saved.")
    
    return use_cases