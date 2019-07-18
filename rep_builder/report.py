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
    def get_title(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-ti', '--title', type=str, required=True, 
        help='Enter The Header Title.') 
        args = vars(parser.parse_args())
        self.title = args['title']

        return(self.title)

    def header(self):
        now = datetime.datetime.now()
        # Logo
        self.image('./pics/kob_logo.png', 10, 8, 33)
        # Title
        self.set_font('Arial', 'B', 10)
        self.cell(80)
        self.cell(30, 10, '{}\nService Quality Report'.format(self.title), 0, 0, 'C')
        # Date
        self.set_font('Arial', '', 8)
        self.cell(60)
        self.cell(50, 10, str(now)[:10])
        # Line break
        self.ln(17)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def build_header_data(self):
        header_file = open('../jpg_builder/media/header/header_data.pkl', 'rb')
        header_data = pickle.load(header_file)
        
        self.line(20,25,210-20,25)

        self.cell(40)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[0], header_data['Total Frac Jobs']))   

        self.cell(50)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[2], header_data['Time In Hole (hrs)']))
        
        self.ln(5)
        self.cell(40)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[1], header_data['Total Kobold Tool Runs']))

        self.cell(50)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[3], header_data['NPT (hrs)']))
        
        self.ln(5)
        self.cell(40)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[5], header_data['Total Tons Fracked']))

        self.cell(50)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[4], header_data['In Hole Distance Travelled (m)']))
        
        self.ln(5)
        self.cell(40)
        self.cell(10,10,'{0} - {1}'.format(header_data.index[6], header_data['Total Stages Fracked']))
        
        self.line(20,52,210-20,52)

    def build_frac_section(self):
        self.image('../jpg_builder/media/frac/num_trips.jpg', -10, 60, 100, 50)
        self.image('../jpg_builder/media/frac/job_forms.jpg', 100, 60, 90, 60)
        self.image('../jpg_builder/media/frac/job_depths.jpg', 10, 125, 100, 50)
        self.image('../jpg_builder/media/frac/stg_bd.jpg', 100, 125, 100, 50)
        self.image('../jpg_builder/media/frac/stg_times.jpg', 40, 185, 150, 90)


if __name__ == '__main__':

    pdf = PDF()
    pdf.get_title()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.build_header_data()
    pdf.build_frac_section()
    pdf.add_page()
    # pdf.set_font('Times', '', 12)
    # for i in range(1, 41):
    #     pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)
    pdf.output('tuto2.pdf', 'F')




