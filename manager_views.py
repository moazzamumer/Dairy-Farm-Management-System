from mID_retrievals import retrieve_MID_m
from flask import render_template
from database_conn import db_conn
conn=db_conn()


def milk_production_view_m():
    mID=retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Milk_Production where M_ID=?",(mID))
    milkproduction_data = cursor.fetchall()
    return render_template('/m_pages/milk_production_view_m.html', milk_data=milkproduction_data)

def income_view_m():
    mID=retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Daily_Income where M_ID=?",(mID))
    income_data = cursor.fetchall()
    return render_template('/m_pages/income_view_m.html', income_data=income_data)

def sales_view_m():
    mID=retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sales where M_ID=?",(mID))
    sales_data = cursor.fetchall()
    return render_template('/m_pages/sales_view_m.html', sales_data=sales_data)

def view_employees():
    mID=retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees where M_ID=?",(mID))
    employees_data = cursor.fetchall()
    return render_template('/m_pages/view_employees.html', employees_data=employees_data)
