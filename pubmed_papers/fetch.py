import requests
from typing import List, Dict, Optional
from requests.exceptions import RequestException

def fetch_papers(query: str, max_results: int = 10) -> List[Dict]:
    """
    Fetches research papers from PubMed based on the query and extracts required details.

    Args:
        query: PubMed search query string
        max_results: Maximum number of papers to return (default: 10, max: 100)

    Returns:
        List of dictionaries containing paper details with keys:
        - PubmedID: Unique PubMed identifier
        - Title: Paper title
        - Publication Date: Publication date
        - Authors: List of author dictionaries
        - Affiliations: Author affiliations
        - Corresponding Author Email: Email of corresponding author

    Raises:
        ValueError: If max_results is not between 1-100
        RequestException: If there's an error with the PubMed API request
    """
    # Validate max_results
    if not 1 <= max_results <= 100:
        raise ValueError("max_results must be between 1 and 100")

    try:
        # First API call to get paper IDs
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        search_params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": max_results,
            "sort": "relevance"  # Get most relevant results first
        }
        
        response = requests.get(search_url, params=search_params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        paper_ids = data.get("esearchresult", {}).get("idlist", [])
        if not paper_ids:
            return []  # No results found

        # Second API call to get paper details
        summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        summary_params = {
            "db": "pubmed",
            "id": ",".join(paper_ids),  # Get all papers at once
            "retmode": "json"
        }
        
        paper_response = requests.get(summary_url, params=summary_params, timeout=10)
        paper_response.raise_for_status()
        paper_data = paper_response.json()

        paper_details = []
        for paper_id in paper_ids:
            result = paper_data.get("result", {}).get(paper_id, {})
            
            # Extract authors with more detailed information
            authors = []
            for author in result.get("authors", []):
                authors.append({
                    "name": author.get("name", ""),
                    "authtype": author.get("authtype", ""),
                    "affiliation": author.get("affiliation", "")
                })

            paper_details.append({
                "PubmedID": paper_id,
                "Title": result.get("title", "No title available"),
                "Publication Date": result.get("pubdate", "Unknown"),
                "Authors": authors,
                "Affiliations": result.get("source", ""),
                "Corresponding Author Email": result.get("corresponding_uthor", {}).get("email", "N/A")
            })

        return paper_details

    except RequestException as e:
        raise RequestException(f"PubMed API request failed: {str(e)}")
    except ValueError as e:
        raise ValueError(f"Invalid parameter: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")