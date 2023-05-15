from flask import request,redirect
from database_conn import db_conn
from mID_retrievals import retrieve_MID_e
conn=db_conn()

def delete_milk_production_entry(production_date, animal_id):
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Milk_Production WHERE Production_Date = ? AND A_ID = ? AND M_ID=?", (production_date, animal_id,mID))
        conn.commit()
        return redirect('/milk_production_view_e')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting milk production entry: {str(e)}"



def delete_animal_entry(aID, mID):
    mID=retrieve_MID_e()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Animals WHERE A_ID = ? AND M_ID=?", (aID,mID))
        conn.commit()
        return redirect('/view_animals')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting milk production entry: {str(e)}"

def delete_animal_health_entry(a_id, m_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Animal_Health_Info WHERE A_ID = ? AND M_ID=?", (a_id, m_id))
        conn.commit()
        return redirect('/view_animals_health')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting animal health entry: {str(e)}"
    

def delete_sales_entry(sale_id, m_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Sales WHERE Sale_ID = ? AND M_ID = ?", (sale_id, m_id))
        conn.commit()
        return redirect('/view_sales_e')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting sales entry: {str(e)}"
    

def delete_product_entry(p_id, m_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE P_ID = ? AND M_ID = ?", (p_id, m_id))
        conn.commit()
        return redirect('/view_products_e')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting product entry: {str(e)}"

def delete_employee(employee_id, manager_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Employees WHERE E_ID = ? AND M_ID = ?", (employee_id, manager_id))
        conn.commit()
        return redirect('/view_employees')
    except Exception as e:
        # Handle any errors that occur during the deletion process
        return f"Error deleting employee: {str(e)}"
