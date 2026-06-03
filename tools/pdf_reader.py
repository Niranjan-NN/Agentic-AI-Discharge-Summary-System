import fitz
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class PDFReaderTool:

    @staticmethod
    def extract(uploaded_file):

        docs = []

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        for page_num in range(len(pdf)):

            page = pdf[page_num]

            text = page.get_text()

            # OCR fallback
            if len(text.strip()) < 20:

                pix = page.get_pixmap(
                    matrix=fitz.Matrix(3, 3)
                )

                img_bytes = pix.tobytes("png")

                image = Image.open(
                    io.BytesIO(img_bytes)
                )

                image = image.convert("RGB")

                text = pytesseract.image_to_string(
                    image,
                    lang="eng",
                    config="--psm 6"
                )

            docs.append({
                "page": page_num + 1,
                "text": text
            })

        return docs