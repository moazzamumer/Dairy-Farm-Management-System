from mID_retrievals import retrieve_MID_e
from flask import render_template
from database_conn import db_conn
conn=db_conn()


def view_animals():
    mID=retrieve_MID_e()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animals where M_ID=?",(mID))
    animals_data = cursor.fetchall()
    return render_template('/e_pages/view_animals.html', animals_data=animals_data)

def view_animals_health():
    mID=retrieve_MID_e()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Animal_Health_Info where M_ID=?",(mID))
    health_data = cursor.fetchall()
    return render_template('/e_pages/view_health.html', health_data=health_data)

def view_sales_e():
    mID=retrieve_MID_e()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sales where M_ID=?",(mID))
    sales_data = cursor.fetchall()
    return render_template('/e_pages/view_sales_e.html', sales_data=sales_data)

def view_products_e():
    mID=retrieve_MID_e()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products where M_ID=?",(mID))
    products_data = cursor.fetchall()
    return render_template('/e_pages/view_products_e.html', products_data=products_data)

def milk_production_view_e():
    mID=retrieve_MID_e()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Milk_Production where M_ID=?",(mID))
    milkproduction_data = cursor.fetchall()
    return render_template('/e_pages/milk_production_view_e.html', milk_data=milkproduction_data)
