import sqlite3

mycon = sqlite3.connect('C:\\jba\\workspaces\\default\\Demo\\newdb.db')

cr= mycon.cursor()
#cr.execute('Create table student (id INTEGER, name TEXT)')

#cr.execute('insert into student values (101, "Ankur")')
#mycon.execute('insert into student values (101, "Ankur")')

cr.execute('select * from student')

#for one record
#print(cr.fetchone())

#for all records
records = cr.fetchall()

for val in records:
    print(val[0], val[1])

