import sqlite3

mycon = sqlite3.connect('C:\\jba\\workspaces\\default\\Demo\\newdb.db')

cr= mycon.cursor()

#cr.execute('update student set name="ABC" where id = 101')
#cr.execute('delete from student where id = 101')

# for mysql you have to use %s instead of ?
cr.execute('insert into student values (?,?)', (501, 'Anil'))

mycon.commit()