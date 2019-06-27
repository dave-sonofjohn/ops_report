import db_conn
import argparse
import queries
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from textwrap  import wrap

class DonutChart:
    def __init__(self, title, labels, values, d_type):
        self.title = title
        self.labels = labels
        self.values = values
        self.d_type = d_type

    def build(self):
        patches, texts = plt.pie(self.values, startangle=90)

        pct_list = []
        for i in range(len(self.values)):
            pct_list.append(round((self.values[i]/sum(self.values))*100, 2))

        formatted_labels = ['{0} - {1} {2} ({3} %)'.format(i, j, self.d_type, k) for i,j, k in zip(self.labels, self.values, pct_list)]  
        plt.legend(patches, formatted_labels, loc="lower right")
        plt.title('{}'.format(self.title))
        
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
          
        plt.tight_layout()
        plt.show()

class BarChart:
    def __init__(self, title, ds, y_axis=None, x_axis=None):
        self.title = title
        self.ds = ds
        self.x_axis = x_axis
        self.y_axis = y_axis

    def build_mult(self):
        c_labels = self.ds.columns.values 
        colors = ['royalblue', 'red', 'orange', 'green', 'purple', 'deepskyblue', 'deeppink', 'limegreen', 'firebrick']
        x_labels = self.ds.index
        sizes = self.ds.head(5).values

        fig, axes = plt.subplots(ncols=sizes.shape[0], figsize=(10, 5), sharey=True)
        plt.gcf().subplots_adjust(bottom=0.2)
        for ax, height, title in zip(axes, sizes, x_labels):
            ax.set_title(title)

            left = np.arange(len(height)) + 1
            ax.bar(left, height, color=colors)
            ax.set_ylabel(self.y_axis, fontsize=8)
            ax.set_xticks(left)
            ax.set_xticklabels(c_labels, rotation=45, rotation_mode='anchor', ha='right')

        plt.show()

    def build_hz(self):
        plt.rcdefaults()
        fig, ax = plt.subplots(figsize=(8,4))
        plt.gcf().subplots_adjust(left=0.25, right=0.9, top=0.9)

        labels = list(self.ds.index)
        y_pos = np.arange(len(labels))
        values = list(self.ds.values)
                
        ax.barh(y_pos, values, align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        
        ax.invert_yaxis()
        ax.set_ylabel(self.y_axis)
        ax.set_xlabel(self.x_axis)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.set_title(self.title)
        ax.set_xlim(0, 1.25*(max(self.ds.values)))

        for i in ax.patches:
            ax.text(i.get_width()+.3, i.get_y()+.43, str(i.get_width()))

        plt.show()

    def build_single(self):

        ax = self.ds[list(self.ds.columns.values)].plot(kind='bar', width=0.5, align='center', title=self.title, figsize=(12, 9), legend=True, fontsize=8)
       
        ax.set_xlabel(self.x_axis, fontsize=8)
        
        ax.set_ylabel(self.y_axis, fontsize=8)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.gcf().subplots_adjust(left=0.1, right=0.75, top=0.9)
        plt.legend(loc=(1.04,0))

        for i in ax.patches:
            ax.text(i.get_x()+0.5*(i.get_width()), i.get_height()+.01*(i.get_height()), str(i.get_height()), fontsize=10, color='dimgrey')

        plt.show()
        
            

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
        ops_barchart1 = BarChart(title, ops_incidents_dataset1, 'Count', 'Incident Type')
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
    # report.build_trailer_visual1() 
    # report.build_trailer_visual2() 
    # report.build_manpower_visual1() 
    # report.build_manpower_visual2() 
    report.build_ops_incidents_visual1() 
    # report.build_ops_incidents_visual2() 
    # report.build_ops_incidents_visual3()
    # report.build_header_visual()
    # report.build_num_trips_visual() 
    report.build_stages_breakdown_visual()
    # report.build_job_depth_visual() 
    # report.build_job_formation_visual()
    # report.build_stage_time_visual()
    
