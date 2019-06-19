import os
import pyodbc
import queries
import numpy as np

class DBConn:
    def __init__(self, query):
        self.query = query
        self.server = os.getenv('FD_HOST')
        self.db = os.getenv('FD_NAME')
        self.username = os.getenv('FD_USER')
        self.pswd = os.getenv('FD_PASS')
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
            self.server + ';DATABASE=' + self.db +
            ';UID=' + self.username + ';PWD=' + self.pswd)
        self.cursor = self.cnxn.cursor()
        
    def execute_query(self):
        self.cursor.execute(self.query)
        return(self.cursor.fetchall())

def build_dataset(query):
    db = DBConn(query)
    dataset = np.array(db.execute_query())
    return(dataset)
            
def build_trailer_dataset1(query_range):
    trailer_dataset1 = build_dataset(queries.build_trailer_query1(query_range))
    print(trailer_dataset1)
    return(trailer_dataset1)

def build_trailer_dataset2(query_range):
    trailer_dataset2 = build_dataset(queries.build_trailer_query2(query_range))
    print(trailer_dataset2)
    return(trailer_dataset2)

def build_manpower_dataset1(query_range):
    manpower_dataset1 = build_dataset(queries.build_manpower_query1(query_range))
    print(manpower_dataset1)
    return(manpower_dataset1)

def build_manpower_dataset2(query_range):
    manpower_dataset2 = build_dataset(queries.build_manpower_query2(query_range))
    print(manpower_dataset2)
    return(manpower_dataset2)

def build_ops_incidents_dataset1(query_range):
    ops_incidents_dataset1 = build_dataset(queries.build_ops_incidents_query1(query_range))
    print(ops_incidents_dataset1)
    return(ops_incidents_dataset1)

def build_ops_incidents_dataset2(query_range):
    ops_incidents_dataset2 = build_dataset(queries.build_ops_incidents_query2(query_range))
    print(ops_incidents_dataset2)
    return(ops_incidents_dataset2)

def build_ops_incidents_dataset3(query_range):
    ops_incidents_dataset3 = build_dataset(queries.build_ops_incidents_query3(query_range))
    print(ops_incidents_dataset3)
    return(ops_incidents_dataset3)

def build_header_dataset(query_range):
    header_dataset = build_dataset(queries.build_header_query(query_range))
    print(header_dataset)
    return(header_dataset)

def build_num_trips_dataset(query_range):
    num_trips_dataset = build_dataset(queries.build_num_trips_query(query_range))
    print(num_trips_dataset)
    return(num_trips_dataset)

def build_stages_brkdwn_dataset(query_range):
    stages_brkdwn_dataset = build_dataset(queries.build_stages_brkdwn_query(query_range))
    print(stages_brkdwn_dataset)
    return(stages_brkdwn_dataset)

def build_job_depth_dataset(query_range):
    job_depth_dataset = build_dataset(queries.build_job_depth_query(query_range))
    print(job_depth_dataset)
    return(job_depth_dataset)

def build_job_formation_dataset(query_range):
    job_formation_dataset = build_dataset(queries.build_job_formation_query(query_range))
    print(job_formation_dataset)
    return(job_formation_dataset)

def build_stage_time_dataset(query_range):
    stage_time_dataset = build_dataset(queries.build_stage_time_query(query_range))
    print(stage_time_dataset)
    return(stage_time_dataset)



    
   

