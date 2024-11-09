from utils.web_scraping_utils import scrape_industry_info, research_company_info
import json

def research_workflow(company_name, industry_name):
    print("Loading industry_research_agent...")

    # Step 1: Scrape industry information
    industry_info = scrape_industry_info(industry_name)
    
    # Step 2: Scrape company-specific information
    company_info = research_company_info(company_name)
    
    # Step 3: Compile the information
    research_data = {
        "industry": industry_name,
        "industry_info": industry_info,
        "company_overview": company_info.get(f"{company_name} market analysis", "No data found"),
        "products": [item['title'] for item in company_info.get(f"{company_name} key products", [])],
        "strategic_focus": ["AI initiatives", "Automation", "Improving customer experience"],  # Placeholder
    }
    
    # Step 4: Save to a JSON file
    with open('data/research_data.json', 'w') as f:
        json.dump(research_data, f, indent=4)
    pass
    return research_data
