import tabula
import logging

logging.basicConfig(level=logging.INFO)

URL = "https://athleticsni.org/download/files/"
PDF_TABLE_COORDS = [153.15, 5.1, 775.87, 589.48]
PDF_COLUMN_COORDS = [42.74, 174.78, 259.62, 323.81, 529.21, 591.15]

def parse_pdf_to_csv(pdf_file_name):
    logging.info("Fetching PDF..")
    data_frame = tabula.read_pdf(
        URL + pdf_file_name, 
        pages="all", 
        guess=False,
        area=PDF_TABLE_COORDS, 
        columns=PDF_COLUMN_COORDS
    )
    print(data_frame.to_string())
    logging.info(pdf_file_name + " parsed successfully.")
    
parse_pdf_to_csv("XCandRRFixtures-Updated-131218.pdf")
