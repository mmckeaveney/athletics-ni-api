import pdf_parser
import persistence
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    df = pdf_parser.parse_pdf_to_df()
    df = pdf_parser.combine_relevant_rows(df)
    persistence.persist_races(df.to_dict('records'))

