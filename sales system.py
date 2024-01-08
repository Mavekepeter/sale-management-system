# importing libraries
import tkinter as tk
from tkinter import messagebox
import sqlite3

# creating window
root_window = tk.Tk()
root_window.title("Sales Management")
root_window.geometry("720x750")

# creating entry variables
name_entry_text = tk.StringVar()
id_entry_text = tk.StringVar()
quantity_sold_entry_text = tk.StringVar()
quantity_left_entry_text = tk.StringVar()
price_entry_text = tk.StringVar()
today_sales_quantity_entry_text = tk.StringVar()
today_sales_total_price_entry_text = tk.StringVar()
week_sales_quantity_entry_text = tk.StringVar()
week_sales_total_price_entry_text = tk.StringVar()
month_sales_quantity_entry_text = tk.StringVar()
month_sales_total_price_entry_text = tk.StringVar()

delete_entry = tk.StringVar()

# creating the entries
name_entry = tk.Entry(root_window, textvariable=name_entry_text)
id_entry = tk.Entry(root_window, textvariable=id_entry_text)
quantity_sold_entry = tk.Entry(root_window, textvariable=quantity_sold_entry_text)
quantity_left_entry = tk.Entry(root_window, textvariable=quantity_left_entry_text)
price_entry = tk.Entry(root_window, textvariable=price_entry_text)
today_sales_quantity_entry = tk.Entry(root_window, textvariable=today_sales_quantity_entry_text)
today_sales_total_price_entry = tk.Entry(root_window, textvariable=today_sales_total_price_entry_text)
week_sales_quantity_entry = tk.Entry(root_window, textvariable=week_sales_quantity_entry_text)
week_sales_total_price_entry = tk.Entry(root_window, textvariable=week_sales_total_price_entry_text)
month_sales_quantity_entry = tk.Entry(root_window, textvariable=month_sales_quantity_entry_text)
month_sales_total_price_entry = tk.Entry(root_window, textvariable=month_sales_total_price_entry_text)
delete_entry = tk.Entry(root_window, textvariable=delete_entry, width=20)
delete_entry.grid(row=6, column=3, padx=10, columnspan=3, rowspan=2)

delete_entry.insert(0, 'Enter id to delete')

# create the labels
name_label = tk.Label(root_window, text="Product name")
id_label = tk.Label(root_window, text="Product ID")
quantity_sold_label = tk.Label(root_window, text="Quantity sold")
quantity_left_label = tk.Label(root_window, text="Quantity left")
price_label = tk.Label(root_window, text="Price")
today_sales_quantity_label = tk.Label(root_window, text="Today's Sales(quantity)")
today_sales_total_price_label = tk.Label(root_window, text="Today's Sales(Total Price)")
week_sales_quantity_label = tk.Label(root_window, text="Week Sales(quantity)")
week_sales_total_price_label = tk.Label(root_window, text="Week Sales(Total Price)")
month_sales_quantity_label = tk.Label(root_window, text="Month Sales(quantity)")
month_sales_total_price_label = tk.Label(root_window, text="Month Sales(Total Price)")

product_list_label = tk.Label(root_window, text='Product List', font=(30), borderwidth=1, relief="solid", width=50)
product_list_label.grid(row=12, column=0, columnspan=50, pady=20)

pdt_name = tk.Label(root_window, text='Product Name', borderwidth=1, relief="solid")
pdt_id = tk.Label(root_window, text='Product ID', borderwidth=1, relief="solid")
pdt_price = tk.Label(root_window, text='Product Price', borderwidth=1, relief="solid")
pdt_sales_quantity = tk.Label(root_window, text="Today's Sales(Quantity)", borderwidth=1, relief="solid")

# creating functions
def Refresh():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS products (name TEXT, id TEXT PRIMARY KEY, quantitySold TEXT, quantityLeft TEXT, price TEXT, todaySalesQuantity TEXT, todaySalesTotalPrice TEXT, weekSalesQuantity TEXT, weekSalesTotalPrice TEXT, monthSalesQuantity TEXT, monthSalesTotalPrice TEXT)")

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    for i in range(len(products)):
        tk.Label(root_window, text=products[i][0]).grid(row=i+14, column=0)
        tk.Label(root_window, text=products[i][1]).grid(row=i+14, column=1)
        tk.Label(root_window, text=products[i][4]).grid(row=i+14, column=2)
        tk.Label(root_window, text=products[i][5]).grid(row=i+14, column=3)
    conn.close()

def show_message(title, message):
    messagebox.showerror(title, message)

def add_product():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, id, quantitySold, quantityLeft, price, todaySalesQuantity, todaySalesTotalPrice, weekSalesQuantity, weekSalesTotalPrice, monthSalesQuantity, monthSalesTotalPrice) VALUES (?, ?, ?, ?,?,?,?,?,?,?,?)", (str(name_entry_text.get()), str(id_entry_text.get()), str(quantity_sold_entry_text.get()), str(quantity_left_entry_text.get()), str(price_entry_text.get()), str(today_sales_quantity_entry_text.get()), str(today_sales_total_price_entry_text.get()), str(week_sales_quantity_entry_text.get()), str(week_sales_total_price_entry_text.get()), str(month_sales_quantity_entry_text.get()), str(month_sales_total_price_entry_text.get())))

        conn.commit()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        Refresh()
        conn.close()

def delete_product():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        cursor.execute("DELETE FROM products WHERE id = ?", (str(delete_entry.get())))
        conn.commit()
        show_message('Success', 'Product deleted')
        conn.close()
        Refresh()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        conn.close()
        Refresh()

