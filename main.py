import sqlite3


na = input('Enter 1 for create\nEnter 2 for delete\nEnter 0 for check\n')
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE productss (name TEXT, price TEXT, number TEXT)')
#connection.commit()

def pe():
      global n0
      global n1
      global n2
      global no
      if na =='1':
            n0 = input('Enter name')
            n1 = int(input('Enter price'))
            n2 = int(input('Enter number'))
            print('GG')
            cur.execute(f'INSERT INTO productss (name, price, number) VALUES ("{n0}" , "{n1}" , "{n2}")')
            connection.commit()
      if na =='2':
            no = input('Enter row id')
            cur.execute(f'DELETE FROM productss WHERE rowid = {no}')
            connection.commit()
      if na == '0':
            print(res)

cur.execute('SELECT rowid, name, price, number FROM productss')
connection.commit()
res = cur.fetchall()
pe()

connection.close()