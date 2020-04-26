from tkinter import *
import sqlite3


root = Tk()
root.title("SQLite3 Database Management System")
root.geometry('400x800')


#CREATE OR CONNECT TO DATABASE================================================
conn = sqlite3.connect('address_book.db')

#CREATE CURSOR FOR DATABASE============================================================
c = conn.cursor()


#==========FUNCTIONS=====================================================================
def Reset():  #clear Entry inputs
	txtfirst_name.delete(0, END)
	txtlast_name.delete(0, END)
	txtaddress.delete(0, END)
	txtcity.delete(0, END)
	txtState.delete(0, END)
	txtZipcode.delete(0, END)

def Edit():
	editor = Tk()
	editor.title("Edit Database Record")
	editor.geometry('400x400')

	

	#============DB FUNCTION=================================================================
	conn = sqlite3.connect('address_book.db') #connect to DB
	c = conn.cursor()   #activate cursor
	record_id = txt_delete.get()
	c.execute("SELECT *,oid FROM addresses WHERE oid=" + record_id)
	records= c.fetchall()

	global txtfirst_nameE
	global txtlast_nameE
	global txtaddressE
	global txtcityE
	global txtStateE
	global txtZipcodeE
	

	def Update():
		conn = sqlite3.connect('address_book.db') #connect to DB
		c = conn.cursor()   #activate cursor
		record_id = txt_delete.get()
		c.execute("""UPDATE addresses SET
			first_name= :first_name,
			last_name= :last_name,
			address= :address,
			city= :city,
			state= :state,
			zipcode= :zipcode
			WHERE oid= :oid""",
			{
			'first_name': txtfirst_nameE.get(),
			'last_name':txtlast_nameE.get(),
			'address':txtaddressE.get(),
			'city':txtcityE.get(),
			'state':txtStateE.get(),
			'zipcode': txtZipcodeE.get(),
			'oid': record_id
			})
		conn.commit()     
		conn.close()
		Query()
		editor.destroy()

	#===================WIDGETS================================================================
	lblfirst_nameE = Label(editor, text="Firstname", font=('arial', 12, 'bold'), pady=10, padx=20)
	lblfirst_nameE.grid(row=0, column=0)
	txtfirst_nameE = Entry(editor, width=30)
	txtfirst_nameE.grid(row=0, column=1)

	lbllast_nameE = Label(editor, text="Lastname", font=('arial', 12, 'bold'), pady=10, padx=20)
	lbllast_nameE.grid(row=1, column=0)
	txtlast_nameE = Entry(editor, width=30)
	txtlast_nameE.grid(row=1, column=1)

	lbladdressE = Label(editor, text="address", font=('arial', 12, 'bold'), pady=10, padx=20)
	lbladdressE.grid(row=2, column=0)
	txtaddressE = Entry(editor, width=30)
	txtaddressE.grid(row=2, column=1)

	lblcityE = Label(editor, text="City", font=('arial', 12, 'bold'), pady=10, padx=20)
	lblcityE.grid(row=3, column=0)
	txtcityE = Entry(editor, width=30)
	txtcityE.grid(row=3, column=1)

	lblstateE = Label(editor, text="State", font=('arial', 12, 'bold'), pady=10, padx=20)
	lblstateE.grid(row=4, column=0)
	txtStateE = Entry(editor, width=30)
	txtStateE.grid(row=4, column=1)

	lblZipcodeE = Label(editor, text="Zipcode", font=('arial', 12, 'bold'), pady=10, padx=20)
	lblZipcodeE.grid(row=5, column=0)
	txtZipcodeE = Entry(editor, width=30)
	txtZipcodeE.grid(row=5, column=1)

	Save_btnE = Button(editor, font=('arial', 10, 'bold'), text="Save Record in Database", command=Update)
	Save_btnE.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

	for record in records:
		txtfirst_nameE.insert(0, record[0])
		txtlast_nameE.insert(0, record[1])
		txtaddressE.insert(0, record[2])
		txtcityE.insert(0, record[3])
		txtStateE.insert(0, record[4])
		txtZipcodeE.insert(0, record[5])

	

def Delete():
	conn = sqlite3.connect('address_book.db') #connect to DB
	c = conn.cursor()   
	c.execute("DELETE FROM addresses WHERE oid= " + txt_delete.get())
	txt_delete.delete(0, END)
	conn.commit()     
	conn.close()
	Query()

