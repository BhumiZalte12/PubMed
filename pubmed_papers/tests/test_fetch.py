import pytest
from pubmed_papers.fetch import fetch_papers

def test_fetch_papers_basic():
    """Test that fetch_papers returns a list"""
    results = fetch_papers("cancer", max_results=1)
    assert isinstance(results, list)
    if results:  # If we got results
        assert 'PubmedID' in results[0]
        assert 'Title' in results[0]