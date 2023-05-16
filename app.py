from flask import Flask, render_template,request
from insertions import *
from retrievals import *
from manager_views import *
from mID_retrievals import *
from employee_views import *
from login_logout import *
from graphs import *
from edit import *
from delete import *
from search import *

app = Flask(__name__)
app.secret_key = 'xyzsdfg'


#########################
# ROUTES FOR ALL WEBPAGES

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/signup')
def signup():
    return render_template('/m_pages/signup.html')

@app.route('/login')
def login():
    return render_template('/m_pages/login.html')

@app.route('/login_e')
def login_e():
    return render_template('/e_pages/login_e.html')

@app.route('/m_view')
def m_view():
    return render_template('/m_pages/m_view.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/e_view')
def e_view():
    return render_template('/e_pages/e_view.html')

@app.route('/animals')
def animals():
    return render_template('/e_pages/animals.html')

@app.route('/health')
def health():
    return render_template('/e_pages/Health.html')

@app.route('/sales')
def sales():
    return render_template('/e_pages/Sales.html')

@app.route('/product_info')
def product_info():
    return render_template('/e_pages/product_info.html')

@app.route('/finance')
def finance():
    return render_template('/e_pages/finance.html')

@app.route('/others')
def others():
    return render_template('/m_pages/others.html')


######################################################
# ROUTES FOR LOGIN AND LOGOUT FOR MANAGER AND EMPLOYEES
# THESE ROUTES ARE USING LOGIN_LOGOUT.PY FILE

# for manager login
@app.route('/login_form', methods=['GET', 'POST'])
def m_login():
    return login_account()

#for manager logout
@app.route('/logout_manager')
def m_logout():
    return logout_manager()

# for employee login
@app.route('/login_form_employee', methods=['GET', 'POST'])
def e_login():
    return login_account_employee()

#for employee logout
@app.route('/logout_employee')
def e_logout():
    return logout_employee()


##################################################################
# ROUTES FOR DATA RETRIEVAL FROM WEBPAGES AND INSERTION IN DATABASE
# THESE ROUTES USE RETRIEVALS.PY AND INSERTIONS.PY FILES


# function to add new manager
@app.route('/signup_form', methods=['GET', 'POST'])
def retrieval_1():
    return create_account()

# function to add new employee
@app.route('/add_employee_form', methods=['GET', 'POST'])
def retrieval_2():
    return add_employee()

# function for animals data
@app.route('/add_animals', methods=['GET', 'POST'])
def retrieval_3():
    return add_animals()

# function for milk production data 
@app.route('/add_milk_record', methods=['GET', 'POST'])
def retrieval_4():
    return add_milk_record()

# function for animal health data 
@app.route('/add_health_record', methods=['GET', 'POST'])
def retrieval_5():
    return add_health_record()

# function for products data 
@app.route('/add_product', methods=['GET', 'POST'])
def retrieval_6():
    return add_product()

# function for sales data 
@app.route('/add_sales', methods=['GET', 'POST'])
def retrieval_7():
    return add_sales()

# function for daily income data 
@app.route('/add_daily_income', methods=['GET', 'POST'])
def retrieval_8():
    return add_daily_income()


#########################
# ROUTES FOR MANAGER VIEWS
# THESE ROUTES USES MANAGER_VIEWS.PY

@app.route('/milk_production_view_m')
def m_views_1():
    return milk_production_view_m()

@app.route('/income_view_m')
def m_views_2():
    return income_view_m()

@app.route('/sales_view_m')
def m_views_3():
    return sales_view_m()

@app.route('/view_employees')
def m_views_4():
    return view_employees()


##########################
# ROUTES FOR EMPLOYEE VIEWS
# THESE ROUTES USES EMPLOYEE_VIEWS.PY

@app.route('/view_animals')
def e_view_1():
    return view_animals()

@app.route('/view_animals_health')
def e_view_2():
    return view_animals_health()

@app.route('/view_sales_e')
def e_view_3():
    return view_sales_e()

@app.route('/view_products_e')
def e_view_4():
    return view_products_e()

@app.route('/milk_production_view_e')
def e_view_5():
    return milk_production_view_e()


########################
#page to view no data meesage

