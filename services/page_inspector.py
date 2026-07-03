import fitz
import re
from typing import Dict


def inspect_page(pdf_path: str, page_number: int) -> Dict:
    """
    Inspect a single PDF page and return detailed information.

    Args:
        pdf_path (str): Path to the PDF.
        page_number (int): 1-based page number.

    Returns:
        dict: Page statistics and preview.
    """

    doc = fitz.open(pdf_path)

    try:
        if page_number < 1 or page_number > len(doc):
            raise ValueError(
                f"Page {page_number} is out of range. PDF has {len(doc)} pages."
            )

        page = doc.load_page(page_number - 1)

        text = page.get_text("text")

        words = len(text.split())

        numbers = len(
            re.findall(r"\b\d[\d,.\-()%]*\b", text)
        )

        tables_detected = (
            "total assets" in text.lower()
            or "revenue" in text.lower()
            or "cash flow" in text.lower()
            or "balance sheet" in text.lower()
            or "profit before tax" in text.lower()
        )

        preview = text[:1000]

        return {
            "page": page_number,
            "word_count": words,
            "number_count": numbers,
            "character_count": len(text),
            "tables_detected": tables_detected,
            "preview": preview
        }

    finally:
        doc.close()