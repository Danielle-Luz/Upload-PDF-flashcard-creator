import PyPDF2


class TextFileReader:
    def __init__(self, file_path) -> None:
        self.file = open(file_path, "rb")

    def get_pdf_content_as_text(self):
        pdf_read = PyPDF2.PdfReader(self.file)
        pdf_content = ""

        for page in pdf_read.pages:
            pdf_content += page.extract_text()

        return pdf_content
