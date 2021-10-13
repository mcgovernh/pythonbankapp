from tkinter import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import ctypes  # An included library with Python install.

import config # import global variables for form
from config import database

def updatedatabase():
    try:
        connection = database.connect_db()
        cursor = connection.cursor()
        database.connect_updatestudent(cursor, config.firstname.get(), config.lastname.get(), config.address.get(), config.balance.get())
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Student table {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            print("MySQL connection is closed")
    root.destroy()
def login():
    ## Use of global variables makes them available in all functions
    global root
    root=Tk()
    root.title("Student Database")
    root.geometry("450x350")
    root.config(bg="pink")
    root.resizable(0,0)

    Label(root, text='Please Enter your Student Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()

    # added root to StringVar to get form working properly
    config.firstname = StringVar(root)
    config.lastname = StringVar(root)
    config.address = StringVar(root)
    config.balance = StringVar(root)

    Label(root, text="").pack()
    Label(root, text="Firstname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.firstname).pack()
    Label(root, text="Lastname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.lastname).pack()
    Label(root, text="Address :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.address).pack()
    Label(root, text="").pack()
    Label(root, text="Balance :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.balance).pack()
    Label(root, text="").pack()

    Button(root, text="Store to Dbase", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=updatedatabase).pack()
    Button(root, text="Exit", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=Exit).pack()

    Label(root, text="")

    root.mainloop()

def Exit():
    wayOut = Mbox('Student Database', 'Do you want to exit?', 1)
    if wayOut == 1 :
        root.destroy()
    return

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

##login()
#root.mainloop() ## this causes the program to loop indefinitely
