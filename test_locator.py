from services.page_locator import locate_financial_pages

results = locate_financial_pages(
    "uploads/annual report 2024-25 Infosys.pdf"
)

print("\n========== Candidate Pages ==========\n")

for section, pages in results.items():

    print(f"\n{section.upper()}")

    for page in pages:

        print(
            f"Page {page['page']}   Score {page['score']}"
        )