# suggest_tools.py
def suggest_tools_for_use_case(industry):
    tools = []

    if industry.lower() == "retail industry":
        tools.append("Automated Inventory Management System")
        tools.append("AI-powered Customer Feedback Analysis")
    elif industry.lower() == "healthcare":
        tools.append("GenAI-powered Healthcare Document Search")
        tools.append("AI-based Clinical Report Generation Tools")
        print(f"Generated tools for {industry}: {tools}")
    
    return tools

def save_tools_to_markdown(tools, industry):
    with open(f"data/{industry}_tools.md", "w") as file:
        for tool in tools:
            file.write(f"- {tool}\n")  # Writing tools to the markdown file
    print(f"Tools for {industry} saved.")
