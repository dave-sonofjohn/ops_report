import db_conn
import argparse
import queries
import matplotlib.pyplot as plt
import numpy as np

class DonutChart:
    def __init__(self, title, labels, values, d_type):
        self.title = title
        self.labels = labels
        self.values = values
        self.d_type = d_type

    def build(self):
        formatted_labels = ['{0} - {1} {2}'.format(i, j, self.d_type) for i,j in zip(self.labels, self.values)]  

        patches, texts = plt.pie(self.values, startangle=90)
        plt.legend(patches, formatted_labels, loc="best")
        plt.title('{}'.format(self.title))
        
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
          
        plt.tight_layout()
        plt.show()

class BarChart:
    def __init__():
        pass

    def build(self):
        pass

class Report:
    def __init__(self, args):
        self.query_range = args
    
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
        print(trailer_dataset2)
        print('\n')

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
        print(manpower_dataset2)
        print('\n')

    def build_ops_incidents_visual1(self):
        ops_incidents_dataset1 = db_conn.build_ops_incidents_dataset1(self.query_range)
        print(ops_incidents_dataset1)
        print('\n')

    def build_ops_incidents_visual2(self):
        ops_incidents_dataset2 = db_conn.build_ops_incidents_dataset2(self.query_range)
        print(ops_incidents_dataset2)
        print('\n')

    def build_ops_incidents_visual3(self):
        ops_incidents_dataset3 = db_conn.build_ops_incidents_dataset3(self.query_range)
        print(ops_incidents_dataset3)
        print('\n')

    def build_header_visual(self):
        header_dataset = db_conn.build_header_dataset(self.query_range)
        print(header_dataset)
        print('\n')

    def build_num_trips_visual(self):
        num_trips_dataset = db_conn.build_num_trips_dataset(self.query_range)
        print(num_trips_dataset)
        print('\n')
        
    def build_stages_breakdown_visual(self):
        stages_brkdwn_dataset = db_conn.build_stages_brkdwn_dataset(self.query_range)
        print(stages_brkdwn_dataset)
        print('\n')

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
        build_stage_time_dataset = db_conn.build_stage_time_dataset(self.query_range)
        print('\n')


def get_data_range():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-st', '--start', type=str, required=True, 
    help='enter query start date in YYYY-MM-DD')

    parser.add_argument('-end', '--end', type=str, required=True, 
    help='enter query end date in YYYY-MM-DD')

    args = vars(parser.parse_args())

    return(args)

if __name__ == "__main__":
    args = get_data_range()
    report = Report(args)
    report.build_trailer_visual1()
    # report.build_trailer_visual2()
    report.build_manpower_visual1()
    # report.build_manpower_visual2()
    # report.build_ops_incidents_visual1()
    # report.build_ops_incidents_visual2()
    # report.build_ops_incidents_visual3()
    # report.build_header_visual()
    # report.build_num_trips_visual()
    # report.build_stages_breakdown_visual()
    report.build_job_depth_visual()
    report.build_job_formation_visual()
    report.build_stage_time_visual()
    