def update():
    price = price_entry_text.get()
    quantity_sold = quantity_sold_entry_text.get()
    quantity_left = quantity_left_entry_text.get()
    today_sales_quantity = today_sales_quantity_entry_text.get()
    week_sales_quantity = week_sales_quantity_entry_text.get()
    month_sales_quantity = month_sales_quantity_entry_text.get()
    if len(price) < 1 or len(quantity_sold) < 1 or len(quantity_left) < 1 or len(today_sales_quantity) < 1 or len(week_sales_quantity) < 1 or len(month_sales_quantity) < 1:
        show_message('Python error!', 'Please enter values for all fields')
        return
    try:
        price = int(price)
        quantity_sold = int(quantity_sold)
        quantity_left = int(quantity_left)
        today_sales_quantity = int(today_sales_quantity)
        week_sales_quantity = int(week_sales_quantity)
        month_sales_quantity = int(month_sales_quantity)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("UPDATE products SET name=?, id=?, quantitySold=?, quantityLeft=?, price=?, todaySalesQuantity=?, todaySalesTotalPrice=?, weekSalesQuantity=?, weekSalesTotalPrice=?, monthSalesQuantity=?, monthSalesTotalPrice=?  WHERE id=?", (str(name_entry_text.get()), str(id_entry_text.get()), str(quantity_sold_entry_text.get()), str(quantity_left_entry_text.get()), str(price_entry_text.get()), str(today_sales_quantity_entry_text.get()), str(today_sales_total_price_entry_text.get()), str(week_sales_quantity_entry_text.get()), str(week_sales_total_price_entry_text.get()), str(month_sales_quantity_entry_text.get()), str(month_sales_total_price_entry_text.get()), str(id_entry_text.get())))
        conn.commit()
        Refresh()
        show_message('Success', 'Product updated')
        conn.close()
    except sqlite3.Error as e:
        show_message('Sqlite error', e)
    finally:
        Refresh()
        conn.close()

def calculate():
    price = price_entry_text.get()
    quantity_sold = quantity_sold_entry_text.get()
    quantity_left = quantity_left_entry_text.get()
    today_sales_quantity = today_sales_quantity_entry_text.get()
    week_sales_quantity = week_sales_quantity_entry_text.get()
    month_sales_quantity = month_sales_quantity_entry_text.get()
    if len(price) < 1 or len(quantity_sold) < 1 or len(quantity_left) < 1 or len(today_sales_quantity) < 1 or len(week_sales_quantity) < 1 or len(month_sales_quantity) < 1:
        show_message('Python error!', 'Please enter values for all fields')
        return
    try:
        price = int(price)
        quantity_sold = int(quantity_sold)
        quantity_left = int(quantity_left)
        today_sales_quantity = int(today_sales_quantity)
        week_sales_quantity = int(week_sales_quantity)
        month_sales_quantity = int(month_sales_quantity)
    except:
        show_message('Python error!', 'Please enter integer values in these fields-> Price, Today Sales(Quantity), Week Sales(Quantity), Month Sales(Quantity)')
        return
    today_sales_total_price = price * today_sales_quantity
    week_sales_total_price = price * week_sales_quantity
    month_sales_total_price = price * month_sales_quantity

    today_sales_total_price_entry_text.set(today_sales_total_price)
    week_sales_total_price_entry_text.set(week_sales_total_price)
    month_sales_total_price_entry_text.set(month_sales_total_price)
    add_button.config(state='normal')

# calling this function to show stored data
Refresh()

# creating buttons
update_button = tk.Button(text='UPDATE', width=20, height=2, command=update)
delete_button = tk.Button(text='DELETE', width=20,height=2, command=delete_product)
add_button = tk.Button(text='ADD', width=20, height=2, command=add_product)
add_button.config(state='disabled')
calculate_button = tk.Button(text='Verify And Calculate Prices', width=25, height=2, command=calculate)
refresh_button = tk.Button(text='Refresh Table', width=25, height=2, command=Refresh)

# placing widgets in the root window using grid
name_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
id_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
quantity_sold_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
quantity_left_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
price_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
today_sales_quantity_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
today_sales_total_price_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')
week_sales_quantity_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')
week_sales_total_price_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')
month_sales_quantity_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')
month_sales_total_price_label.grid(row=10, column=0, padx=10, pady=10, sticky='w')

name_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
id_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
quantity_sold_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')
quantity_left_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')
price_entry.grid(row=4, column=1, padx=10, pady=10, sticky='w')
today_sales_quantity_entry.grid(row=5, column=1, padx=10, pady=10, sticky='w')
today_sales_total_price_entry.grid(row=6, column=1, padx=10, pady=10, sticky='w')
today_sales_total_price_entry.config(state='disabled')
week_sales_quantity_entry.grid(row=7, column=1, padx=10, pady=10, sticky='w')
week_sales_total_price_entry.grid(row=8, column=1, padx=10, pady=10, sticky='w')
week_sales_total_price_entry.config(state='disabled')
month_sales_quantity_entry.grid(row=9, column=1, padx=10, pady=10, sticky='w')
month_sales_total_price_entry.grid(row=10, column=1, padx=10, pady=10, sticky='w')
month_sales_total_price_entry.config(state='disabled')

update_button.grid(row=3, column=2, rowspan=2, padx=15)
delete_button.grid(row=6, column=2, rowspan=2, padx=15)
calculate_button.grid(row=11, column=0, columnspan=2)
add_button.grid(row=11, column=2)
refresh_button.grid(row=11, column=3)

pdt_name.grid(row=13, column=0)
pdt_id.grid(row=13, column=1)
pdt_price.grid(row=13, column=2)
pdt_sales_quantity.grid(row=13, column=3)

root_window.mainloop()