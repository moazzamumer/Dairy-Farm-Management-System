from app import retrieve_MID_e
from flask import request,render_template,redirect
from database_conn import db_conn
conn=db_conn()

def retrieve_milk_production(production_date, animal_id):
    mID=retrieve_MID_e()
    # Connect to the database and retrieve the milk production entry based on the production date and animal ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Milk_Production WHERE Production_Date=? AND A_ID=? AND M_ID=?", (production_date, animal_id,mID))
    milk_entry = cursor.fetchone()

    if milk_entry:
        # If the milk production entry is found, return it as a dictionary
        entry_dict = {
            'Production_Date': milk_entry[0],
            'A_ID': milk_entry[1],
            'Quantity': milk_entry[3],
            'Quality': milk_entry[4]
        }
        return entry_dict
    else:
        # If the milk production entry is not found, return None
        return None
    
def retrieve_animal_entry(aID, mID):
    mID=retrieve_MID_e()
    # Connect to the database and retrieve the milk production entry based on the production date and animal ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Animals WHERE A_ID=? AND M_ID=?", (aID,mID))
    animal_entry = cursor.fetchone()

    if animal_entry:
        
        entry_dict = {
            'A_ID': animal_entry[0],
            'M_ID': animal_entry[1],
            'A_Name': animal_entry[2],
            'Type': animal_entry[3],
            'Age':animal_entry[4],
            'Weight':animal_entry[5],
            'Gender':animal_entry[6]
        }
        return entry_dict
    else:
        
        return None


def update_milk_production(production_date, animal_id, updated_quantity, updated_quality):
    mID=retrieve_MID_e()
    # Connect to the database and update the milk production entry based on the production date and animal ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Milk_Production SET Quantity=?, Quality=? WHERE Production_Date=? AND A_ID=? AND M_ID=?", 
                   (updated_quantity, updated_quality, production_date, animal_id,mID))
    conn.commit()

def update_animal_entry(aID, mID, updated_name, updated_type,updated_age,updated_weight,updated_gender):
    mID=retrieve_MID_e()
    # Connect to the database and update the milk production entry based on the production date and animal ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Animals SET A_Name=?, Type=?, Age=?, Weight=?, Gender=? WHERE A_ID=? AND M_ID=?", 
                   (updated_name, updated_type, updated_age,updated_weight,updated_gender, aID,mID))
    conn.commit()


#@edit_tables.route('/edit_milk_production/<production_date>/<animal_id>', methods=['GET', 'POST'])
def edit_milk_production_entry(production_date, animal_id):
    if request.method == 'GET':
        # Retrieve the milk production entry from the database based on the production date and animal ID
        # You can use these values to query the database and fetch the corresponding entry
        milk_entry = retrieve_milk_production(production_date, animal_id)

        if milk_entry:
            #return milk_entry
            # Render the edit page with the retrieved milk production entry
            return render_template('/edit_pages/edit_milk_production.html', milk_entry=milk_entry)
        else:
            # Handle the case if the milk production entry is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the milk production entry in the database based on the submitted form data
        updated_quantity = request.form.get('quantity')
        updated_quality = request.form.get('quality')

        # Update the milk production entry in the database using the updated quantity and quality values
        update_milk_production(production_date, animal_id, updated_quantity, updated_quality)

        # Redirect to the milk production view page after the update
        return redirect('/milk_production_view_e')
        #return "DONE"

def edit_animals_entry(aID, mID):
    if request.method == 'GET':

        animal_entry = retrieve_animal_entry(aID, mID)

        if animal_entry:
           return render_template('/edit_pages/edit_animals.html', animal_entry=animal_entry)
        else:
            
            return "ERROR"

    elif request.method == 'POST':
        
        updated_name = request.form.get('a_name')
        updated_type = request.form.get('type')
        updated_age = request.form.get('age')
        updated_weight = request.form.get('weight')
        updated_gender = request.form.get('gender')

       
        update_animal_entry(aID, mID, updated_name.title(), updated_type.title(),updated_age,updated_weight,updated_gender.title())

       
        return redirect('/view_animals')
        #return "DONE"


#######################################
#functions to edit animal health info table

