import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

from tkinter import Menu

from CreateAccount import *  # imports everything from CreateAccount file
import config # import global variables for form

sys.path.append(".") # importing classes from other files

import Transactions
from config import database
from Transactions import TransactionsForm
from EditAccount import *
from WithdrawAccount import *
from DepositAccount import *
from TransferAccount import *


class AccountsMenu(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()
        self.getdata()
        self.pulldownmenu(root)

    def pulldownmenu(self,root):
        ## File Pull down menu
        menu = Menu(root)
        root.config(menu=menu) # this adds menu bar to frame
        new_file1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=new_file1)
        new_file1.add_command(label='Refresh', command=self.insert_data)
        new_file1.add_command(label='Exit Application', command=self.root.destroy)

        ## Edit Pull Down Menu
        new_edit1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='Edit', menu=new_edit1)
        new_edit1.add_command(label='Create Account', command=login)
        new_edit1.add_command(label='Delete Account', command=self.delete_data)
        new_edit1.add_command(label='Edit Account', command=self.geteditid)
        new_edit1.add_command(label='Transfer Funds', command=self.transfer)
        new_edit1.add_command(label='Withdraw Funds', command=self.withdraw)
        new_edit1.add_command(label='Deposit Funds', command=self.deposit)
        new_edit1.add_command(label='View Transactions', command=self.gettransid)

    def initialize_user_interface(self):

        # Configure the root object for the Application
        self.root.title("Banking Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.config(background="lightblue")
        self.root.resizable(0,0)
        # this creates other windows. Need something better.
        #self.root.eval('tk::PlaceWindow . center')

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Id', 'Firstname','Lastname','Address','Balance'))

        # Set the heading (Attribute Names)
        self.tree.heading('#1', text='Id')
        self.tree.heading('#2', text='Firstname')
        self.tree.heading('#3', text='Lastname')
        self.tree.heading('#4', text='Address')
        self.tree.heading('#5', text='Balance')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#1', width=100, stretch=tk.NO)
        self.tree.column('#2', width=200, stretch=tk.NO)
        self.tree.column('#3', width=200, stretch=tk.NO)
        self.tree.column('#4', width=200, stretch=tk.NO)
        self.tree.column('#5', width=100, stretch=tk.NO)

        self.tree.column("#0", width=0)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def getdata(self):
        mydb = database.connect_db()
        my_conn = mydb.cursor()
        database.connect_getstudent(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)

    def delete_data(self):
        row_id = self.tree.focus()
        #print (self.tree.item(row_id)['values'][0])
        row_id = self.tree.item(row_id)['values'][0]

        mydb = database.connect_db()
        mycursor = mydb.cursor()
        id = (row_id, )
        database.connect_deletestudent(mycursor,id)
        mydb.commit()

        ## refresh table
        for i in self.tree.get_children():
            self.tree.delete(i)
        my_conn = mydb.cursor()
        database.connect_getstudent(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)

    def geteditid(self):
        global passedidnumber
        editid = self.tree.focus()
        row_id = self.tree.item(editid)['values'][0]
        #print (row_id)
        passedidnumber = row_id
        editrecord(passedidnumber)

    def transfer(self):
        global passedidnumber
        editid = self.tree.focus()
        row_id = self.tree.item(editid)['values'][0]
        #print (row_id)
        passedidnumber = row_id
        transferrecord(passedidnumber)

    def withdraw(self):
        global passedidnumber
        editid = self.tree.focus()
        row_id = self.tree.item(editid)['values'][0]
        passedidnumber = row_id
        withdrawrecord(passedidnumber)

    def deposit(self):
        global passedidnumber
        editid = self.tree.focus()
        row_id = self.tree.item(editid)['values'][0]
        #print (row_id)
        passedidnumber = row_id
        depositrecord(passedidnumber)

    def insert_data(self):
        mydb = database.connect_db()
        my_conn = mydb.cursor()
        ## refresh table
        for i in self.tree.get_children():
            self.tree.delete(i)
        database.connect_getstudent(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)

    def gettransid(self):
        global passedidnumber
        editid = self.tree.focus()
        row_id = self.tree.item(editid)['values'][0]
        passedidnumber = (row_id, )
        #print (passedidnumber)
        app2 = Transactions.TransactionsForm(tk.Tk())
        #app2.transactionform(tk.root2)
        app2.gettransdata(passedidnumber)


#app = AccountsMenu(tk.Tk())
#app.root.mainloop()
