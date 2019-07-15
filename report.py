from ops_visual import Ops_Visual
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import argparse

def get_data_range():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-st', '--start', type=str, required=True, 
    help='enter query start date in YYYY-MM-DD')

    parser.add_argument('-end', '--end', type=str, required=True, 
    help='enter query end date in YYYY-MM-DD')

    date_range = vars(parser.parse_args())

    return(date_range)

def build_trailer_report():
    tr_plt1 = ops_visual.build_trailer_visual1()
    tr_plt1.show()
    tr_plt2 = ops_visual.build_trailer_visual2()
    tr_plt2.show()

def build_manpower_report():
    mpwr_plt1 = ops_visual.build_manpower_visual1() 
    mpwr_plt1.show()
    mpwr_plt2 = ops_visual.build_manpower_visual2() 
    mpwr_plt2.show()

def build_ops_incidents_report():
    ops_plt1 = ops_visual.build_ops_incidents_visual1() 
    ops_plt1.show()
    ops_plt2 = ops_visual.build_ops_incidents_visual2() 
    ops_plt2.show()
    ops_plt3 = ops_visual.build_ops_incidents_visual3()
    ops_plt3.show()
    
def build_frac_jobs_report():
    # ops_visual.build_header_visual()
    frac_plt1 = ops_visual.build_num_trips_visual() 
    frac_plt1.show()
    frac_plt2 = ops_visual.build_stages_breakdown_visual()
    frac_plt2.show()
    frac_plt3 = ops_visual.build_job_depth_visual() 
    frac_plt3.show()
    frac_plt4 = ops_visual.build_job_formation_visual()
    frac_plt4.show()
    frac_plt5 = ops_visual.build_stage_time_visual()
    frac_plt5.show()

if __name__ == "__main__":
    
    date_range = get_data_range()
    ops_visual = Ops_Visual(date_range)
    build_trailer_report()
    build_manpower_report()
    build_ops_incidents_report()
    build_frac_jobs_report()
    
    
    
    