from app import retrieve_MID_e,retrieve_MID_m
from flask import request,redirect,flash
import random,string
from insertions import *

def add_milk_record():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    Production_date = request.form.get('dop')
    a_ID =request.form.get("aID")
    quantity =request.form.get("quantity")
    quality=request.form.get("quality").title()
    mID=retrieve_MID_e()

    data=[Production_date,a_ID,mID,quantity,quality]

    insert_milk_data(data)

    return redirect("/e_view")

def add_health_record():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    aID = request.form.get('aID')
    mID=retrieve_MID_e()
    a_name =request.form.get("a_name").title()
    date =request.form.get("date")
    status=request.form.get("status").title()
    treatment=request.form.get("treatment").title()
    cost=request.form.get('cost')

    data=[aID,mID,a_name,date,status,treatment,cost]

    insert_health_record(data)

    return redirect("/health")

def add_product():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    pID = request.form.get('pID')
    p_name =request.form.get("p_name").title()
    mID =retrieve_MID_e()
    ppu=request.form.get("ppu")
    avalability=request.form.get("avalability").title()
    pdate=request.form.get('pdate')
    edate=request.form.get('edate')

    data=[pID,p_name,mID,ppu,avalability,pdate,edate]

    insert_products(data)

    return redirect("/product_info")

def add_sales():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    sID = request.form.get('sID')
    s_date =request.form.get("sdate")
    cname =request.form.get("cName").title()
    pID=request.form.get("pID")
    mID=retrieve_MID_e()
    tcost=request.form.get('t_cost')

    data=[sID,mID,s_date,cname,pID,tcost]

    insert_sales_record(data)

    return redirect("/sales")

def add_daily_income():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    date = request.form.get('date')
    revenue =request.form.get("revenue")
    expense =request.form.get("expense")
    mID=retrieve_MID_e()

    data=[date,revenue,expense,mID]

    insert_daily_income(data)

    return redirect("/finance")

def add_animals():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    a_ID = request.form.get('aID')
    a_name =request.form.get("a_name").title()
    a_type =request.form.get("type").title()
    age=request.form.get("age")
    weight=request.form.get("weight")
    gender=request.form.get("gender").title()
    mID=retrieve_MID_e()

    #mID=request.form.get("mID")

    data=[a_ID,mID,a_name,a_type,age,weight,gender]

    insert_animals(data)

    return redirect("/animals")

def add_employee():
    #MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    employee_id = request.form.get('employeeID')
    e_name=request.form.get("name").title()
    mid=retrieve_MID_m()
    gender=request.form.get("gender").title()
    salary=request.form.get('salary')
    username=request.form.get('username')
    password=request.form.get('password')
    contact = request.form.get('contact')

    data=[employee_id,mid,e_name,gender,contact,salary,username,password]

    insert_employee_data(data)

    return redirect("/m_view")

def create_account():
    MID = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    username = request.form.get('username')
    fullname = request.form.get('fullname').title()
    password = request.form.get('password')
    contact = request.form.get('contact')
    
    # Add checks for username, fullname, password, and contact
    if len(username) <= 6:
        flash("Username must be at least 6 characters long.", "error")
        return redirect('/signup')

    if len(fullname) <= 6:
        flash("Full name must be at least 6 characters long.", "error")
        return redirect('/signup')

    if len(password) <= 4:
        flash("Password must be at least 4 characters long.", "error")
        return redirect('/signup')

    if not contact.isdigit():
        flash("Contact must be a numeric value.", "error")
        return redirect('/signup')
    
    data = [MID, username, fullname, password, contact]

    # Call the function to insert the data into the database
    insert_manager_data(data)

    return redirect('/login')