from services.table_extractor import extract_tables

PDF = "uploads/annual report 2024-25 Infosys.pdf"

pages = {
    "Balance Sheet": 117,
    "Income Statement": 119,
    "Cash Flow": 123
}

for statement, page in pages.items():

    print("\n" + "=" * 70)
    print(statement)

    tables = extract_tables(PDF, page)

    print(f"Tables Found: {len(tables)}")

    for i, table in enumerate(tables, start=1):
        print(f"\nTable {i}")
        print(table.head(15))
        print(f"\nRows: {len(table)}")
        print(f"Columns: {len(table.columns)}")