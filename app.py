from flask import Flask, render_template,request,redirect,flash,session
import pyodbc
import random, string

app = Flask(__name__)
app.secret_key = 'xyzsdfg'

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/demo')
def demo():
    return "demo"

conx_string = " DRIVER={SQL SERVER}; server=MOAZZAM-NOTEBOO\SQLEXPRESS; database=DFMS; trusted_connection=YES;"
conn = pyodbc.connect(conx_string)

# Insert data into the manager table
def insert_manager_data(data):
    cursor = conn.cursor()
    query = "INSERT INTO manager VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()

# Route for receiving the data
@app.route('/signup_form', methods=['GET', 'POST'])
def create_account():
    MID = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    username = request.form.get('username')
    fullname = request.form.get('fullname')
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

@app.route('/login_form', methods=['GET', 'POST'])
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
            return redirect('/dashboard')
        else:
            # If the username or password is incorrect, display an error message
            error_message = 'Invalid username or password.'
            return redirect('/demo')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if the user is logged in by verifying the session variable
    if 'username' in session:
        username = session['username']
        return f'Welcome, {username}! This is your dashboard.'
    else:
        return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
