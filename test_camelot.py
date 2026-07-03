import camelot

pdf = "uploads/annual report 2024-25 Infosys.pdf"

for flavor in ["lattice", "stream"]:
    print(f"\nTesting {flavor.upper()} mode")

    try:
        tables = camelot.read_pdf(
            pdf,
            pages="117",
            flavor=flavor
        )

        print(f"Tables Found: {len(tables)}")

        if len(tables):
            print(tables[0].df.head())

    except Exception as e:
        print(e)