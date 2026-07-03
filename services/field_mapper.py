from typing import Dict

# Different companies use different names for the same financial metric.
FIELD_MAPPING = {
    "Revenue": "revenue",
    "Revenue from Operations": "revenue",
    "Net Sales": "revenue",
    "Sales": "revenue",
    "Total Income": "revenue",

    "Net Profit": "net_profit",
    "Profit After Tax": "net_profit",
    "PAT": "net_profit",
    "Profit for the year": "net_profit",

    "Operating Profit": "operating_profit",
    "Operating Income": "operating_profit",

    "EBITDA": "ebitda",

    "Total Assets": "total_assets",

    "Total Equity": "equity",
    "Shareholders' Equity": "equity",
    "Shareholder's Equity": "equity",
    "Equity": "equity",

    "Borrowings": "total_debt",
    "Total Debt": "total_debt",
    "Long-Term Borrowings": "total_debt",
    "Short-Term Borrowings": "total_debt",

    "Cash and Cash Equivalents": "cash",
    "Cash & Cash Equivalents": "cash",

    "Total Liabilities": "total_liabilities",

    "Basic EPS": "eps",
    "Earnings Per Share": "eps"
}


def map_fields(extracted_data: Dict) -> Dict:
    """
    Standardize extracted financial fields into a common schema.
    """

    standardized = {}

    for key, value in extracted_data.items():

        mapped_key = FIELD_MAPPING.get(key, key)

        standardized[mapped_key] = value

    return standardized