def Submit():
	if (txtfirst_name.get() != ""):
		conn = sqlite3.connect('address_book.db') #connect to DB
		c = conn.cursor()   #activate cursor
		c.execute("INSERT INTO addresses VALUES(:first_name, :last_name, :address, :city, :state, :zipcode)", 
		{
		'first_name': txtfirst_name.get(),
		'last_name':txtlast_name.get(),
		'address':txtaddress.get(),
		'city':txtcity.get(),
		'state':txtState.get(),
		'zipcode': txtZipcode.get()
		})
		conn.commit()     #save Changes
		conn.close()    #close connection
		lblSub = Label(root, text="Info Submitted", font=('arial', 12, 'bold'), pady=10, padx=20)
		lblSub.grid(row=20, column=0)
		Reset()

def Query():
	conn = sqlite3.connect('address_book.db') #connect to DB
	c = conn.cursor()   #activate cursor
	c.execute("SELECT *, oid FROM addresses",)
	records= c.fetchall()
	#print(records)
	print_records = ""    #holder Var
	for record in records:
		print_records += str(record[0])+ "  " + str(record[1])+ "  " + str(record[2])+ "  " + str(record[3])+ "  " + str(record[4])+ "  " + str(record[5])+ "\t" + str(record[6]) + "\n" 
	lblQuery = Label(root, justify=LEFT, text=print_records, font=('arial', 12, 'bold'), pady=10, padx=20)
	lblQuery.grid(row=15, column=0, columnspan=2)

	conn.commit()     #save Changes
	conn.close()   



#CREATE TABLE Func=============================================================================
def start():
	c.execute("""CREATE TABLE IF NOT EXISTS addresses(
	first_name text,
	last_name text,
	address text,
	city text,
	state text,
	zipcode integer)
	""") 

start()

#INPUT FIELDS MAIN============================================================================
lblfirst_name = Label(root, text="Firstname", font=('arial', 12, 'bold'), pady=10, padx=20)
lblfirst_name.grid(row=0, column=0)
txtfirst_name = Entry(root, width=30)
txtfirst_name.grid(row=0, column=1)

lbllast_name = Label(root, text="Lastname", font=('arial', 12, 'bold'), pady=10, padx=20)
lbllast_name.grid(row=1, column=0)
txtlast_name = Entry(root, width=30)
txtlast_name.grid(row=1, column=1)

lbladdress = Label(root, text="address", font=('arial', 12, 'bold'), pady=10, padx=20)
lbladdress.grid(row=2, column=0)
txtaddress = Entry(root, width=30)
txtaddress.grid(row=2, column=1)

lblcity = Label(root, text="City", font=('arial', 12, 'bold'), pady=10, padx=20)
lblcity.grid(row=3, column=0)
txtcity = Entry(root, width=30)
txtcity.grid(row=3, column=1)

lblstate = Label(root, text="State", font=('arial', 12, 'bold'), pady=10, padx=20)
lblstate.grid(row=4, column=0)
txtState = Entry(root, width=30)
txtState.grid(row=4, column=1)

lblZipcode = Label(root, text="Zipcode", font=('arial', 12, 'bold'), pady=10, padx=20)
lblZipcode.grid(row=5, column=0)
txtZipcode = Entry(root, width=30)
txtZipcode.grid(row=5, column=1)

lbl_delete = Label(root, text="Select ID:", font=('arial', 12, 'bold'), pady=10, padx=20)
lbl_delete.grid(row=8, column=0)
txt_delete = Entry(root, width=30)
txt_delete.grid(row=8, column=1)

#SUBMIT BUTTON====================================================================
sbt_btn = Button(root, font=('arial', 10, 'bold'), text="Add Record To Database", command=Submit)
sbt_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
qry_btn = Button(root, font=('arial', 10, 'bold'), text="Show Record in Database", command=Query)
qry_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
dlt_btn = Button(root, font=('arial', 10, 'bold'), text="Delete Record in Database", command=Delete)
dlt_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
Edt_btn = Button(root, font=('arial', 10, 'bold'), text="Edit Record in Database", command=Edit)
Edt_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)






#COMMIT CHANGES
conn.commit()



#CLOSE CONNECTION
conn.close()




root.mainloop()




