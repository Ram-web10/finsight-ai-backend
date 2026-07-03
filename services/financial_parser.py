import re
import pandas as pd
from typing import List, Dict

# ==========================================================
# FINANCIAL FIELD ALIASES
# ==========================================================

FIELD_ALIASES = {

    "Revenue": [
        "Revenue",
        "Revenue from Operations",
        "Total Revenue",
        "Sales",
        "Net Sales",
        "Turnover",
        "Operating Revenue",
        "Income from Operations"
    ],

    "Net Profit": [
        "Net Profit",
        "Profit After Tax",
        "PAT",
        "Profit for the Year",
        "Net Income",
        "Profit attributable to owners"
    ],

    "Operating Profit": [
        "Operating Profit",
        "EBIT",
        "Operating Income"
    ],

    "EBITDA": [
        "EBITDA",
        "Operating EBITDA"
    ],

    "Profit Before Tax": [
        "Profit Before Tax",
        "PBT",
        "Profit before tax"
    ],

    "EPS": [
        "EPS",
        "Earnings Per Share",
        "Basic EPS",
        "Diluted EPS"
    ],

    "Total Assets": [
        "Total Assets",
        "Assets"
    ],

    "Total Liabilities": [
        "Total Liabilities",
        "Liabilities"
    ],

    "Shareholders Equity": [
        "Equity",
        "Total Equity",
        "Shareholders Equity",
        "Total Shareholders' Equity",
        "Net Worth"
    ],

    "Current Assets": [
        "Current Assets"
    ],

    "Current Liabilities": [
        "Current Liabilities"
    ],

    "Cash": [
        "Cash",
        "Cash and Cash Equivalents",
        "Cash & Cash Equivalents"
    ],

    "Inventory": [
        "Inventory",
        "Inventories"
    ],

    "Borrowings": [
        "Borrowings",
        "Total Borrowings"
    ],

    "Operating Cash Flow": [
        "Operating Cash Flow",
        "Cash Flow from Operating Activities"
    ],

    "Investing Cash Flow": [
        "Cash Flow from Investing Activities"
    ],

    "Financing Cash Flow": [
        "Cash Flow from Financing Activities"
    ]
}

# ==========================================================
# NORMALIZATION HELPERS
# ==========================================================

def normalize_label(label: str) -> str:
    """
    Normalize table labels for matching.
    """
    if label is None:
        return ""
    return re.sub(r"\s+", " ", str(label)).strip().lower()


def clean_number(value):
    """
    Convert financial values into float.

    Handles:
        ₹12,345
        (12,345)
        12,345 Cr
        12,345 Million
        12,345 Billion
        -
        N/A
    """

    if value is None:
        return None

    value = str(value).strip()

    if value in ["", "-", "--", "N/A", "nan"]:
        return None

    negative = False

    if value.startswith("(") and value.endswith(")"):
        negative = True
        value = value[1:-1]

    value = value.replace("₹", "").replace("$", "").replace(",", "").strip()

    multiplier = 1
    lower = value.lower()

    if "crore" in lower or "cr" in lower:
        multiplier = 10_000_000
    elif "million" in lower:
        multiplier = 1_000_000
    elif "billion" in lower:
        multiplier = 1_000_000_000

    value = re.sub(r"(crore|cr|million|billion)", "", value, flags=re.IGNORECASE).strip()

    try:
        number = float(value)
        if negative:
            number *= -1
        return number * multiplier
    except Exception:
        return None

# ==========================================================
# TABLE-BASED EXTRACTION ENGINE
# ==========================================================

def extract_financial_data_from_tables(tables: List[pd.DataFrame]) -> Dict:
    """
    Extract financial metrics from PDF tables using alias matching.
    """

    extracted_data = {key: None for key in FIELD_ALIASES.keys()}

    for table in tables:

        if table is None or table.empty:
            continue

        table = table.fillna("").astype(str)

        for _, row in table.iterrows():

            row_values = [str(v) for v in row.values]

            for col_index, cell in enumerate(row_values):

                normalized_cell = normalize_label(cell)

                if not normalized_cell:
                    continue

                for field_name, aliases in FIELD_ALIASES.items():

                    for alias in aliases:

                        if alias.lower() in normalized_cell:

                            value = None

                            if col_index + 1 < len(row_values):
                                value = row_values[col_index + 1]
                            else:
                                value = row_values[-1]

                            cleaned = clean_number(value)

                            if cleaned is not None:
                                extracted_data[field_name] = cleaned

    return extracted_data

# ==========================================================
# TEXT-BASED FALLBACK EXTRACTION
# ==========================================================

def extract_financial_data(text: str) -> Dict:
    """
    Regex fallback extraction from raw PDF text.
    """

    results = {key: None for key in FIELD_ALIASES.keys()}

    clean_text = text.replace(",", "")

    for field, aliases in FIELD_ALIASES.items():

        for alias in aliases:

            pattern = rf"{re.escape(alias)}\s*[:\-]?\s*([\d\.\(\)]+(?:\s*(cr|crore|million|billion))?)"

            matches = re.findall(pattern, clean_text, re.IGNORECASE)

            if matches:

                raw_value = matches[0][0]
                cleaned = clean_number(raw_value)

                if cleaned is not None:
                    results[field] = cleaned
                    break

    return results