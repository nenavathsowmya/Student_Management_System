import mysql.connector
from tkinter import*
import tkinter.messagebox  
import random
import Std_info_BackEnd
from tkinter import ttk
from tkinter import messagebox
#import numpy as np


def connect():
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()
       cur.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name text, fname text, mname text, \
                     address text, mobno integer,email text, dob integer, gender text)")
       conn.commit()
       conn.close()

def insert(name , fname , mname , address , mobno , email , dob , gender ):
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()
       #cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)", (name, fname, mname, address , mobno, email, dob, gender))
       #id = random.randint(1,10000)
       cur.execute(f"INSERT INTO student Values (id,'{name}', '{fname}', '{mname}', '{address}', {mobno}, '{email}', {dob}, '{gender}')")
       conn.commit()
       conn.close()
                                                                        

def view():
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()
       cur.execute("SELECT * FROM student")
       rows = cur.fetchall()
       return rows
       conn.close()

def delete(id):
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()
       cur.execute(f"DELETE FROM student WHERE id = {id}")
       conn.commit()
       conn.close()

def update(id, name , fname , mname , address , mobno , email , dob , gender):
       #messagebox.showinfo("name", id)
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()   
       query = "update student set "
       if name:
                query+= f"name = '{name}',"
       if fname:
                query+= f"fname = '{fname}',"
       if mname:
                query+= f"mname = '{mname}',"
       if address:
                query+= f"address = '{address}',"
       if mobno:
                query+= f"mobno = {mobno},"
       if email:
                query+= f"email = '{email}',"
       if dob:
                query+= f"dob = '{dob}',"
       if gender:
                query+= f"gender = '{gender}',"
                         
                
       query = query.rstrip(", ")
       query += f" WHERE id = {id};"
       cur.execute(query)
       #cur.execute(f"UPDATE student SET name = '{name}' OR fname = '{fname}' OR mname = '{mname}' OR address = '{address}' OR mobno = {mobno} OR email = '{email}' OR dob = '{dob}' OR gender = '{gender}' where id = {id}")
       conn.commit()
       conn.close()

def search(name , fname , mname , address , mobno , email , dob , gender):
       conn = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = conn.cursor()
       cur.execute(f"select * from student where name = '{name}' OR fname = '{fname}' OR mname = '{mname}' OR address = '{address}' OR mobno = '{mobno}' OR email = '{email}' OR dob = '{dob}' OR gender = '{gender}' ")
       rows = cur.fetchall()
       return rows    
       conn.close()

                                                               
connect()
       
