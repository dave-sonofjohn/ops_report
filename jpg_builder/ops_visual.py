import db_conn
import queries
from donut_chart import DonutChart
from bar_chart import BarChart
import numpy as np
import matplotlib.pyplot as plt


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
        plt = tr_donut.build()
        plt.savefig('pics/trailers/tr1.jpg', dpi='figure')
        plt.close()

    def build_trailer_visual2(self):
        trailer_dataset2 = db_conn.build_trailer_dataset2(self.query_range)        
        for k, data_group in trailer_dataset2.groupby(np.arange(len(trailer_dataset2))//5):
            title = 'Utlization by Trailer Nunmber'
            emp_barchart = BarChart(title, data_group, 'Days', 'Trailer Number')
            plt = emp_barchart.build_mult()
            plt.savefig('pics/trailers/tr2_{}.jpg'.format(k), dpi='figure')
            plt.close()

    def build_manpower_visual1(self):
        manpower_dataset1 = db_conn.build_manpower_dataset1(self.query_range)
        title = 'Manpower Utilization Summary'
        labels = manpower_dataset1.index.tolist()
        values = manpower_dataset1.values.tolist()
        d_type = 'Days'
        mpwr_donut = DonutChart(title, labels, values, d_type)
        plt = mpwr_donut.build()
        plt.savefig('pics/manpower/mp1.jpg')
        plt.close()
    
    def build_manpower_visual2(self):
        manpower_dataset2 = db_conn.build_manpower_dataset2(self.query_range)
        for k, data_group in manpower_dataset2.groupby(np.arange(len(manpower_dataset2))//5):
            title = 'Utlization by Field Hand'
            emp_barchart = BarChart(title, data_group, 'Days', 'Field Employee')
            plt = emp_barchart.build_mult()
            plt.savefig('pics/manpower/mp2_{0}.jpg'.format(k))
            plt.close()

    def build_ops_incidents_visual1(self):
        ops_incidents_dataset1 = db_conn.build_ops_incidents_dataset1(self.query_range)
        title = 'Operations Incidents By Severity'
        ops_barchart1 = BarChart(title, ops_incidents_dataset1, 'Incident Type', 'Count')
        plt = ops_barchart1.build_hz()
        plt.savefig('pics/ops_incidents/ops1.jpg')
        plt.close()
        
    def build_ops_incidents_visual2(self):
        ops_incidents_dataset2 = db_conn.build_ops_incidents_dataset2(self.query_range)
        title = 'Ops Incidents Month Over Month'
        ops_barchart2 = BarChart(title, ops_incidents_dataset2, 'Number Of Incidents', 'Month')
        plt = ops_barchart2.build_single()
        plt.savefig('pics/ops_incidents/ops2.jpg')
        plt.close()
        
    def build_ops_incidents_visual3(self):
        ops_incidents_dataset3 = db_conn.build_ops_incidents_dataset3(self.query_range)
        title = 'Operations Incidents By Incident Type'
        ops_barchart3 = BarChart(title, ops_incidents_dataset3, 'Incident Type', 'Number Of Incidents')
        plt = ops_barchart3.build_hz()
        plt.savefig('pics/ops_incidents/ops3.jpg')
        plt.close()

    def build_header_visual(self):
        header_dataset = db_conn.build_header_dataset(self.query_range)
            
    def build_num_trips_visual(self):
        num_trips_dataset = db_conn.build_num_trips_dataset(self.query_range)
        title = 'Frac Jobs By Number Of Kobold Tool Trips'
        num_trips_barchart = BarChart(title, num_trips_dataset, 'Kobold Tool Trip Count', 'Job Count')
        plt = num_trips_barchart.build_hz()
        plt.savefig('pics/frac/num_trips.jpg')
        plt.close()
        
    def build_stages_breakdown_visual(self):
        stages_brkdwn_dataset = db_conn.build_stages_brkdwn_dataset(self.query_range)
        title = 'Frac Metrics By Stage'
        stages_brkdwn_barchart = BarChart(title, stages_brkdwn_dataset, None, 'Stage Count')
        plt = stages_brkdwn_barchart.build_hz()
        plt.savefig('pics/frac/stg_bd.jpg')
        plt.close()
        
    def build_job_depth_visual(self):
        job_depth_dataset = db_conn.build_job_depth_dataset(self.query_range)
        title = 'Frac Jobs By Well Depth'
        labels = job_depth_dataset.index.tolist()
        values = job_depth_dataset.values.tolist()
        d_type = 'Jobs'
        jd_donut = DonutChart(title, labels, values, d_type)
        plt = jd_donut.build()
        plt.savefig('pics/frac/job_depths.jpg')
        plt.close()
        
    def build_job_formation_visual(self):
        job_formation_dataset = db_conn.build_job_formation_dataset(self.query_range)        
        title = 'Frac Jobs By Formation'
        labels = job_formation_dataset.index.tolist()
        values = job_formation_dataset['Job Count'].tolist()
        d_type = 'Jobs'
        jf_donut = DonutChart(title, labels, values, d_type)
        plt = jf_donut.build()
        plt.savefig('pics/frac/job_forms.jpg')
        plt.close()
        
    def build_stage_time_visual(self):
        stage_time_dataset = db_conn.build_stage_time_dataset(self.query_range)
        title = 'Avg Frac, Interval Time By Client'
        stage_time_barchart = BarChart(title, stage_time_dataset, 'Time (min)', 'Client')
        plt = stage_time_barchart.build_single()
        plt.savefig('pics/frac/stg_times.jpg')
        plt.close()