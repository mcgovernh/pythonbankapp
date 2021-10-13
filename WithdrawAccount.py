from tkinter import *
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import ctypes  # An included library with Python install.

import config # import global variables for form
from config import database

def withdrawrecord(passedidnumber):
    global id
    global fn
    global ln
    global ad
    global si
    global wbalance

    try:
        mydb = database.connect_db()
        mycursor = mydb.cursor()
        passedid = (passedidnumber, )
        database.connect_selectstudent(mycursor,passedid)
        record = mycursor.fetchone()
        id = record[0]
        fn = record[1]
        ln = record[2]
        ad = record[3]
        si = record[4]

        mydb.commit()
        #print(mycursor.rowcount, "record(s) selected")

    except mysql.connector.Error as error:
        print("Failed to select record into Student table {}".format(error))

    finally:
        if (mydb.is_connected()):
            mydb.close()
            #print("MySQL connection is closed")

    ## Use of global variables makes them available in all functions
    global root

    root=Tk()
    root.title("Withdrawal Screen")
    root.geometry("450x400")
    root.config(bg="pink")
    root.resizable(0,0)

    Label(root, text='Please Edit your Student Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()

    # added root to StringVar to get form working properly
    config.id = StringVar(root,id)
    config.firstname = StringVar(root,fn)
    config.lastname = StringVar(root,ln)
    config.address = StringVar(root,ad)
    config.balance = StringVar(root,si)
    config.wbalance = StringVar(root,"")


    Label(root, text="").pack()
    Label(root, text="ID :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.id,state=DISABLED).pack()
    Label(root, text="").pack()
    Label(root, text="Firstname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.firstname,state=DISABLED).pack()
    Label(root, text="Lastname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.lastname,state=DISABLED).pack()
    Label(root, text="Address :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.address,state=DISABLED).pack()
    Label(root, text="").pack()
    Label(root, text="Withdrawal Amount :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.wbalance).pack()
    Label(root, text="").pack()

    Button(root, text="Store to Dbase", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=writerecordtodatabase).pack()
    Button(root, text="Exit", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=Exit).pack()

    Label(root, text="")

    root.mainloop()

def writerecordtodatabase():
    try:
        num1 = int(config.balance.get())
        num2 = int('0' + config.wbalance.get()) ## crashes with empty text box
        num3 = str(num1 - num2)

        connection = database.connect_db()
        cursor = connection.cursor()
        database.connect_updateeditstudent(cursor,config.firstname.get(),config.lastname.get(),config.address.get(),num3 ,config.id.get())

        # Write to transaction table
        reference = 'Withdrawal from ' + str(config.id.get())
        database.updatetransactions(cursor,config.id.get(),reference,str(num2),'',num3)

        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into Student table {}".format(error))

    finally:
        if (connection.is_connected()):
            connection.close()
            #print("MySQL connection is closed")
    root.destroy()
def Exit():
    wayOut = Mbox('Student Database', 'Do you want to exit?', 1)
    if wayOut == 1 :
        root.destroy()
    return

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


#editrecord()
#root.mainloop() ## this causes the program to loop indefinitely
