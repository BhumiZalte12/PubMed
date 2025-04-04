from typing import List, Dict

def filter_non_academic_authors(papers: List[Dict]) -> List[Dict]:
    """
    Filters out academic authors and extracts non-academic affiliations.
    """
    filtered_papers = []
    
    company_keywords = ["pharma", "biotech", "inc.", "corp", "gmbh", "ltd", "company"]

    for paper in papers:
        affiliations = paper.get("Affiliations", "").lower()
        authors = paper.get("Authors", [])

        # Extract author names from the author dictionaries
        author_names = [author.get("name", "") for author in authors]
        
        company_affiliations = [aff for aff in affiliations.split(";") if any(keyword in aff for keyword in company_keywords)]

        if company_affiliations:
            paper["Non-academic Author(s)"] = ", ".join(author_names) if author_names else "N/A"
            paper["Company Affiliation(s)"] = ", ".join(company_affiliations)
            filtered_papers.append(paper)

    return filtered_papers