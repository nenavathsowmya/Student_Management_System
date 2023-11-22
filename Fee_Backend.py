import mysql.connector
import random

def connect():
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INT AUTO_INCREMENT PRIMARY KEY, recpt integer, name text, admsn text, date integer, \
                    branch text, sem text, total integer, paid integer, due integer)')

       con.commit()
       con.close()

def insert(recpt, name, admsn , date ,  branch , sem , total, paid , due):
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()
       #id = random.randint(1,10000)
       #print(id)
       cur.execute(f"INSERT INTO fee VALUES (id,{recpt},'{name}','{admsn}','{date}','{branch}','{sem}', {total} ,{paid},{due})")             
       con.commit()
       con.close()

def view():
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()
       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row
       con.commit()
       

def delete(id):
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()
       cur.execute(f"DELETE FROM fee WHERE id ={id}")
       con.commit()
       con.close()

def update(id,recpt, name, admsn, date, branch, sem, total, paid, due):
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()
       query = "update fee set "
       if recpt:
                query+= f"recpt = {recpt},"
       if name:
                query+= f"name = '{name}',"
       if admsn:
                query+= f"admsn = '{admsn}',"
       if date:
                query+= f"date = '{date}',"
       if branch:
                query+= f"branch = '{branch}',"
       if sem:
                query+= f"sem = '{sem}',"
       if total:
                query+= f"total = {total},"
       if paid:
                query+= f"paid = {paid},"
       if due:
                query+= f"due = {due},"
       query = query.rstrip(", ")
       query += f" WHERE id = {id};" 
       cur.execute(query)
       print(query)                 
       con.commit()
       con.close()

def search(recpt, name, admsn, date, branch, sem):
       con = mysql.connector.connect(user='root', password ='', host='127.0.0.1', database='project')
       cur = con.cursor()
       cur.execute(f"SELECT * FROM fee WHERE  recpt = '{recpt}' OR name = '{name}' OR admsn ='{admsn}' OR branch = '{branch}'OR sem = '{sem}'")
       row = cur.fetchall()
       return row
       #con.commit()
       
connect()


