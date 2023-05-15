from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import time
from flask import redirect,render_template,request
from mID_retrievals import retrieve_MID_m
from database_conn import db_conn

conn=db_conn()


#graph for milk production
def milk_production_stats():
    mID=retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT Production_Date, Quantity FROM Milk_Production where M_ID=? ORDER BY Production_Date ASC",(mID))
    milk_data = []
    rows = cursor.fetchall()

    if not rows:
        # No data in the table, handle the case
        # Return an appropriate response or render a template indicating no data
        return redirect('/no_data')
    
    for row in rows:
        production_date = row[0]
        quantity = row[1]
        milk_data.append({'Production_Date': production_date, 'Quantity': quantity})

    # Extract the relevant data for the bar chart
    production_dates = [entry['Production_Date'] for entry in milk_data]
    quantities = [entry['Quantity'] for entry in milk_data]

    # Create the initial bar chart
    fig, ax = plt.subplots(figsize=(14, 5.5))
    ax.bar(production_dates, quantities)
    ax.set_xlabel('Production Date')
    ax.set_ylabel('Quantity (KG)')
    ax.set_title('Milk Production Stats')
    # Rotate x-axis tick labels
    ax.set_xticklabels(production_dates, rotation=90)

    # Adjust layout to prevent overlapping of tick labels
    fig.autofmt_xdate()

    # Update function for the animation
    def update_chart(frame):
        ax.clear()
        ax.bar(production_dates[:frame+1], quantities[:frame+1],color='brown')
        ax.set_xlabel('Production Date')
        ax.set_ylabel('Quantity (KG)')
        ax.set_title('Milk Production Stats')
        # Rotate x-axis tick labels
        #ax.set_xticklabels(production_dates, rotation=90)

    # Adjust layout to prevent overlapping of tick labels
        fig.autofmt_xdate()

    # Animate the chart
    animation = FuncAnimation(fig, update_chart, frames=len(production_dates), interval=500, repeat=False)

    # Save the chart image with a unique filename
    chart_image_filename = f'milk_production_stats_{int(time.time())}.png'
    chart_image_path = f'static/charts/{chart_image_filename}'
    animation.save(chart_image_path, writer='Pillow')

    # Clear the figure to release memory
    plt.clf()

    # Pass the chart image path to the template
    return render_template('/m_pages/milk_production_stats.html', chart_image_filename=f'charts/{chart_image_filename}')


#grpah for income stats
def income_stats():
    mID = retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT Date, Total_Revenue, Total_Expense FROM Daily_Income where M_ID=? ORDER BY Date ASC",(mID))
    income_data = []
    rows = cursor.fetchall()

    if not rows:
        # No data in the table, handle the case
        # Return an appropriate response or render a template indicating no data
        return redirect('/no_data')
    
    for row in rows:
        date = row[0]
        revenue = row[1]
        expense = row[2]
        income_data.append({'Date': date, 'revenue': revenue, 'expense': expense})

    # Extract the relevant data for the line graph
    dates = [entry['Date'] for entry in income_data]
    profit = [entry['revenue'] - entry['expense'] for entry in income_data]

    # Create the initial line graph
    fig, ax = plt.subplots(figsize=(14, 5.5))
    ax.plot(dates, profit, color='blue', marker='o', linewidth=2, markersize=6)
    ax.set_xlabel('Date')
    ax.set_ylabel('Profit')
    ax.set_title('Daily Income Stats')

    # Rotate x-axis tick labels
    ax.set_xticklabels(dates, rotation=90)
    # Set the gridlines
    ax.grid(True)
    # Adjust layout to prevent overlapping of tick labels
    fig.autofmt_xdate()

    #animation_running = True
    # Update function for the animation
    def update_chart(frame):
        #nonlocal animation_running
        ax.clear()
        ax.plot(dates[:frame+1], profit[:frame+1], color='red', marker='o', linewidth=2, markersize=6)
        ax.set_xlabel('Date')
        ax.set_ylabel('Profit')
        ax.set_title('Daily Income Stats')
        ax.set_xticklabels(dates, rotation=90)
        # Set the gridlines
        ax.grid(True)
        fig.autofmt_xdate()
        # Stop the animation when it reaches the end
            

    # Animate the chart
    animation = FuncAnimation(fig, update_chart, frames=len(dates), interval=1000)

    # Save the chart image with a unique filename
    chart_image_filename = f'Daily_income_stats_{int(time.time())}.png'
    chart_image_path = f'static/charts/{chart_image_filename}'
    animation.save(chart_image_path, writer='Pillow')

    # Clear the figure to release memory
    plt.clf()

    # Pass the chart image path to the template
    return render_template('/m_pages/income_stats.html', income_image_filename=f'charts/{chart_image_filename}')


#graph for sales stats
def sales_stats():
    mID = retrieve_MID_m()
    cursor = conn.cursor()
    cursor.execute("SELECT P_ID, COUNT(*) AS SalesCount FROM Sales WHERE M_ID=? GROUP BY P_ID", (mID,))
    sales_data = cursor.fetchall()

    if not sales_data:
        # No sales data in the table, handle the case
        # Return an appropriate response or render a template indicating no data
        return redirect('/no_data')

    # Extract the relevant data for the bar chart
    product_ids = [entry[0] for entry in sales_data]
    sales_count = [entry[1] for entry in sales_data]

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(14, 5.5))
    ax.bar(product_ids, sales_count)
    ax.set_xlabel('Product ID')
    ax.set_ylabel('Sales Count')
    ax.set_title('Count of Sales by Product')
    ax.grid(True)
    fig.autofmt_xdate()

    def update_chart(frame):
        #nonlocal animation_running
        ax.clear()
        ax.bar(product_ids[:frame+1], sales_count[:frame+1],color='brown')
        ax.set_xlabel('Product ID')
        ax.set_ylabel('Sales Count')
        ax.set_title('Count of Sales by Product')
        #ax.grid(True)
        fig.autofmt_xdate()

    # Animate the chart
    animation = FuncAnimation(fig, update_chart, frames=len(product_ids), interval=1000)

    # Save the chart image with a unique filename
    chart_image_filename = f'sales_stats_{int(time.time())}.png'
    chart_image_path = f'static/charts/{chart_image_filename}'
    animation.save(chart_image_path, writer='Pillow')

    # Clear the figure to release memory
    plt.clf()

    # Pass the chart image path to the template
    return render_template('/m_pages/sales_stats.html', sales_filename=f'charts/{chart_image_filename}')
