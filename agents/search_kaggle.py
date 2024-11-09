from kaggle.api.kaggle_api_extended import KaggleApi

# Function to search for datasets on Kaggle
def search_kaggle_datasets(query):
    api = KaggleApi()
    api.authenticate()
    
    # Search datasets based on the query
    datasets = api.dataset_list(search=query)
    
    # Return the list of datasets found
    return datasets
# search_huggingface.py
import requests
from bs4 import BeautifulSoup

def search_huggingface_datasets(query):
    url = f"https://huggingface.co/datasets?search={query}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        datasets = soup.find_all('a', class_="link-secondary")
        dataset_links = [f"https://huggingface.co{a['href']}" for a in datasets]
        return dataset_links
    else:
        print(f"Error fetching Hugging Face datasets: {response.status_code}")
        return []

# search_github.py
import requests
from bs4 import BeautifulSoup

def search_github_repositories(query):
    url = f"https://github.com/search?q={query}+dataset&type=repositories"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        repos = soup.find_all('a', class_="v-align-middle")
        repo_links = [f"https://github.com{a['href']}" for a in repos]
        return repo_links
    else:
        print(f"Error fetching GitHub repositories: {response.status_code}")
        return []

# Example usage:
if __name__ == "__main__":
    query = "retail industry"
    datasets = search_kaggle_datasets(query)
    
    # Print the names and URLs of the datasets
    for dataset in datasets:
        print(f"Dataset: {dataset.title}")
        print(f"URL: https://www.kaggle.com/datasets/{dataset.ref}")
        print()
