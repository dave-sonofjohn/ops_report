import db_conn
import argparse

class Report:
    def __init__(self, args):
        self.query_range = args
        # self.start_date = args['start']
        # self.end_date = args['end']
    
    def build_trailer_visual1(self):
        trailer_dataset1 = db_conn.build_trailer_dataset1(self.query_range)
        trailer_dataset2 = db_conn.build_trailer_dataset2(self.query_range)
        manpower_dataset1 = db_conn.build_manpower_dataset1(self.query_range)
        manpower_dataset2 = db_conn.build_manpower_dataset2(self.query_range)
        ops_incidents_dataset1 = db_conn.build_ops_incidents_dataset1(self.query_range)
        ops_incidents_dataset2 = db_conn.build_ops_incidents_dataset2(self.query_range)
        ops_incidents_dataset3 = db_conn.build_ops_incidents_dataset3(self.query_range)
        header_dataset = db_conn.build_header_dataset(self.query_range)
        num_trips_dataset = db_conn.build_num_trips_dataset(self.query_range)
        stages_brkdwn_dataset = db_conn.build_stages_brkdwn_dataset(self.query_range)
        job_depth_dataset = db_conn.build_job_depth_dataset(self.query_range)
        job_formation_dataset = db_conn.build_job_formation_dataset(self.query_range)
        build_stage_time_dataset = db_conn.build_stage_time_dataset(self.query_range)
        


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
