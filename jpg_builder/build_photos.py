from ops_visual import Ops_Visual
from fpdf import FPDF
import matplotlib.pyplot as fig
import argparse

def get_data_range():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-st', '--start', type=str, required=True, 
    help='enter query start date in YYYY-MM-DD')

    parser.add_argument('-end', '--end', type=str, required=True, 
    help='enter query end date in YYYY-MM-DD')

    date_range = vars(parser.parse_args())

    return(date_range)

def compile_jpgs():
    ops_visual.build_trailer_visual1()
    ops_visual.build_trailer_visual2()
    ops_visual.build_manpower_visual1()         
    ops_visual.build_manpower_visual2()        
    ops_visual.build_ops_incidents_visual1()         
    ops_visual.build_ops_incidents_visual2()        
    ops_visual.build_ops_incidents_visual3() 
    ops_visual.build_header_data()       
    ops_visual.build_num_trips_visual()        
    ops_visual.build_stages_breakdown_visual()        
    ops_visual.build_job_depth_visual()         
    ops_visual.build_job_formation_visual()        
    ops_visual.build_stage_time_visual()

    
if __name__ == "__main__":
    
    date_range = get_data_range()
    ops_visual = Ops_Visual(date_range)
    compile_jpgs()
    


    
    
    
    
    
    