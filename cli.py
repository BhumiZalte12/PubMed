import typer
import pandas as pd
from pubmed_papers.fetch import fetch_papers
from pubmed_papers.filter import filter_non_academic_authors

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "-f", "--file", help="Filename to save the results"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug mode")
):
    """
    Fetches research papers from PubMed and filters papers with non-academic authors.
    """
    if debug:
        typer.echo(f"Debug: Fetching papers for query: {query}")

    papers = fetch_papers(query)
    filtered_papers = filter_non_academic_authors(papers)

    df = pd.DataFrame(filtered_papers)

    if file:
        df.to_csv(file, index=False)
        typer.echo(f"Results saved to {file}")
    else:
        typer.echo(df.to_string())

if __name__ == "__main__":
    app()
