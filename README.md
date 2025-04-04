# PubMed Research Papers Fetcher

A Python tool to fetch and filter research papers from PubMed with pharmaceutical/biotech company affiliations.

## Features

- Fetch papers from PubMed using their API
- Filter papers with non-academic (industry) affiliations
- Export results to CSV
- Command-line interface with options
- Type-annotated Python code
- Configurable result limits

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BhumiZalte12/PubMed.git
   cd PubMed


## install dependencies using Poetry:

poetry install


## Usage
Command Line Interface
Basic usage:

poetry run python -m cli "search query" -f output.csv
Options:

-f/--file: Output CSV file path (optional)

-d/--debug: Enable debug mode

-h/--help: Show help message

## Example:

# Search for cancer research papers and save to results.csv
poetry run python -m cli "cancer research" -f results.csv

# Show results in console without saving
poetry run python -m cli "diabetes treatment"

## As a Python Module

from pubmed_papers.fetch import fetch_papers
from pubmed_papers.filter import filter_non_academic_authors

# Fetch papers
papers = fetch_papers("cancer immunotherapy", max_results=20)

# Filter for industry-affiliated papers
filtered = filter_non_academic_authors(papers)

## Output Format

The CSV file contains these columns:

PubmedID: Unique PubMed identifier

Title: Paper title

Publication Date: Publication date

Non-academic Author(s): Authors with industry affiliations

Company Affiliation(s): Pharmaceutical/biotech companies

Corresponding Author Email: Email of corresponding author

## Dependencies
Python 3.8+

Poetry (for dependency management)

## Required packages:

requests - HTTP requests

pandas - Data handling

typer - CLI framework

## Testing
Run tests with:

poetry run pytest

## Contributing
Fork the repository

Create a new branch

Make your changes

Submit a pull request

## License
MIT License

## Acknowledgments
PubMed/E-utilities API

Python community packages