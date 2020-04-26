import sqlite3

def EmployeeData():
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Employee(id INTEGER PRIMARY KEY,  Reference text,FirstName text,Surname text,Address text,Gender text,Mobile text,NINumber text,stdLoan text,Tax text,Pension text,Deductions text,Netpay text,Grosspay text)")
	con.commit()
	con.close()




def AddEmployeeRec(Reference ,FirstName ,Surname ,Address ,Gender ,Mobile ,NINumber ,stdLoan ,Tax ,Pension ,Deductions ,Netpay,Grosspay):
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("INSERT INTO Employee VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)", (Reference ,FirstName ,Surname ,Address ,Gender ,Mobile ,NINumber ,stdLoan ,Tax ,Pension ,Deductions ,Netpay,Grosspay))
	con.commit()
	con.close()

def Viewdata():
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Employee")
	rows= cur.fetchall()
	con.close()
	return rows


def DeleteRec():
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("DELETE * FROM Employee WHERE id=?", (id,))
	con.commit()
	con.close()

def SearchData(Reference="",FirstName="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",Netpay="",Grosspay=""):
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Employee WHERE Reference=? OR FirstName=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deductions=? OR Netpay=? OR Grosspay=?", (Reference ,FirstName ,Surname ,Address ,Gender ,Mobile ,NINumber ,stdLoan ,Tax ,Pension ,Deductions ,Netpay,Grosspay))
	rows= cur.fetchall()
	con.close()
	return rows

def UpdateData(Reference="",FirstName="",Surname="",Address="",Gender="",Mobile="",NINumber="",stdLoan="",Tax="",Pension="",Deductions="",Netpay="",Grosspay=""):
	con = sqlite3.connect("Employee.db")
	cur = con.cursor()
	cur.execute("UPDATE Employee SET Reference=? OR FirstName=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? OR NINumber=? OR stdLoan=? OR Tax=? OR Pension=? OR Deductions=? OR Netpay=? OR Grosspay=?", (Reference ,FirstName ,Surname ,Address ,Gender ,Mobile ,NINumber ,stdLoan ,Tax ,Pension ,Deductions ,Netpay,Grosspay,id))
	con.commit()
	con.close()


EmployeeData() 