def edit_animal_health_entry(a_id, m_id):
    if request.method == 'GET':
        # Retrieve the animal health entry from the database based on the animal ID and M_ID
        # You can use these values to query the database and fetch the corresponding entry
        health_entry = retrieve_animal_health(a_id, m_id)

        if health_entry:
            # Render the edit page with the retrieved animal health entry
            return render_template('/edit_pages/edit_animal_health.html', health_entry=health_entry)
        else:
            # Handle the case if the animal health entry is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the animal health entry in the database based on the submitted form data
        updated_date = request.form.get('date')
        updated_status = request.form.get('status')
        updated_treatment = request.form.get('treatment')
        updated_cost = request.form.get('cost')

        # Update the animal health entry in the database using the updated values
        update_animal_health(a_id, m_id, updated_date, updated_status, updated_treatment, updated_cost)

        # Redirect to the animal health view page after the update
        return redirect('/view_animals_health')
        #return "DONE"

def update_animal_health(a_id, m_id, updated_date, updated_status, updated_treatment, updated_cost):
    # Connect to the database and update the animal health entry based on the animal ID and M_ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Animal_Health_Info SET Date=?, Health_Status=?, Treatment=?, Cost=? WHERE A_ID=? AND M_ID=?", 
                   (updated_date, updated_status, updated_treatment, updated_cost, a_id, m_id))
    conn.commit()

def retrieve_animal_health(a_id, m_id):
    # Connect to the database and retrieve the animal health entry based on the animal ID and M_ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Animal_Health_Info WHERE A_ID=? AND M_ID=?", (a_id, m_id))
    health_entry = cursor.fetchone()

    if health_entry:
        # If the animal health entry is found, return it as a dictionary
        entry_dict = {
            'A_ID': health_entry[0],
            'M_ID': health_entry[1],
            'A_Name': health_entry[2],
            'Date': health_entry[3],
            'Health_Status': health_entry[4],
            'Treatment': health_entry[5],
            'Cost': health_entry[6]
        }
        return entry_dict
    else:
        # If the animal health entry is not found, return None
        return None
    
###################################
#functions to edit sales table entry

def edit_sales_entry(sale_id, m_id):
    if request.method == 'GET':
        # Retrieve the sales entry from the database based on the Sale ID and M_ID
        sales_entry = retrieve_sales_entry(sale_id, m_id)

        if sales_entry:
            # Render the edit page with the retrieved sales entry
            return render_template('/edit_pages/edit_sales.html', sales_entry=sales_entry)
        else:
            # Handle the case if the sales entry is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the sales entry in the database based on the submitted form data
        updated_sale_date = request.form.get('sdate')
        updated_c_name = request.form.get('cName')
        updated_p_id = request.form.get('pID')
        updated_total_cost = request.form.get('t_cost')

        # Update the sales entry in the database using the updated values
        update_sales_entry(sale_id, m_id, updated_sale_date, updated_c_name, updated_p_id, updated_total_cost)

        # Redirect to the sales view page after the update
        return redirect('/view_sales_e')

def update_sales_entry(sale_id, m_id, updated_sale_date, updated_c_name, updated_p_id, updated_total_cost):
    # Connect to the database and update the sales entry based on the Sale ID and M_ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Sales SET Sale_Date=?, C_Name=?, P_ID=?, Total_Cost=? WHERE Sale_ID=? AND M_ID=?", 
                   (updated_sale_date, updated_c_name, updated_p_id, updated_total_cost, sale_id, m_id))
    conn.commit()

