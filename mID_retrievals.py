import pyodbc
from flask import session

conx_string = " DRIVER={SQL SERVER}; server=MOAZZAM-NOTEBOO\SQLEXPRESS; database=DFMS; trusted_connection=YES;"
conn = pyodbc.connect(conx_string)

#function to retrieve M_ID from employee credentials
def retrieve_MID_e():
    cursor = conn.cursor()
    cursor.execute("SELECT M_ID FROM employees WHERE Login_username=? AND Login_password=?", (session['username'], session['password']))
    mID = cursor.fetchone().M_ID
    return mID

#function to retrieve M_ID from manager credentials
def retrieve_MID_m():
    cursor = conn.cursor()
    cursor.execute("SELECT M_ID FROM manager WHERE M_UserName=? AND Password=?", (session['username'], session['password']))
    mID = cursor.fetchone().M_ID
    return mID