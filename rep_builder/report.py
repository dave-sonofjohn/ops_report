import pickle
import pandas as pd
from fpdf import FPDF
import datetime
import argparse


def get_title():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-ti', '--title', type=str, required=True, 
    help='Enter The Header Title.')
    
    args = vars(parser.parse_args())
    title = args['title']

    return(title)

class PDF(FPDF):

    def header(self):
        now = datetime.datetime.now()
        # Logo
        self.image('./pics/kob_logo.png', 10, 8, 33)
        
        # Title
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        self.cell(30, 10, 'Service Quality Report', 0, 0, 'C')
        
        # Date
        self.set_font('Arial', '', 10)
        self.cell(60)
        self.cell(50, 10, str(now)[:10])
        
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

# Instantiation of inherited class


if __name__ == '__main__':

    title = get_title()
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 41):
        pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
    pdf.output('tuto2.pdf', 'F')




