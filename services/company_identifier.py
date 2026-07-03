import re


def identify_company(text: str):
    """
    Extract company information from the annual report.
    """

    company_name = "Unknown Company"

    patterns = [
        r"([A-Z][A-Za-z&.,\-\s]+?)\s+Limited",
        r"([A-Z][A-Za-z&.,\-\s]+?)\s+Ltd",
        r"([A-Z][A-Za-z&.,\-\s]+?)\s+Corporation",
        r"([A-Z][A-Za-z&.,\-\s]+?)\s+Inc",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)

        if match:
            company_name = match.group(0).strip()
            break

    return {
        "name": company_name,
        "report_type": "Annual Report",
    }