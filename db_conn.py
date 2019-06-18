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
            
if __name__ == "__main__":
    trailer_dataset1 = build_dataset(queries.TRAILERS_QUERY1)
    trailer_dataset2 = build_dataset(queries.TRAILERS_QUERY2)
    manpower_dataset1 = build_dataset(queries.MANPOWER_QUERY1)
    manpower_dataset2 = build_dataset(queries.MANPOWER_QUERY2)
    ops_incidents_dataset1 = build_dataset(queries.OPS_INCIDENTS_QUERY1)
    ops_incidents_dataset2 = build_dataset(queries.OPS_INCIDENTS_QUERY2)
    ops_incidents_dataset3 = build_dataset(queries.OPS_INCIDENTS_QUERY3)



    
   

