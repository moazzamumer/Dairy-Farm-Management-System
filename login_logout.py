from flask import request,session,render_template,redirect
from database_conn import db_conn

conn=db_conn()


def login_account():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to check if the username and password are valid
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Manager WHERE M_UserName=? AND Password=?", (username, password))
        manager = cursor.fetchone()

        if manager:
            # If the user is found in the database, store their username in a session variable
            session['username'] = manager.M_UserName
            session['password'] = manager.Password
            return redirect('/milk_production_view_m')
        else:
            # If the username or password is incorrect, display an error message
            error_message = 'Invalid username or password.'
            return error_message

    return render_template('/m_pages/login.html')

def logout_manager():
    session.clear()
    return redirect('/')


def login_account_employee():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to check if the username and password are valid
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE Login_username=? AND Login_password=?", (username, password))
        employee = cursor.fetchone()

        if employee:
            # If the user is found in the database, store their username in a session variable
            session['username'] = employee.Login_username
            session['password'] = employee.Login_password
            return redirect("/e_view")
        else:
            # If the username or password is incorrect, display an error message
            error_message = 'Invalid username or password.'
            return error_message

    return render_template('/e_pages/login_e.html')

def logout_employee():
    session.clear()
    return redirect('/')

