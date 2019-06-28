import db_conn
import queries
from donut_chart import DonutChart
from bar_chart import BarChart
import numpy as np


class Ops_Visual:
    def __init__(self, date_range):
        self.query_range = date_range
    
    def build_trailer_visual1(self):        
        trailer_dataset1 = db_conn.build_trailer_dataset1(self.query_range)
        title = 'Trailer Utilization Summary'
        labels = trailer_dataset1.index.tolist()
        values = trailer_dataset1.values.tolist()
        d_type = 'Days'
        tr_donut = DonutChart(title, labels, values, d_type)
        tr_donut.build()
        
    def build_trailer_visual2(self):
        trailer_dataset2 = db_conn.build_trailer_dataset2(self.query_range)
        for k, data_group in trailer_dataset2.groupby(np.arange(len(trailer_dataset2))//5):
            title = 'Utlization by Trailer Nunmber'
            emp_barchart = BarChart(title, data_group, 'Days', 'Trailer Number')
            emp_barchart.build_mult()

    def build_manpower_visual1(self):
        manpower_dataset1 = db_conn.build_manpower_dataset1(self.query_range)
        title = 'Manpower Utilization Summary'
        labels = manpower_dataset1.index.tolist()
        values = manpower_dataset1.values.tolist()
        d_type = 'Days'
        mpwr_donut = DonutChart(title, labels, values, d_type)
        mpwr_donut.build()
    
    def build_manpower_visual2(self):
        manpower_dataset2 = db_conn.build_manpower_dataset2(self.query_range)
        for k, data_group in manpower_dataset2.groupby(np.arange(len(manpower_dataset2))//5):
            title = 'Utlization by Field Hand'
            emp_barchart = BarChart(title, data_group, 'Days', 'Field Employee')
            emp_barchart.build_mult()

    def build_ops_incidents_visual1(self):
        ops_incidents_dataset1 = db_conn.build_ops_incidents_dataset1(self.query_range)
        title = 'Operations Incidents By Severity'
        ops_barchart1 = BarChart(title, ops_incidents_dataset1, 'Incident Type', 'Count')
        ops_barchart1.build_hz()
        
    def build_ops_incidents_visual2(self):
        ops_incidents_dataset2 = db_conn.build_ops_incidents_dataset2(self.query_range)
        title = 'Ops Incidents Month Over Month'
        ops_barchart2 = BarChart(title, ops_incidents_dataset2, 'Number Of Incidents', 'Month')
        ops_barchart2.build_single()
        
    def build_ops_incidents_visual3(self):
        ops_incidents_dataset3 = db_conn.build_ops_incidents_dataset3(self.query_range)
        title = 'Operations Incidents By Incident Type'
        ops_barchart3 = BarChart(title, ops_incidents_dataset3, 'Incident Type', 'Number Of Incidents')
        ops_barchart3.build_hz()

    def build_header_visual(self):
        header_dataset = db_conn.build_header_dataset(self.query_range)
            
    def build_num_trips_visual(self):
        num_trips_dataset = db_conn.build_num_trips_dataset(self.query_range)
        title = 'Frac Jobs By Number Of Kobold Tool Trips'
        num_trips_barchart = BarChart(title, num_trips_dataset, 'Kobold Tool Trip Count', 'Job Count')
        num_trips_barchart.build_hz()
        
    def build_stages_breakdown_visual(self):
        stages_brkdwn_dataset = db_conn.build_stages_brkdwn_dataset(self.query_range)
        title = 'Frac Metrics By Stage'
        stages_brkdwn_barchart = BarChart(title, stages_brkdwn_dataset, None, 'Stage Count')
        stages_brkdwn_barchart.build_hz()
        
    def build_job_depth_visual(self):
        job_depth_dataset = db_conn.build_job_depth_dataset(self.query_range)
        title = 'Frac Jobs By Well Depth'
        labels = job_depth_dataset.index.tolist()
        values = job_depth_dataset.values.tolist()
        d_type = 'Jobs'
        jd_donut = DonutChart(title, labels, values, d_type)
        jd_donut.build()
        
    def build_job_formation_visual(self):
        job_formation_dataset = db_conn.build_job_formation_dataset(self.query_range)        
        title = 'Frac Jobs By Formation'
        labels = job_formation_dataset.index.tolist()
        values = job_formation_dataset['Job Count'].tolist()
        d_type = 'Jobs'
        jf_donut = DonutChart(title, labels, values, d_type)
        jf_donut.build()
        
    def build_stage_time_visual(self):
        stage_time_dataset = db_conn.build_stage_time_dataset(self.query_range)
        title = 'Avg Frac, Interval Time By Client'
        stage_time_barchart = BarChart(title, stage_time_dataset, 'Time (min)', 'Client')
        stage_time_barchart.build_single()
        

    
