import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter import Menu
from CreateAccount import *  # imports everything from CreateAccount file
import config # import global variables for form

sys.path.append(".") # importing classes from other files

from config import database


class TransactionsForm(tk.Frame):
    def __init__(self, root2):
        self.root2 = root2
        self.transactionform(root2)
        #self.gettransdata()

    def transactionform(self,root2):

        ## File Pull down menu
        menu = Menu(root2)
        root2.config(menu=menu) # this adds menu bar to frame
        new_file1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=new_file1)
        new_file1.add_command(label='Refresh', command=self.insert_data)
        new_file1.add_command(label='Close Form', command=self.root2.destroy)

        ## Edit Pull Down Menu
        new_edit1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='Edit', menu=new_edit1)
        new_edit1.add_command(label='Delete Transaction', command=self.delete_data)

        # Configure the root object for the Application
        self.root2.title("Transactions List")
        self.root2.grid_rowconfigure(0, weight=1)
        self.root2.grid_columnconfigure(7, weight=1)
        self.root2.config(background="lightblue")
        self.root2.resizable(0,0)
        # this creates other windows. Need something better.
        #self.root2.eval('tk::PlaceWindow . center')

        # Set the treeview
        self.tree = ttk.Treeview(self.root2, columns=('TransId', 'Date','ReferenceID','Reference','Debit','Credit','Balance'))

        # Set the heading (Attribute Names)
        self.tree.heading('#1', text='TransId')
        self.tree.heading('#2', text='Date')
        self.tree.heading('#3', text='ReferenceID')
        self.tree.heading('#4', text='Reference')
        self.tree.heading('#5', text='Debit')
        self.tree.heading('#6', text='Credit')
        self.tree.heading('#7', text='Balance')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#1', width=100, stretch=tk.NO)
        self.tree.column('#2', width=200, stretch=tk.NO)
        self.tree.column('#3', width=100, stretch=tk.NO)
        self.tree.column('#4', width=200, stretch=tk.NO)
        self.tree.column('#5', width=100, stretch=tk.NO)
        self.tree.column('#6', width=100, stretch=tk.NO)
        self.tree.column('#7', width=100, stretch=tk.NO)

        self.tree.column("#0", width=0)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

        #self.gettransdata()


    def gettransdata(self,passedidnumber):
        for i in self.tree.get_children():
            self.tree.delete(i)
        mydb = database.connect_db()
        my_conn = mydb.cursor()
        database.connect_selecttransactions(my_conn,passedidnumber)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)

    def delete_data(self):
        row_id = self.tree.focus()
        row_id = self.tree.item(row_id)['values'][0]

        mydb = database.connect_db()
        mycursor = mydb.cursor()
        id = (row_id, )
        database.connect_deletetransaction(mycursor,id)
        mydb.commit()

        ## refresh table
        for i in self.tree.get_children():
            self.tree.delete(i)
        my_conn = mydb.cursor()
        database.connect_getalltransactions(my_conn)
        rows = my_conn.fetchall()
        for transactions in rows:
            self.treeview.insert('', 'end', values=transactions)

    def insert_data(self):
        mydb = database.connect_db()
        my_conn = mydb.cursor()
        ## refresh table
        for i in self.tree.get_children():
            self.tree.delete(i)
        database.connect_getalltransactions(my_conn)
        rows = my_conn.fetchall()
        for transactions in rows:
            self.treeview.insert('', 'end', values=transactions )


#transform = TransactionsForm(tk.Tk())
#transform.root2.mainloop()
