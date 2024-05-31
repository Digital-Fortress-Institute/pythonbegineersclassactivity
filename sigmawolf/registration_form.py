import tkinter as tk
from tkinter import messagebox
import sqlite3

def conn_db():
    conn = sqlite3.connect('reg_form.db')
    i = conn.cursor()
    i.execute("""
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
    conn.commit()
    conn.close()

def registration():
    username = user_entry.get()
    password = pass_entry.get()
    email = em_entry.get()

    if username == "" or password == "" or email == "":
        messagebox.showerror('Error, all fields are required')
    else:
        conn = sqlite3.connect('reg_form.db')
        i = conn.cursor()
        i.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                  (username, password, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('Successfully registered')
        user_entry.delete(0, tk.END)
        pass_entry.delete(0, tk.END)
        em_entry.delete(0, tk.END)

root = tk.Tk()
root.geometry('300x600')
root.title('Registration Form')

label_username = tk.Label(root, text='Username:')
label_username.grid(row=0, column=0, padx=5, pady=5)
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(root, text='Password:')
label_password.grid(row=1, column=0, padx=5, pady=5)
pass_entry = tk.Entry(root, show='*')
pass_entry.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(root, text='Email:')
label_email.grid(row=2, column=0, padx=5, pady=5)
em_entry = tk.Entry(root)
em_entry.grid(row=2, column=1, padx=5, pady=5)

button_submit = tk.Button(root, text='Submit', command=registration)
button_submit.grid(row=3, columnspan=2, pady=5)

conn_db()

root.mainloop()