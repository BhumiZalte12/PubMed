import requests
from typing import List, Dict

def fetch_papers(query: str) -> List[Dict]:
    """
    Fetches research papers from PubMed based on the query and extracts required details.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Adjust for more results
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    paper_details = []
    
    for paper_id in paper_ids:
        paper_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        paper_params = {
            "db": "pubmed",
            "id": paper_id,
            "retmode": "json"
        }
        
        paper_response = requests.get(paper_url, params=paper_params)
        paper_data = paper_response.json()
        
        result = paper_data.get("result", {}).get(paper_id, {})
        
        paper_details.append({
            "PubmedID": paper_id,
            "Title": result.get("title", "No title available"),
            "Publication Date": result.get("pubdate", "Unknown"),
            "Authors": result.get("authors", []),  # List of authors
            "Affiliations": result.get("source", ""),  # Placeholder, detailed parsing needed
            "Corresponding Author Email": result.get("corresponding_author", {}).get("email", "N/A")
        })

    return paper_details
