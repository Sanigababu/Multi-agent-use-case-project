# save_tools.py
def save_tools_to_markdown(tools, industry):
    with open(f"data/{industry}_tools.md", "w") as file:
        file.write(f"### Suggested Tools for {industry} Use Cases\n\n")
        for tool in tools:
            file.write(f"- {tool}\n")
