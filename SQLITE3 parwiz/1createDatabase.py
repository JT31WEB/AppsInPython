#==============1ST SCRIPT=================================
import sqlite3 as lit

def main():

	try:
		db = lit.connect('employee.db')
		print('Database created successfully')

	except:
		print('failed to create Database')


	finally:
		db.close()


if __name__ == "__main__":
	main()



