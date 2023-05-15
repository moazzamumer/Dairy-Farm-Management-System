import pyodbc


def db_conn():
    conx_string = " DRIVER={SQL SERVER}; server=MOAZZAM-NOTEBOO\SQLEXPRESS; database=DFMS; trusted_connection=YES;"
    conn = pyodbc.connect(conx_string)
    return conn
