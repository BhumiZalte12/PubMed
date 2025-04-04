import pytest
from pubmed_papers.filter import filter_non_academic_authors

SAMPLE_PAPERS = [
    {
        "PubmedID": "123",
        "Title": "Test Paper",
        "Publication Date": "2023",
        "Authors": [{"name": "John Doe"}],
        "Affiliations": "University of Test",
        "Corresponding Author Email": "john@university.edu"
    },
    {
        "PubmedID": "456",
        "Title": "Pharma Paper",
        "Publication Date": "2023",
        "Authors": [{"name": "Jane Smith"}],
        "Affiliations": "Pharma Inc",
        "Corresponding Author Email": "jane@pharma.com"
    }
]

def test_filter_non_academic():
    """Test filtering of non-academic papers"""
    filtered = filter_non_academic_authors(SAMPLE_PAPERS)
    assert len(filtered) == 1
    assert filtered[0]["PubmedID"] == "456"