def retrieve_sales_entry(sale_id, m_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Sales WHERE Sale_ID = ? AND M_ID = ?", (sale_id, m_id))
        sales_entry = cursor.fetchone()

        if sales_entry:
            # If the sales entry is found, return it as a dictionary
            entry_dict = {
                'Sale_ID': sales_entry[0],
                'M_ID': sales_entry[1],
                'Sale_Date': sales_entry[2],
                'C_Name': sales_entry[3],
                'P_ID': sales_entry[4],
                'Total_Cost': sales_entry[5]
            }
            return entry_dict
        else:
            # If the sales entry is not found, return None
            return None
    except Exception as e:
        # Handle any errors that occur during the retrieval process
        return str(e)

########################
#functions to edit products

def edit_product_entry(p_id, m_id):
    if request.method == 'GET':
        # Retrieve the product entry from the database based on the P_ID and M_ID
        product_entry = retrieve_product_entry(p_id, m_id)

        if product_entry:
            # Render the edit page with the retrieved product entry
            return render_template('/edit_pages/edit_product.html', product_entry=product_entry)
        else:
            # Handle the case if the product entry is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the product entry in the database based on the submitted form data
        updated_p_name = request.form.get('p_name')
        updated_price_per_unit = request.form.get('ppu')
        updated_availability = request.form.get('avalability')
        updated_production_date = request.form.get('pdate')
        updated_expiration_date = request.form.get('edate')

        # Update the product entry in the database using the updated values
        update_product_entry(p_id, m_id, updated_p_name, updated_price_per_unit, updated_availability,
                             updated_production_date, updated_expiration_date)

        # Redirect to the product view page after the update
        return redirect('/view_products_e')

def update_product_entry(p_id, m_id, updated_p_name, updated_price_per_unit, updated_availability,
                         updated_production_date, updated_expiration_date):
    # Connect to the database and update the product entry based on the P_ID and M_ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET P_Name=?, Price_Per_Unit=?, Availability=?, Production_Date=?, Expiration_Date=? "
                   "WHERE P_ID=? AND M_ID=?", 
                   (updated_p_name, updated_price_per_unit, updated_availability, updated_production_date,
                    updated_expiration_date, p_id, m_id))
    conn.commit()



def retrieve_product_entry(p_id, m_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE P_ID = ? AND M_ID = ?", (p_id, m_id))
        product_entry = cursor.fetchone()

        if product_entry:
            # If the product entry is found, return it as a dictionary
            entry_dict = {
                'P_ID': product_entry[0],
                'M_ID': product_entry[1],
                'P_Name': product_entry[2],
                'Price_Per_Unit': product_entry[3],
                'Availability': product_entry[4],
                'Production_Date': product_entry[5],
                'Expiration_Date': product_entry[6]
            }
            return entry_dict
        else:
            # If the product entry is not found, return None
            return None
    except Exception as e:
        # Handle any errors that occur during the retrieval process
        return str(e)

#######################
# functions for employee to edit profile

def edit_employee_profile(username, password):
    if request.method == 'GET':
        # Retrieve the employee profile from the database based on the employee ID and M_ID
        # You can use these values to query the database and fetch the corresponding profile
        employee_profile = retrieve_employee_profile(username, password)

        if employee_profile:
            # Render the edit page with the retrieved employee profile
            return render_template('/edit_pages/edit_profile_e.html', employee_profile=employee_profile)
        else:
            # Handle the case if the employee profile is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the employee profile in the database based on the submitted form data
        e_id=request.form.get('e_id')
        m_id=retrieve_MID_e()
        updated_name = request.form.get('name')
        updated_gender = request.form.get('gender')
        updated_contact = request.form.get('contact')
        updated_salary = request.form.get('salary')
        updated_username = request.form.get('username')
        updated_password = request.form.get('password')

        # Update the employee profile in the database using the updated values
        update_employee_profile(e_id, m_id, updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password)

        # Redirect to the employee profile view page after the update
        return redirect('/')
        #return "DONE"

def update_employee_profile(e_id, m_id, updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password):
    # Connect to the database and update the employee profile based on the employee ID and M_ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Employees SET E_Name=?, Gender=?, Contact=?, Salary=?, Login_username=?, Login_password=? WHERE E_ID=? AND M_ID=?", 
                   (updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password, e_id, m_id))
    conn.commit()

def retrieve_employee_profile(username, password):
    mID=retrieve_MID_e()
    # Connect to the database and retrieve the employee profile based on the employee ID and M_ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees WHERE Login_username=? AND Login_password=? AND M_ID=?", (username,password, mID))
    employee_profile = cursor.fetchone()

    if employee_profile:
        # If the employee profile is found, return it as a dictionary
        profile_dict = {
            'E_ID': employee_profile[0],
            'M_ID': employee_profile[1],
            'E_Name': employee_profile[2],
            'Gender': employee_profile[3],
            'Contact': employee_profile[4],
            'Salary': employee_profile[5],
            'Login_username': employee_profile[6],
            'Login_password': employee_profile[7]
        }
        return profile_dict
    else:
        # If the employee profile is not found, return None
        return None
    

