import sqlite3

connection = sqlite3.connect('example.db')


cursor = connetction.cursor('''
CREATE TABLE IF NOT EXISTS employeees(

   id Integer primary key autoincrement ,
   name text not null ,
   position text not null ,
   depertament text not null,
   salary real
   )
''')


connection.commit()
