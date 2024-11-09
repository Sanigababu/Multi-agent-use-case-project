import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("SERPER_API_KEY")
exa_api_key = os.getenv("EXA_API_KEY")

def scrape_industry_info(industry):
    query = industry.replace(" ", "_")  # Replace spaces with underscores for URL format
    url = f"https://en.wikipedia.org/wiki/{query}"  # Wikipedia page for the industry
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the first paragraph or summary for industry information
        industry_summary = soup.find('p').text
        return industry_summary
    else:
        return f"Could not fetch data for {industry}"

def search_serper(query):
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    url = "https://api.serper.dev/search"
    payload = {
        "q": query,
        "location": "United States"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns a JSON with search results
    else:
        print(f"Error: {response.status_code}")
        return None
    
def search_exa(query):
    headers = {
        "Authorization": f"Bearer {exa_api_key}"
    }
    url = f"https://serpapi.com/search?q={query}&api_key=SERPA_API_Key"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns JSON with search results
    else:
        print(f"Error: {response.status_code}")
        return None


def research_company_info(company_name):
    queries = [
        f"{company_name} market analysis",
        f"{company_name} key products",
        f"{company_name} AI initiatives",
        f"{company_name} strategic focus",
    ]
    company_info = {}
    
    for query in queries:
        result = search_serper(query)
        if result:
            company_info[query] = result['organic_results']
    
    return company_info

def scrape_trends_from_report(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = " ".join([p.text for p in paragraphs])
        return text
    return "Could not scrape the report."

def search_ai_trends(industry):
    # Search for AI trends in the specific industry
    search_query = f"AI trends in {industry} 2024"
    trends_data = search_serper(search_query)
    
    # If Serper API didn't return sufficient data, fall back to Exa API or web scraping
    if not trends_data:
        trends_data = search_exa(search_query)
    if not trends_data:
        # Scrape a report if no API data is available
        trends_data = scrape_trends_from_report(f"https://example.com/ai-trends-in-{industry}")
    
    return trends_data