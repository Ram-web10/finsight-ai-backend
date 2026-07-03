from services.page_inspector import inspect_page

PDF = "uploads/annual report 2024-25 Infosys.pdf"

pages = [117,119,123,150,163]

for page in pages:

    result = inspect_page(PDF, page)

    print("\n" + "="*70)

    print(f"PAGE {result['page']}")

    print(f"Words   : {result['words']}")

    print(f"Numbers : {result['numbers']}")

    print("\nPreview:\n")

    print(result["preview"])

    print("\n")
