from tkinter import *
import sqlite3


root = Tk()
root.title("VIP Contacts DB System")
root.geometry('490x550+0+0')
root.config(background='beige')


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
		Query()
		Reset()

def Query():
	VIP.delete(0, END)
	conn = sqlite3.connect('address_book.db') #connect to DB
	c = conn.cursor()   #activate cursor
	c.execute("SELECT *, oid FROM addresses",)
	records= c.fetchall()
	print_records = ""    #holder Var
	for record in records:
		#print_records = str(record[0])+ "__" + str(record[1])+ "  *   " + str(record[2])+ "   *   " + str(record[3])+ "   *   " + str(record[4])+ "   *   " + str(record[5])+ "   *   " + str(record[6]) + "\n"
		VIP.insert(END, record)
	conn.commit()     #save Changes
	conn.close()   


def contactRec(event):
			SearchEd = VIP.curselection()[0]
			Ed = VIP.get(SearchEd)

			txtfirst_name.delete(0, END)
			txtfirst_name.insert(END, Ed[0])
			txtlast_name.delete(0, END)
			txtlast_name.insert(END, Ed[1])
			txtaddress.delete(0, END)
			txtaddress.insert(END, Ed[2])
			txtcity.delete(0, END)
			txtcity.insert(END, Ed[3])
			txtState.delete(0, END)
			txtState.insert(END, Ed[4])
			txtZipcode.delete(0, END)
			txtZipcode.insert(END, Ed[5])

			txt_delete.delete(0, END)
			txt_delete.insert(END, Ed[6])

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
			'first_name': txtfirst_name.get(),
			'last_name':txtlast_name.get(),
			'address':txtaddress.get(),
			'city':txtcity.get(),
			'state':txtState.get(),
			'zipcode': txtZipcode.get(),
			'oid': record_id
			})
		conn.commit()     
		conn.close()
		Query()
	




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
lblTitle = Label(root, text="CONTACTS DATABASE", bg='gold', font=('arial', 20, 'bold'), padx=90)
lblTitle.grid(row=0, column=0, sticky=W)

#========================================================================================================
DisplayFrame = Frame(root, bd=1, bg='blue', relief=RIDGE)
DisplayFrame.grid(row=1, column=0,sticky= W)

lblLabel = Label(DisplayFrame, bg='blue', fg='white', text="Firstname\tLastname\tAddress\tCity\tState\tZipcode", font=('arial', 10, 'bold'), pady=2,padx=8)
lblLabel.grid(row=0, column=0, columnspan=6, sticky=W)

scrollbar = Scrollbar(DisplayFrame, bg='blue')
scrollbar.grid(row=1, column=1, sticky="ns")

VIP = Listbox(DisplayFrame, width=50, height=8, bd=10,  font=('arial', 12, 'bold'), bg="powder blue", fg="black", yscrollcommand=scrollbar.set)
VIP.bind("<<ListboxSelect>>", contactRec)
VIP.grid(row=1, column=0, sticky='nsew')
scrollbar.config(command=VIP.xview)

#========================================================================================================
InputFrame = Frame(root, width= 400, background='beige')
InputFrame.grid(row=2, column=0, padx= 50, sticky= W)

lblfirst_name = Label(InputFrame, text="Firstname", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lblfirst_name.grid(row=0, column=0)
txtfirst_name = Entry(InputFrame, width=30)
txtfirst_name.grid(row=0, column=1)

lbllast_name = Label(InputFrame, text="Lastname", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lbllast_name.grid(row=1, column=0)
txtlast_name = Entry(InputFrame, width=30)
txtlast_name.grid(row=1, column=1)

lbladdress = Label(InputFrame, text="Address", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lbladdress.grid(row=2, column=0)
txtaddress = Entry(InputFrame, width=30)
txtaddress.grid(row=2, column=1)

lblcity = Label(InputFrame, text="City", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lblcity.grid(row=3, column=0)
txtcity = Entry(InputFrame, width=30)
txtcity.grid(row=3, column=1)

lblstate = Label(InputFrame, text="State", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lblstate.grid(row=4, column=0)
txtState = Entry(InputFrame, width=30)
txtState.grid(row=4, column=1)

lblZipcode = Label(InputFrame, text="Zipcode", font=('arial', 12, 'bold'), pady=5, padx= 8, background='beige')
lblZipcode.grid(row=5, column=0)
txtZipcode = Entry(InputFrame, width=30)
txtZipcode.grid(row=5, column=1)

#SUBMIT BUTTON====================================================================
qry_btn = Button(InputFrame, font=('arial', 10, 'bold'), width=20, text="Show Records in Database", bg='yellow', fg='black', command=Query)
qry_btn.grid(row=6, column=0, columnspan=1, pady=5, padx=15)
sbt_btn = Button(InputFrame, font=('arial', 10, 'bold'), width=20, text="Add Record To Database", bg='green', fg='white', command=Submit)
sbt_btn.grid(row=6, column=1, columnspan=1, pady=5, padx=15)

lbl_delete = Label(InputFrame, bg='beige', text="Record ID:", font=('arial', 12, 'bold'), pady=5)
lbl_delete.grid(row=7, column=0)
txt_delete = Entry(InputFrame, width=10)
txt_delete.grid(row=7, column=1)

Edt_btn = Button(InputFrame, font=('arial', 10, 'bold'), width=20, text="Update Record", bg='cadet blue', fg='black', command=Update)
Edt_btn.grid(row=8, column=0, pady=5)
dlt_btn = Button(InputFrame, font=('arial', 10, 'bold'), width=20, text="Delete Record", bg='red', fg='white', command=Delete)
dlt_btn.grid(row=8, column=1, columnspan=1, pady=5)

#COMMIT CHANGES
conn.commit()



#CLOSE CONNECTION
conn.close()




root.mainloop()




