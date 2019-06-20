import os
import pyodbc
import queries
import numpy as np
import pandas as pd

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
        
    def execute_query_1D(self):
        self.cursor.execute(self.query)
        names = [ x[0] for x in self.cursor.description ]
        rows = self.cursor.fetchall()
        ds = pd.Series(rows[0], index=names)
        return(ds)

    def execute_query_2D(self):
        self.cursor.execute(self.query)
        rows = np.array(self.cursor.fetchall())
        df = pd.DataFrame(data=rows)
        df.columns = [ x[0] for x in self.cursor.description ]
        df = df.set_index(['index'])
        return(df)


def build_dataset_1D(query):
    db = DBConn(query)
    dataseries = db.execute_query_1D()
    return(dataseries)

def build_dataset_2D(query):
    db = DBConn(query)
    df = db.execute_query_2D()
    return(df)
            
def build_trailer_dataset1(query_range):
    trailer_dataset1 = build_dataset_1D(queries.build_trailer_query1(query_range))    
    return(trailer_dataset1)

def build_trailer_dataset2(query_range):
    trailer_dataset2 = build_dataset_2D(queries.build_trailer_query2(query_range))    
    return(trailer_dataset2)

def build_manpower_dataset1(query_range):
    manpower_dataset1 = build_dataset_1D(queries.build_manpower_query1(query_range))    
    return(manpower_dataset1)

def build_manpower_dataset2(query_range):
    manpower_dataset2 = build_dataset_2D(queries.build_manpower_query2(query_range))    
    return(manpower_dataset2)

def build_ops_incidents_dataset1(query_range):
    ops_incidents_dataset1 = build_dataset(queries.build_ops_incidents_query1(query_range))
    return(ops_incidents_dataset1)

def build_ops_incidents_dataset2(query_range):
    ops_incidents_dataset2 = build_dataset(queries.build_ops_incidents_query2(query_range))
    return(ops_incidents_dataset2)

def build_ops_incidents_dataset3(query_range):
    ops_incidents_dataset3 = build_dataset(queries.build_ops_incidents_query3(query_range))
    return(ops_incidents_dataset3)

def build_header_dataset(query_range):
    header_dataset = build_dataset(queries.build_header_query(query_range))
    return(header_dataset)

def build_num_trips_dataset(query_range):
    num_trips_dataset = build_dataset(queries.build_num_trips_query(query_range))
    
    return(num_trips_dataset)

def build_stages_brkdwn_dataset(query_range):
    stages_brkdwn_dataset = build_dataset(queries.build_stages_brkdwn_query(query_range))    
    return(stages_brkdwn_dataset)

def build_job_depth_dataset(query_range):
    job_depth_dataset = build_dataset(queries.build_job_depth_query(query_range))
    return(job_depth_dataset)

def build_job_formation_dataset(query_range):
    job_formation_dataset = build_dataset(queries.build_job_formation_query(query_range))
    return(job_formation_dataset)

def build_stage_time_dataset(query_range):
    stage_time_dataset = build_dataset(queries.build_stage_time_query(query_range))
    return(stage_time_dataset)





    
   

