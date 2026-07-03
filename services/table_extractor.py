import camelot
from typing import List
import pandas as pd


def extract_tables(pdf_path: str, page_number: int) -> List[pd.DataFrame]:
    """
    Extract tables from a specific PDF page.

    Tries Camelot Stream mode first.
    If no tables are found, automatically tries Lattice mode.

    Args:
        pdf_path (str): Path to PDF.
        page_number (int): 1-based page number.

    Returns:
        List[pd.DataFrame]: List of extracted tables.
    """

    try:
        # First attempt: Stream (works well for most annual reports)
        tables = camelot.read_pdf(
            pdf_path,
            pages=str(page_number),
            flavor="stream",
            strip_text="\n"
        )

        if len(tables) == 0:
            # Second attempt: Lattice (works for bordered tables)
            tables = camelot.read_pdf(
                pdf_path,
                pages=str(page_number),
                flavor="lattice"
            )

        extracted_tables = []

        for table in tables:
            df = table.df

            # Remove completely empty rows
            df = df.dropna(how="all")

            # Remove completely empty columns
            df = df.dropna(axis=1, how="all")

            # Reset indexing
            df = df.reset_index(drop=True)

            extracted_tables.append(df)

        return extracted_tables

    except Exception as e:
        print(f"Table Extraction Error (Page {page_number}): {e}")
        return []