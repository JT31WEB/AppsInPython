#==============3RD SCRIPT=================================
import sqlite3 as lit

MyUsers = {
	
	(1, 'THAPELO', 'TJSEPALE@gmail.com'),
	(2, 'DUNCAN', 'DUNCAN@gmail.com'),
	(3, 'HENRY', 'HENRY@gmail.com'),
	(4, 'FEZZIE', 'FEZZIE@gmail.com')
}

db = lit.connect('employee.db')

with db:
	cur = db.cursor()
	cur.executemany('INSERT INTO users VALUES (?,?,?)', MyUsers)


	print("Data inserted successfully")


