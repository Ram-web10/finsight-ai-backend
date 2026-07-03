import pdfplumber


def extract_text(pdf_path: str):

    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                full_text += page_text + "\n"

    return full_text