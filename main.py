import PyPDF2

class resume_helper:

    def __init__(self):
        self.path = "test_path"

    def read_pdf(self):
        with open(self.path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

            total_pages = len(reader.pages)
            print(f"Total pages: {total_pages}")
            print("PDF successfully parsed")

        return reader