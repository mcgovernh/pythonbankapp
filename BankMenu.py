import ctypes  # An included library with Python install.
from tkinter import *
from tkinter import Menu
import tkinter  as tk
import mysql.connector

from CreateAccount import *  # imports everything from CreateAccount file
from config import database

window = Tk()
window.title("Banking App")
menu = Menu(window)

def pulldownmenu():
    ## File Pull down menu
    new_file1 = Menu(menu, tearoff=0)
    menu.add_cascade(label='File', menu=new_file1)
    new_file1.add_command(label='Refresh', command=adddata)
    new_file1.add_command(label='Exit Application', command=LogOut)

    ## Edit Pull Down Menu
    new_edit1 = Menu(menu, tearoff=0)
    menu.add_cascade(label='Edit', menu=new_edit1)
    new_edit1.add_command(label='Create Account', command=login)
    new_edit1.add_command(label='Delete Account')
    new_edit1.add_command(label='Edit Account')
    new_edit1.add_command(label='Transfer Funds')
    new_edit1.add_command(label='Withdraw Funds')
    new_edit1.add_command(label='Deposit Funds')
    new_edit1.add_command(label='View Transactions')

def adddata():

    ## add account data to window
    my_w = window
    my_connect = mydb = database.connect_db()
    my_conn = my_connect.cursor()
    ## erase any data in widget
    print(window.winfo_children())

    widget_list = window.winfo_children()
    for item in widget_list:
        item.pack_forget()
        ##item.destroy()

    ####### end of connection ####
    database.connect_getstudent(my_conn)
    i=0
    for student in my_conn:
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i=i+1

def LogOut():
    wayOut = Mbox('Alert', 'Logout?', 1)
    if wayOut == 1 :
        window.destroy()
    return

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#code from MainMenu and Transactions for Buttons and Labels and TextBoxes
    ## from main menu
    # Define the different GUI widgets
    #self.name_label = tk.Label(self.root, text="Name:")
    #self.name_entry = tk.Entry(self.root)
    #self.name_label.grid(row=0, column=0, sticky=tk.W)
    #self.name_entry.grid(row=0, column=1)

    #self.idnumber_label = tk.Label(self.root, text="ID:")
    #self.idnumber_entry = tk.Entry(self.root)
    #self.idnumber_label.grid(row=1, column=0, sticky=tk.W)
    #self.idnumber_entry.grid(row=1, column=1)

    #self.edit_button = tk.Button(self.root, text="Create", command=login,height = 1, width = 8)
    #self.edit_button.grid(row=0, column=0, sticky=tk.W)

    #self.edit_button = tk.Button(self.root, text="Edit", command=self.geteditid,height=1, width=8)
    #self.edit_button.grid(row=0, column=1, sticky=tk.W)

    #self.submit_button = tk.Button(self.root, text="Refresh", command=self.insert_data,height = 1, width = 8)
    #self.submit_button.grid(row=0, column=2, sticky=tk.W)

    #self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_data,height = 1, width = 8)
    #self.delete_button.grid(row=1, column=2, sticky=tk.W)

    #self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy,height = 1, width = 8)
    #problem with self.root.quit self.root.destroy seems to work better
    #self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit,height = 1, width = 8)
    #self.exit_button.grid(row=0, column=3, sticky=tk.W)

    #self.exit_button = tk.Button(self.root, text="Transfer", command=self.transfer,height = 1, width = 8)
    #self.exit_button.grid(row=1, column=3, sticky=tk.W)

    #self.exit_button = tk.Button(self.root, text="TransList", command=self.gettransid,height = 1, width = 8)
    #self.exit_button.grid(row=1, column=4, sticky=tk.W)

    #self.exit_button = tk.Button(self.root, text="Deposit", command=self.deposit,height = 1, width = 8)
    #self.exit_button.grid(row=1, column=0, sticky=tk.W)

    #self.exit_button = tk.Button(self.root, text="Withdraw", command=self.withdraw,height = 1, width = 8)
    #self.exit_button.grid(row=1, column=1, sticky=tk.W)

    ## from Transactions
    #self.submit_button = tk.Button(self.root2, text="Refresh", command=self.insert_data,height = 1, width = 8)
    #self.submit_button.grid(row=0, column=1, sticky=tk.W)

    #self.delete_button = tk.Button(self.root2, text="Delete", command=self.delete_data,height = 1, width = 8)
    #self.delete_button.grid(row=0, column=2, sticky=tk.W)

    #self.exit_button = tk.Button(self.root2, text="Exit", command=self.root2.destroy,height = 1, width = 8)
    #self.exit_button.grid(row=0, column=3, sticky=tk.W)


# run functions
pulldownmenu()
adddata()
window.config(menu=menu)
window.mainloop()
