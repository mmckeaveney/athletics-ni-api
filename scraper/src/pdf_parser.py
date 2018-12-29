import tabula
import numpy as np
import pandas as pd
import logging

URL = 'https://athleticsni.org/download/files/'
PDF_TABLE_COORDS = [153.15, 5.1, 775.87, 589.48]
PDF_COLUMN_COORDS = [42.74, 174.78, 259.62, 323.81, 529.21, 591.15]

def parse_pdf_to_df(pdf_file_name = 'XCandRRFixtures-Updated-131218.pdf'):
    logging.info('Fetching PDF..')
    data_frame = tabula.read_pdf(
        URL + pdf_file_name, 
        pages='all', 
        guess=False,
        area=PDF_TABLE_COORDS, 
        columns=PDF_COLUMN_COORDS
    )
    logging.info(pdf_file_name + ' parsed successfully.')
    return data_frame

def combine_relevant_rows(df):
    logging.info('Combining date rows..')
    for index, row in df.iterrows():
        val = df.at[index, 'Date']
        if str(val).isnumeric():
            row_before = df.at[index - 1, 'Date']
            df.at[index - 1, 'Date'] = row_before + ' ' + df.at[index, 'Date']
            df.at[index, 'Date'] = None

    logging.info('Combining other race data..')
    for index, row in df.iterrows():
        # if the row has a NaN date
        val = df.at[index, 'Date']
        if pd.isnull(val) and index is not 0:
            df.at[index - 1, 'Event'] = str(df.at[index - 1, 'Event']) + ' ' + str(df.at[index, 'Event'])
            df.at[index - 1, 'Venue'] = str(df.at[index - 1, 'Venue']) + ' ' + str(df.at[index, 'Venue'])
            df.at[index - 1, 'Time'] = str(df.at[index - 1, 'Time']) + ' ' + str(df.at[index, 'Time'])
            df.at[index - 1, 'Contact'] = str(df.at[index - 1, 'Contact']) + ' ' + str(df.at[index, 'Contact'])

    df = df.dropna(subset=['Date'])
    return df
