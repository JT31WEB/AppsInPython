import sqlite3 as lit

db = lit.connect('employee.db')

with db:
	user_id = 1

	cur = db.cursor()
	cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
	db.commit()

	print('DATA DELETED SUCCESSFULLY')