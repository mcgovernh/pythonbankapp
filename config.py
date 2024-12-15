import mysql.connector
from tkinter import *
import ctypes  # An included library with Python install.
# Use config file to share variables across the project
class student:
    id =""
    firstname =""
    lastname =""
    address =""
    balance =""
    wbalance =""
    tbalance =""
    destid = ""

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class myClass:
	def __init__(self,val):
		self.val=val
	def getVal(self):
		return self.val

class database:
    def connect_db():
        #print ("connected to mySQL dbase")
        return mysql.connector.connect(host="localhost",user="root",password="",database="python_mysql")

    def connect_getstudent(my_conn):
        my_conn.execute("SELECT * FROM students")

    def connect_deletestudent(my_conn,id):
        my_conn.execute("DELETE FROM students WHERE ID = %s",id)
        #print(my_conn.rowcount,"record(s) deleted")

    def connect_selectstudent(my_conn,id):
        my_conn.execute('SELECT * FROM students WHERE ID = %s',id)

    def connect_updatestudent(cursor, firstname, lastname, address, balance):
        cursor.execute('INSERT INTO Students (firstname, lastname, address, balance) VALUES (%s,%s,%s,%s) ' , (firstname,lastname,address,balance))
        #Mbox('Alert', '{} {} inserted into Student table'.format(firstname,lastname), 1)
        #print(cursor.rowcount, "record for {} {} inserted successfully to Student table".format(firstname,lastname))

    def connect_updateeditstudent(cursor, firstname, lastname, address, balance,id):
        cursor.execute('UPDATE Students '
                       'SET firstname=%s, lastname=%s, address=%s, balance=%s'
                       'WHERE ID = %s ',
                        (firstname,lastname,address,balance,id))
        #Mbox('Alert', '{} {} updated into Student table'.format(firstname,lastname), 1)
        #print(cursor.rowcount, "record for {} {} edited successfully in Student table".format(firstname,lastname))

    def updatebalance(cursor, balance,id):
        cursor.execute('UPDATE Students '
                       'SET balance=%s'
                       'WHERE ID = %s ',
                        (balance,id))

    def updatetransactions(cursor, referenceID, reference, debit, credit, balance):
        cursor.execute('INSERT INTO transactions (referenceID, reference, debit, credit, balance) VALUES (%s,%s,%s,%s,%s) ' , (referenceID, reference,debit,credit,balance))

    def connect_selecttransactions(my_conn,id):
        my_conn.execute('SELECT * FROM transactions WHERE ReferenceID = %s',id)

    def connect_getalltransactions(my_conn):
        my_conn.execute("SELECT * FROM transactions")

    def connect_deletetransaction(my_conn,id):
        my_conn.execute("DELETE FROM transactions WHERE TransID = %s",id)
