from database_conn import db_conn
conn=db_conn()


# Insert data into the manager table
def insert_manager_data(data):
    cursor = conn.cursor()
    query = "INSERT INTO manager VALUES (?, ?, ?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into emplyees table
def insert_employee_data(data):
    cursor = conn.cursor()
    query = "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into milk production table
def insert_milk_data(data):
    cursor = conn.cursor()
    query = "INSERT INTO Milk_Production VALUES (?, ?, ?, ?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into animals table
def insert_animals(data):
    cursor = conn.cursor()
    query = "INSERT INTO animals VALUES (?, ?, ?, ?,?,?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into health record table
def insert_health_record(data):
    cursor = conn.cursor()
    query = "INSERT INTO Animal_Health_Info VALUES (?,?, ?, ?, ?,?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into products table
def insert_products(data):
    cursor = conn.cursor()
    query = "INSERT INTO products VALUES (?, ?, ?, ?,?,?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into sales table
def insert_sales_record(data):
    cursor = conn.cursor()
    query = "INSERT INTO sales VALUES (?, ?, ?, ?,?,?)"
    cursor.execute(query, data)
    conn.commit()

# insert data into daily income table
def insert_daily_income(data):
    cursor = conn.cursor()
    query = "INSERT INTO Daily_Income VALUES (?, ?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()