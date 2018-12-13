import requests
import logging

logging.basicConfig(level=logging.INFO)

URL = "https://athleticsni.org/download/files/"

def download_pdf(file_name):
    """ Downloads a PDF file from the web """
    with open(file_name, 'wb') as pdf:
        logging.info("Fetching PDF..")
        response = requests.get(URL + file_name)
        pdf.write(response.content)
        logging.info(file_name + " saved successfully.")

    
download_pdf("XCandRRFixtures-Updated-131218.pdf")