@app.route('/no_data')
def no_data():
    previous_url = request.referrer
    return render_template('no_data.html', url=previous_url)


#########################
# ROUTES FOR GRAPH VIEWS

@app.route('/milk_production_stats')
def graphs_1():
    return milk_production_stats()

@app.route('/income_stats')
def graphs_2():
    return income_stats()

@app.route('/sales_stats')
def graph_3():
    return sales_stats()



###################################
# ROUTES FOR EDITING TABLE ENTRIES
#THESE ROUTES ARE USING EDIT.PY FILE

@app.route('/edit_milk_production/<production_date>/<animal_id>', methods=['GET', 'POST'])
def edit_1(production_date, animal_id):
    return edit_milk_production_entry(production_date, animal_id)
    
@app.route('/edit_animals/<aID>/<mID>', methods=['GET', 'POST'])
def edit_2(aID, mID):
    return edit_animals_entry(aID, mID)

@app.route('/edit_animal_health/<aID>/<mID>', methods=['GET', 'POST'])
def edit_3(aID, mID):
    return edit_animal_health_entry(aID, mID)

@app.route('/edit_sales/<sID>/<mID>', methods=['GET', 'POST'])
def edit_4(sID, mID):
    return edit_sales_entry(sID, mID)

@app.route('/edit_products/<pID>/<mID>', methods=['GET', 'POST'])
def edit_5(pID, mID):
    return edit_product_entry(pID, mID)

@app.route('/edit_profile_e/<username>/<password>',methods=['GET', 'POST'])
def edit_profile_e(username,password):
    return edit_employee_profile(username,password)
  
@app.route('/edit_employee_m/<eID>/<mID>',methods=['GET', 'POST'])
def edit_employee_m(eID,mID):
    return edit_employee_profile_m(eID,mID)

@app.route('/edit_profile_m',methods=['GET', 'POST'])
def edit_profile_m():
    mID=retrieve_MID_m()
    return edit_manager_profile(mID)


##############################
# ROUTES FOR DELETEING ENTRIES FROM DATABASE
# THESE ROUTES ARE USING DELETE.PY FILE

@app.route('/delete_milk_production/<production_date>/<animal_id>', methods=['GET', 'POST'])
def delete_1(production_date, animal_id):
    return delete_milk_production_entry(production_date, animal_id)

@app.route('/delete_animal_entry/<aID>/<mID>', methods=['GET', 'POST'])
def delete_2(aID, mID):
    return delete_animal_entry(aID, mID)

@app.route('/delete_animal_health_entry/<aID>/<mID>', methods=['GET', 'POST'])
def delete_3(aID, mID):
    return delete_animal_health_entry(aID, mID)

@app.route('/delete_sales/<sID>/<mID>', methods=['GET', 'POST'])
def delete_4(sID, mID):
    return delete_sales_entry(sID, mID)

@app.route('/delete_products/<pID>/<mID>', methods=['GET', 'POST'])
def delete_5(pID, mID):
    return delete_product_entry(pID, mID)

@app.route('/delete_employee/<eID>/<mID>', methods=['GET', 'POST'])
def delete_e(eID, mID):
    return delete_employee(eID, mID)

########################
# ROUTES FOR SEARCH TABS IN VIEWS
# THESE ROUTES ARE USING SEARCH.PY FILE

@app.route('/search_milk_data_m', methods=['GET','POST'])
def search_1():
    return search_milk_data_m()

@app.route('/search_milk_data_e', methods=['GET','POST'])
def search_1_e():
    return search_milk_data_e()

@app.route('/search_revenue_record_m', methods=['GET','POST'])
def search_2():
    return search_revenue_record_m()

@app.route('/search_sales_m', methods=['GET','POST'])
def search_3():
    return search_sales_m()

@app.route('/search_sales_e', methods=['GET','POST'])
def search_3_e():
    return search_sales_e()

@app.route('/search_employee_m', methods=['GET','POST'])
def search_4():
    return search_employee_m()

@app.route('/search_animal', methods=['GET','POST'])
def search_5():
    return search_animals()

@app.route('/search_health', methods=['GET','POST'])
def search_6():
    return search_health()

if __name__ == '__main__':
    app.run(debug=True)
