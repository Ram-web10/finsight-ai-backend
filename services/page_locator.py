import fitz
from typing import Dict, List

SECTION_RULES = {
    "income_statement": {
        "title": [
            "statement of profit and loss",
            "statement of income",
            "statement of earnings",
            "consolidated statement of profit and loss",
            "consolidated statement of income",
            "income statement"
        ],
        "keywords": [
            "revenue",
            "net sales",
            "other income",
            "finance cost",
            "employee benefit",
            "profit before tax",
            "profit after tax",
            "earnings per share",
            "eps",
            "operating profit",
            "total income"
        ]
    },

    "balance_sheet": {
        "title": [
            "balance sheet",
            "statement of financial position",
            "consolidated balance sheet"
        ],
        "keywords": [
            "total assets",
            "share capital",
            "borrowings",
            "cash and cash equivalents",
            "trade receivables",
            "inventories",
            "current liabilities",
            "non-current assets",
            "equity",
            "total equity",
            "total liabilities"
        ]
    },

    "cash_flow": {
        "title": [
            "cash flow statement",
            "statement of cash flows",
            "consolidated cash flow statement"
        ],
        "keywords": [
            "operating activities",
            "investing activities",
            "financing activities",
            "cash and cash equivalents",
            "net increase in cash",
            "net cash generated",
            "net cash used"
        ]
    }
}


def score_page(text: str, rule: Dict) -> int:
    score = 0

    text = text.lower()

    # High weight for exact title
    for title in rule["title"]:
        if title in text:
            score += 50

    # Medium weight for keywords
    for keyword in rule["keywords"]:
        if keyword in text:
            score += 5

    # Bonus if many keywords are present
    keyword_matches = sum(
        keyword in text for keyword in rule["keywords"]
    )

    if keyword_matches >= 5:
        score += 20

    return score


def locate_financial_pages(pdf_path: str, top_n: int = 3) -> Dict[str, List[Dict]]:

    doc = fitz.open(pdf_path)

    results = {}

    # Ignore cover pages but still search most of the report
    start_page = max(0, int(len(doc) * 0.20))

    for section, rule in SECTION_RULES.items():

        candidates = []

        for page_number in range(start_page, len(doc)):

            page = doc.load_page(page_number)

            text = page.get_text("text")

            if not text.strip():
                continue

            score = score_page(text, rule)

            if score > 0:
                candidates.append({
                    "page": page_number + 1,
                    "score": score
                })

        candidates.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        results[section] = candidates[:top_n]

    doc.close()

    return results