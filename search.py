from flask import redirect,request,render_template
from database_conn import db_conn
from mID_retrievals import *
conn=db_conn()


def search_milk_data():
    animal_id = request.form.get('animal_id')
    mID=retrieve_MID_m()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Production_Date, A_ID, Quantity, Quality FROM Milk_Production WHERE M_ID = ? AND A_ID=?", (mID,animal_id,))
        milk_data = cursor.fetchall()
        return render_template('/m_pages/milk_production_view_m.html', milk_data=milk_data)
    except Exception as e:
        return f"Error retrieving milk data: {str(e)}"