import os
import pyodbc
import queries

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
    trailer_data = db.execute_query()
    return(trailer_data)
            
def build_trailer_dataset1():
    trailer_dataset1 = build_dataset(queries.TRAILERS_QUERY1)
    return(trailer_dataset1)

def build_trailer_dataset2():
    trailer_dataset2 = build_dataset(queries.TRAILERS_QUERY2)
    return(trailer_dataset2)

def build_manpower_dataset1():
    manpower_dataset1 = build_dataset(queries.MANPOWER_QUERY1)
    return(manpower_dataset1)

def build_manpower_dataset2():
    manpower_dataset2 = build_dataset(queries.MANPOWER_QUERY2)
    return(manpower_dataset2)

def build_ops_incidents_dataset1():
    ops_incidents_dataset1 = build_dataset(queries.OPS_INCIDENTS_QUERY1)
    return(ops_incidents_dataset1)

def build_ops_incidents_dataset2():
    ops_incidents_dataset2 = build_dataset(queries.OPS_INCIDENTS_QUERY2)
    return(ops_incidents_dataset2)

def build_ops_incidents_dataset3():
    ops_incidents_dataset3 = build_dataset(queries.OPS_INCIDENTS_QUERY3)
    return(ops_incidents_dataset3)

def build_header_dataset():
    header_dataset = build_dataset(queries.HEADER_QUERY)
    return(header_dataset)

def build_num_trips_dataset():
    num_trips_dataset = build_dataset(queries.NUM_TRIPS_QUERY)
    return(num_trips_dataset)

def build_stages_brkdwn_dataset():
    stages_brkdwn_dataset = build_dataset(queries.STAGES_BRKDWN_QUERY)
    return(stages_brkdwn_dataset)

def build_job_depth_dataset():
    job_depth_dataset = build_dataset(queries.JOB_DEPTH_QUERY)
    return(job_depth_dataset)

def build_job_formation_dataset():
    job_formation_dataset = build_dataset(queries.JOB_FORMATION_QUERY)
    return(job_formation_dataset)

def build_stage_time_dataset():
    stage_time_dataset = build_dataset(queries.STAGE_TIME_QUERY)
    return(stage_time_dataset)



    
   