#####################
# functions for manager to edit employee

def edit_employee_profile_m(e_id, m_id):
    if request.method == 'GET':
        # Retrieve the employee profile from the database based on the employee ID and M_ID
        # You can use these values to query the database and fetch the corresponding profile
        employee_profile = retrieve_employee_profile_m(e_id, m_id)

        if employee_profile:
            # Render the edit page with the retrieved employee profile
            return render_template('/edit_pages/edit_employee_profile_m.html', employee_profile=employee_profile)
        else:
            # Handle the case if the employee profile is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the employee profile in the database based on the submitted form data
        updated_name = request.form.get('name')
        updated_gender = request.form.get('gender')
        updated_contact = request.form.get('contact')
        updated_salary = request.form.get('salary')
        updated_username = request.form.get('username')
        updated_password = request.form.get('password')

        # Update the employee profile in the database using the updated values
        update_employee_profile_m(e_id, m_id, updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password)

        # Redirect to the employee profile view page after the update
        return redirect('/view_employees')
        #return "DONE"

def update_employee_profile_m(e_id, m_id, updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password):
    # Connect to the database and update the employee profile based on the employee ID and M_ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Employees SET E_Name=?, Gender=?, Contact=?, Salary=?, Login_username=?, Login_password=? WHERE E_ID=? AND M_ID=?", 
                   (updated_name, updated_gender, updated_contact, updated_salary, updated_username, updated_password, e_id, m_id))
    conn.commit()

def retrieve_employee_profile_m(e_id, m_id):
    # Connect to the database and retrieve the employee profile based on the employee ID and M_ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Employees WHERE E_ID=? AND M_ID=?", (e_id, m_id))
    employee_profile = cursor.fetchone()

    if employee_profile:
        # If the employee profile is found, return it as a dictionary
        profile_dict = {
            'E_ID': employee_profile[0],
            'M_ID': employee_profile[1],
            'E_Name': employee_profile[2],
            'Gender': employee_profile[3],
            'Contact': employee_profile[4],
            'Salary': employee_profile[5],
            'Login_username': employee_profile[6],
            'Login_password': employee_profile[7]
        }
        return profile_dict
    else:
        # If the employee profile is not found, return None
        return None
    
    
#######################
#functions to edit manager 

def edit_manager_profile(m_id):
    if request.method == 'GET':
        # Retrieve the manager profile from the database based on the manager ID
        manager_profile = retrieve_manager_profile(m_id)

        if manager_profile:
            # Render the edit page with the retrieved manager profile
            return render_template('/edit_pages/edit_profile_m.html', manager_profile=manager_profile)
        else:
            # Handle the case if the manager profile is not found
            return "ERROR"

    elif request.method == 'POST':
        # Update the manager profile in the database based on the submitted form data
        updated_username = request.form.get('username')
        updated_fullname = request.form.get('fullname')
        updated_password = request.form.get('password')
        updated_contact = request.form.get('contact')

        # Update the manager profile in the database using the updated values
        update_manager_profile(m_id, updated_username, updated_fullname, updated_password, updated_contact)

        # Redirect to the manager profile view page after the update
        return redirect('/')
        # return "DONE"

def update_manager_profile(m_id, updated_username, updated_fullname, updated_password, updated_contact):
    # Connect to the database and update the manager profile based on the manager ID
    cursor = conn.cursor()
    cursor.execute("UPDATE Manager SET M_UserName=?, M_FullName=?, Password=?, Contact=? WHERE M_ID=?", 
                   (updated_username, updated_fullname, updated_password, updated_contact, m_id))
    conn.commit()

def retrieve_manager_profile(m_id):
    # Connect to the database and retrieve the manager profile based on the manager ID
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Manager WHERE M_ID=?", (m_id,))
    manager_profile = cursor.fetchone()

    if manager_profile:
        # If the manager profile is found, return it as a dictionary
        profile_dict = {
            'M_ID': manager_profile[0],
            'M_UserName': manager_profile[1],
            'M_FullName': manager_profile[2],
            'Password': manager_profile[3],
            'Contact': manager_profile[4]
        }
        return profile_dict
    else:
        # If the manager profile is not found, return None
        return None

