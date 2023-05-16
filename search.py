from flask import redirect,request,render_template
from database_conn import db_conn
from mID_retrievals import *
conn=db_conn()


def search_milk_data_m():
    animal_id = request.form.get('animal_id')
    mID=retrieve_MID_m()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Production_Date, A_ID, Quantity, Quality FROM Milk_Production WHERE M_ID = ? AND A_ID=?", (mID,animal_id,))
        milk_data = cursor.fetchall()
        return render_template('/m_pages/milk_production_view_m.html', milk_data=milk_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    

def search_milk_data_e():
    animal_id = request.form.get('animal_id')
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Milk_Production WHERE M_ID = ? AND A_ID=?", (mID,animal_id,))
        milk_data = cursor.fetchall()
        return render_template('/e_pages/milk_production_view_e.html', milk_data=milk_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"

def search_revenue_record_m():
    date=request.form.get('date')
    mID=retrieve_MID_m()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Date, Total_Revenue, Total_Expense FROM Daily_Income WHERE M_ID = ? AND Date=?", (mID,date))
        income_data = cursor.fetchall()
        return render_template('/m_pages/income_view_m.html', income_data=income_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    
def search_sales_m():
    sID=request.form.get('sID')
    mID=retrieve_MID_m()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Sale_ID, Sale_Date, C_Name, P_ID, Total_Cost FROM Sales WHERE M_ID = ? AND Sale_ID=?", (mID,sID))
        sales_data = cursor.fetchall()
        return render_template('/m_pages/sales_view_m.html', sales_data=sales_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    
def search_employee_m():
    eID=request.form.get('eID')
    mID=retrieve_MID_m()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT E_ID,M_ID, E_Name, Gender, Contact, Salary, Login_username, Login_password FROM Employees WHERE M_ID = ? AND E_ID=?", (mID,eID))
        e_data = cursor.fetchall()
        return render_template('/m_pages/view_employees.html', employees_data=e_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    

def search_animals():
    animal_id = request.form.get('animal_id')
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Animals WHERE M_ID = ? AND A_ID=?", (mID,animal_id,))
        a_data = cursor.fetchall()
        return render_template('/e_pages/view_animals.html', animals_data=a_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    

def search_health():
    animal_id = request.form.get('animal_id')
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Animal_Health_Info WHERE M_ID = ? AND A_ID=?", (mID,animal_id,))
        a_data = cursor.fetchall()
        return render_template('/e_pages/view_health.html', health_data=a_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    
def search_sales_e():
    sID=request.form.get('sid')
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sales WHERE M_ID = ? AND Sale_ID=?", (mID,sID))
        sales_data = cursor.fetchall()
        return render_template('/e_pages/view_sales_e.html', sales_data=sales_data)
    except Exception as e:
        return f"Error retrieving data: {str(e)}"
    