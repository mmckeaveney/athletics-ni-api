import tabula
import logging

logging.basicConfig(level=logging.INFO)
URL = "https://athleticsni.org/download/files/"

def parse_pdf_to_csv(pdf_file_name):
    logging.info("Fetching PDF..")
    data_frame = tabula.read_pdf(URL + pdf_file_name)
    print(data_frame.to_string())
    logging.info(pdf_file_name + " parsed successfully.")
    
parse_pdf_to_csv("XCandRRFixtures-Updated-131218.pdf")
