import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Database Functions
def connect_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    return conn, cursor

def create_table():
    conn, cursor = connect_db()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT,
            category TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(amount, description, category, date):
    conn, cursor = connect_db()
    cursor.execute('''
        INSERT INTO expenses (amount, description, category, date)
        VALUES (?, ?, ?, ?)
    ''', (amount, description, category, date))
    conn.commit()
    conn.close()

def get_expenses(start_date, end_date):
    conn, cursor = connect_db()
    cursor.execute('''
        SELECT * FROM expenses
        WHERE date BETWEEN ? AND ?
    ''', (start_date, end_date))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_summary(start_date, end_date):
    conn, cursor = connect_db()
    cursor.execute('''
        SELECT category, SUM(amount) FROM expenses
        WHERE date BETWEEN ? AND ?
        GROUP BY category
    ''', (start_date, end_date))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Initialize database
create_table()

# Helper Functions
def add_expense_gui():
    try:
        amount = float(amount_entry.get())
        description = description_entry.get()
        category = category_combobox.get()
        date = date_entry.get()

        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')
        
        add_expense(amount, description, category, date)
        messagebox.showinfo("Success", "Expense added successfully")
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please check your data.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_expenses():
    try:
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # Validate date format
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')
        
        expenses = get_expenses(start_date, end_date)
        display_text = "\n".join([f"ID: {row[0]}, Amount: {row[1]}, Description: {row[2]}, Category: {row[3]}, Date: {row[4]}" for row in expenses])
        expenses_text.delete(1.0, tk.END)
        expenses_text.insert(tk.END, display_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_summary():
    try:
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()

        # Validate date format
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')

        summary = get_summary(start_date, end_date)
        display_text = "\n".join([f"Category: {row[0]}, Total Amount: {row[1]}" for row in summary])
        summary_text.delete(1.0, tk.END)
        summary_text.insert(tk.END, display_text)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Application
root = tk.Tk()
root.title("Expense Tracker")

# Create Widgets
tk.Label(root, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Description").grid(row=1, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

tk.Label(root, text="Category").grid(row=2, column=0)
categories = ["Food", "Transportation", "Entertainment", "Others"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=2, column=1)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=3, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense_gui).grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Start Date (YYYY-MM-DD)").grid(row=5, column=0)
start_date_entry = tk.Entry(root)
start_date_entry.grid(row=5, column=1)

tk.Label(root, text="End Date (YYYY-MM-DD)").grid(row=6, column=0)
end_date_entry = tk.Entry(root)
end_date_entry.grid(row=6, column=1)

tk.Button(root, text="Show Expenses", command=show_expenses).grid(row=7, column=0)
tk.Button(root, text="Show Summary", command=show_summary).grid(row=7, column=1)

tk.Label(root, text="Expenses").grid(row=8, column=0, columnspan=2)
expenses_text = tk.Text(root, height=10, width=50)
expenses_text.grid(row=9, column=0, columnspan=2)

tk.Label(root, text="Summary").grid(row=10, column=0, columnspan=2)
summary_text = tk.Text(root, height=10, width=50)
summary_text.grid(row=11, column=0, columnspan=2)

root.mainloop()
