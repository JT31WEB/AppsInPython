from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
from datetime import datetime, date, timedelta
import random, time, tempfile, os
import EmployeeDatabase


class Employee:
	def __init__(self, root):
		self.root = root
		self.root.title("Employee Database Management System")
		self.root.geometry('1350x750+0+0')
		self.root.config(background="gainsboro")

		#=============FRAMES==========================================================================
		MainFrame =Frame(self.root, width=1350, bd=6, height=700, relief=RAISED)
		MainFrame.grid()

		TopFrame1 = Frame(MainFrame, width=1310, height=50,bd=1, relief=RIDGE)
		TopFrame1.grid(row=2, column=0,sticky= W)

		TopFrame2 = Frame(MainFrame, width=1310, height=100,bd=1, relief=RAISED)
		TopFrame2.grid(row=1, column=0,sticky= W)

		TopFrame3 = Frame(MainFrame, width=1340, height=500,bd=1, relief=RAISED)
		TopFrame3.grid(row=0, column=0,sticky= W)

		LeftFrame = Frame(TopFrame3, width=1340, height=400,bd=1, relief=RIDGE)
		LeftFrame.grid(row=0, column=0,sticky= W)
		LeftFrame1 = Frame(LeftFrame, width=600, height=180,bd=1, relief=RIDGE)
		LeftFrame1.grid(row=0, column=0,sticky= W)

		LeftFrame2 = Frame(LeftFrame, width=600, height=180,bd=1, relief=RIDGE)
		LeftFrame2.grid(row=1, column=0,sticky= W)
		LeftFrame2Left = Frame(LeftFrame2, width=300, height=170,bd=1, relief=RIDGE)
		LeftFrame2Left.grid(row=0, column=0,sticky= W)
		LeftFrame2Right = Frame(LeftFrame2, width=300, height=170,bd=1, relief=RIDGE)
		LeftFrame2Right.grid(row=0, column=1,sticky= W)

		RightFrame1 = Frame(TopFrame3, width=320, height=400,bd=1, relief=RIDGE)
		RightFrame1.grid(row=0, column=1,sticky= W)
		RightFrame1a = Frame(RightFrame1, width=310, height=300,bd=1, relief=RIDGE)
		RightFrame1a.grid(row=0, column=1,sticky= W)

		RightFrame2 = Frame(RightFrame1, width=300, height=400,bd=1, relief=RIDGE)
		RightFrame2.grid(row=0, column=0,sticky= W)
		RightFrame2a = Frame(RightFrame2, width=280, height=50,bd=1, relief=RIDGE)
		RightFrame2a.grid(row=0, column=0,sticky= W)
		RightFrame2b = Frame(RightFrame2, width=280, height=200,bd=1, relief=RIDGE)
		RightFrame2b.grid(row=1, column=0,sticky= W)
		RightFrame2c = Frame(RightFrame2, width=280, height=100,bd=1, relief=RIDGE)
		RightFrame2c.grid(row=2, column=0,sticky= W)
		RightFrame2d = Frame(RightFrame2, width=280, height=50,bd=1, relief=RIDGE)
		RightFrame2d.grid(row=3, column=0,sticky= W)

		#==============VARIABLES===========================================================================================
		global Ed
		FirstName = StringVar()
		Surname = StringVar()
		Address = StringVar()
		Reference = StringVar()
		CityWeighting = IntVar()
		Mobile = StringVar()
		BasicSalary = IntVar()
		Overtime = StringVar()
		Grosspay = StringVar()
		Netpay = StringVar()
		Tax = StringVar()
		Pension = StringVar()
		stdLoan = StringVar()
		NIPayment = StringVar()
		Deductions = StringVar()
		Gender = StringVar()
		Payday = StringVar()
		TaxPeriod = StringVar()
		NINumber = StringVar()
		NICode = StringVar()
		TaxablePay = StringVar()
		Pensionablepay = StringVar()
		OtherPaymentDue = StringVar()
		TaxCode = StringVar()

		BasicSalary.set("")
		CityWeighting.set("")
		OtherPaymentDue.set("0.00")
		#==============FUNCTIONS===========================================================================================
		def iExit():
			qExit = messagebox.askyesno("Library DataBase System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

		def Reset ():
			FirstName.set("")
			Surname.set("")
			Address.set("")
			Reference.set("")
			CityWeighting.set("")
			Mobile.set("")
			BasicSalary.set("")
			Overtime.set("")
			Grosspay.set("")
			Netpay.set("")
			Tax.set("")
			Pension.set("")
			stdLoan.set("")
			NIPayment.set("")
			Deductions.set("")
			Gender.set("")
			Payday.set("")
			TaxPeriod.set("")
			NINumber.set("")
			NICode.set("")
			TaxablePay.set("")
			Pensionablepay.set("")
			OtherPaymentDue.set("")
			TaxCode.set("")

			BasicSalary.set("")
			CityWeighting.set("")
			OtherPaymentDue.set("0.00")
			self.txtReceipt.delete("1.0", END)

		def iPrint():
			q= self.txtReceipt.get("1.0", "end-1c")
			filename = tempfile.mktemp(".txt")
			open (filename, "w"). write(q)
			os.startfile(filename, "print")

		def addData():
			if (len(Reference.get()) !=0):
				EmployeeDatabase.AddEmployeeRec(Reference.get(),FirstName.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),Netpay.get(),Grosspay.get())
				lstEmployee.delete(0, END)
				lstEmployee.insert(END,(Reference.get(),FirstName.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),Netpay.get(),Grosspay.get()))

		def DisplayData():
			lstEmployee.delete(0, END)
			for row in EmployeeDatabase.Viewdata():
				lstEmployee.insert(END, row, str(""))

		def EmployeeRec(event):
			global Ed
			SearchEd = lstEmployee.curselection()[0]
			Ed = lstEmployee.get(SearchEd)

			self.txtReference.delete(0, END)
			self.txtReference.insert(END, Ed[1])
			self.txtFirstName.delete(0, END)
			self.txtFirstName.insert(END, Ed[2])
			self.txtSurname.delete(0, END)
			self.txtSurname.insert(END, Ed[3])
			self.txtAddress.delete(0, END)
			self.txtAddress.insert(END, Ed[4])
			self.txtGender.delete(0, END)
			self.txtGender.insert(END, Ed[5])
			self.txtMobile.delete(0, END)
			self.txtMobile.insert(END, Ed[6])
			self.txtNINumber.delete(0, END)
			self.txtNINumber.insert(END, Ed[7])
			self.txtstdLoan.delete(0, END)
			self.txtstdLoan.insert(END, Ed[8])
			self.txtTax.delete(0, END)
			self.txtTax.insert(END, Ed[9])
			self.txtPension.delete(0, END)
			self.txtPension.insert(END, Ed[10])
			self.txtDeductions.delete(0, END)
			self.txtDeductions.insert(END, Ed[11])
			self.txtNetpay.delete(0, END)
			self.txtNetpay.insert(END, Ed[12])
			self.txtGrosspay.delete(0, END)
			self.txtGrosspay.insert(END, Ed[13])

		def deleteData():
			if (len(Reference.get()) !=0):
				EmployeeDatabase.DeleteRec(Ed[0])
				Reset()
				DisplayData()

		def searchData():
			lstEmployee.delete(0, END)
			for row in EmployeeDatabase.SearchData(Reference.get(),FirstName.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),Netpay.get(),Grosspay.get()):
				lstEmployee.insert(END, row, str(""))

		def Update():
			if (len(Reference.get()) !=0):
				EmployeeDatabase.DeleteRec(Ed[0])
			if (len(Reference.get()) !=0):
				EmployeeDatabase.AddEmployeeRec(Reference.get(),FirstName.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),Netpay.get(),Grosspay.get())
				lstEmployee.delete(0, END)
				lstEmployee.insert(END, (Reference.get(),FirstName.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),NINumber.get(),stdLoan.get(),Tax.get(),Pension.get(),Deductions.get(),Netpay.get(),Grosspay.get()))

		def PayRef():
			Payday.set(time.strftime("%d/%m/%Y"))
			refpay = random.randint(160000, 700000)
			refpaid = ("Ref" + str(refpay))
			Reference.set(refpaid)

			NIpay = random.randint(34051, 409705)
			NIpaid = ("NI" + str(NIpay))
			NINumber.set(NIpay)

			iDate = datetime.now()
			TaxPeriod.set(iDate.month)

			Ncode = random.randint(1299, 15705)
			CodeNI = ("NI" + str(Ncode))
			NICode.set(CodeNI)

			iTaxCode = random.randint(7509, 15785)
			paymentTaxCode = ("TCode" + str(iTaxCode))
			NICode.set(paymentTaxCode)

		def monthlySalary():
			PayRef()

			BS= float(BasicSalary.get())
			CW= float(CityWeighting.get())
			OT= float(Overtime.get())
			OTD= float(OtherPaymentDue.get())

			MTax = ((BS + CW + OT + OTD) *0.3)
			TTax = "R", str('%.2f'%(MTax))
			Tax.set(TTax)

			MPension = ((BS + CW + OT + OTD) *0.2)
			MmPension = "R", str('%.2f'%(MPension))
			Pension.set(MmPension)

			MStdLoan = ((BS + CW + OT + OTD) *0.012)
			MmStdLoan = "R", str('%.2f'%(MStdLoan))
			stdLoan.set(MmStdLoan)

			M_NIpayment = ((BS + CW + OT + OTD) *0.011)
			Mm_NIpayment = "R", str('%.2f'%(M_NIpayment))
			NIPayment.set(Mm_NIpayment)

			deduct = (MTax +MPension +MStdLoan +M_NIpayment)
			deduct_payM =  "R", str('%.2f'%(deduct))
			Deductions.set(deduct_payM)
			Gross_pay =  "R", ('%.2f'%(BS + CW + OT + OTD))
			Grosspay.set(Gross_pay)

			NetPayAfter = (BS + CW + OT + OTD) - deduct
			Netafter = "R", str('%.2f'%(NetPayAfter))
			Netpay.set(Netafter)

			TaxablePay.set(TTax)
			Pensionablepay.set(MmPension)

			self.txtReceipt.insert(END, '\t\tMonthly Pay Slip\n\n')
			self.txtReceipt.insert(END, 'Reference: \t\t' + Reference.get() + "\n")
			self.txtReceipt.insert(END, 'Reference: \t\t' + Payday.get() + "\n")
			self.txtReceipt.insert(END, 'Surname: \t\t' + Surname.get() + "\n")
			self.txtReceipt.insert(END, 'Firstname: \t\t' + FirstName.get() + "\n")
			self.txtReceipt.insert(END, 'Tax: \t\t' + Tax.get() + "\n")
			self.txtReceipt.insert(END, 'Pension: \t\t' + Pension.get() + "\n")
			self.txtReceipt.insert(END, 'Student Loan: \t\t' + stdLoan.get() + "\n")
			self.txtReceipt.insert(END, 'NI Number: \t\t' + NINumber.get() + "\n")
			self.txtReceipt.insert(END, 'NI Payment: \t\t' + NIPayment.get() + "\n")
			self.txtReceipt.insert(END, 'Deductions: \t\t' + Deductions.get() + "\n")
			self.txtReceipt.insert(END, 'City Weighting: \t\t' + str("R %.2f"%(CityWeighting.get()) ) + "\n")
			self.txtReceipt.insert(END, 'Tax Paid: \t\t' + str("R %.2f"%(BasicSalary.get()) ) + "\n")
			self.txtReceipt.insert(END, 'Overtime: \t\t' + Overtime.get() + "\n")
			self.txtReceipt.insert(END, 'Netpay: \t\t' + Netpay.get() + "\n")
			self.txtReceipt.insert(END, 'Grosspay: \t\t' + Grosspay.get() + "\n")

			addData()



		#==============RECEIPT===========================================================================================

		self.txtReceipt = Text(RightFrame1a, height=24,bd=10, width=49, font=('arial', 9, 'bold'))
		self.txtReceipt.grid(row=0, column=0, )
		#========================================================================================================
		self.lblLabel = Label(TopFrame2, text="Reference\tFirstName\tSurname\tAddress\t\tGender\t\tMobile\tNI Numbert\tStudent Loan\ttax\tPension\tDeductions\tNet Pay\t    Gross Pay", font=('arial', 10, 'bold'), pady=2,padx=8)
		self.lblLabel.grid(row=0, column=0, columnspan=18, sticky=W)
		#========================================================================================================

		scrollbar = Scrollbar(TopFrame2)
		scrollbar.grid(row=1, column=1, sticky="ns")

		lstEmployee = Listbox(TopFrame2, width=137, height=10,  font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
		lstEmployee.bind("<<ListboxSelect>>", EmployeeRec)
		lstEmployee.grid(row=1, column=0, padx=1, sticky='nsew')
		scrollbar.config(command=lstEmployee.xview)

		#======================WIDGETS TF3 LF1==================================================================================
		self.lblReference = Label(LeftFrame1, text="Reference", font=('arial', 12, 'bold'), pady=10)
		self.lblReference.grid(row=0, column=0, padx=2, sticky= W)
		self.txtReference = Entry(LeftFrame1, textvariable=Reference, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtReference.grid(row=0, column=1)

		self.lblFirstName = Label(LeftFrame1, text="Firstname", font=('arial', 12, 'bold'), pady=8)
		self.lblFirstName.grid(row=1, column=0, padx=2, sticky= W)
		self.txtFirstName = Entry(LeftFrame1, textvariable=FirstName, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtFirstName.grid(row=1, column=1)

		self.lblSurname = Label(LeftFrame1, text="Surname", font=('arial', 12, 'bold'), pady=8)
		self.lblSurname.grid(row=2, column=0, padx=2, sticky= W)
		self.txtSurname = Entry(LeftFrame1, textvariable=Surname, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtSurname.grid(row=2, column=1)

		self.lblAddress = Label(LeftFrame1, text="Address", font=('arial', 12, 'bold'), pady=8)
		self.lblAddress.grid(row=3, column=0, padx=2, sticky= W)
		self.txtAddress = Entry(LeftFrame1, textvariable=Address, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtAddress.grid(row=3, column=1)

		self.lblGender = Label(LeftFrame1, text="Gender", font=('arial', 12, 'bold'), pady=8)
		self.lblGender.grid(row=4, column=0, padx=2, sticky= W)
		self.txtGender = Entry(LeftFrame1, textvariable=Gender, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtGender.grid(row=4, column=1)

		self.lblMobile = Label(LeftFrame1, text="Mobile", font=('arial', 12, 'bold'), pady=10)
		self.lblMobile.grid(row=4, column=0, padx=2, sticky= W)
		self.txtMobile = Entry(LeftFrame1, textvariable=Mobile, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=56)
		self.txtMobile.grid(row=4, column=1)

		#======================WIDGETS TF3 LF2Left==================================================================================
		self.lblCityWeighting = Label(LeftFrame2Left, text="CityWeighting", font=('arial', 12, 'bold'), pady=10)
		self.lblCityWeighting.grid(row=0, column=0, padx=2, sticky= W)
		self.txtCityWeighting = Entry(LeftFrame2Left, textvariable=CityWeighting, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtCityWeighting.grid(row=0, column=1)

		self.lblBasicSalary = Label(LeftFrame2Left, text="BasicSalary", font=('arial', 12, 'bold'), pady=8)
		self.lblBasicSalary.grid(row=1, column=0, padx=2, sticky= W)
		self.txtBasicSalary = Entry(LeftFrame2Left, textvariable=BasicSalary, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtBasicSalary.grid(row=1, column=1)

		self.lblOvertime = Label(LeftFrame2Left, text="Overtime", font=('arial', 12, 'bold'), pady=8)
		self.lblOvertime.grid(row=2, column=0, padx=2, sticky= W)
		self.txtOvertime = Entry(LeftFrame2Left, textvariable=Overtime, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtOvertime.grid(row=2, column=1)

		self.lblOtherPaymentDue = Label(LeftFrame2Left, text="OtherPaymentDue", font=('arial', 12, 'bold'), pady=10)
		self.lblOtherPaymentDue.grid(row=3, column=0, padx=2, sticky= W)
		self.txtOtherPaymentDue = Entry(LeftFrame2Left, textvariable=OtherPaymentDue, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtOtherPaymentDue.grid(row=3, column=1)

		#======================WIDGETS TF3 LF2Right==================================================================================
		self.lblTax = Label(LeftFrame2Right, text="Tax", font=('arial', 12, 'bold'), pady=10)
		self.lblTax.grid(row=0, column=0, padx=2, sticky= W)
		self.txtTax = Entry(LeftFrame2Right, textvariable=Tax, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtTax.grid(row=0, column=1)

		self.lblPension = Label(LeftFrame2Right, text="Pension", font=('arial', 12, 'bold'), pady=8)
		self.lblPension.grid(row=1, column=0, padx=2, sticky= W)
		self.lblPension = Entry(LeftFrame2Right, textvariable=Pension, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.lblPension.grid(row=1, column=1)

		self.lblstdLoan = Label(LeftFrame2Right, text="Student Loan", font=('arial', 12, 'bold'), pady=8)
		self.lblstdLoan.grid(row=2, column=0, padx=2, sticky= W)
		self.txtstdLoan = Entry(LeftFrame2Right, textvariable=stdLoan, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtstdLoan.grid(row=2, column=1)

		self.lblNIPayment = Label(LeftFrame2Right, text="OtherPaymentDue", font=('arial', 12, 'bold'), pady=10)
		self.lblNIPayment.grid(row=3, column=0, padx=2, sticky= W)
		self.txtNIPayment = Entry(LeftFrame2Right, textvariable=NIPayment, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=15)
		self.txtNIPayment.grid(row=3, column=1)

		#======================WIDGETS RightFrame2a==================================================================================

		self.lblPayday = Label(RightFrame2a, text="Payday", font=('arial', 12, 'bold'))
		self.lblPayday.grid(row=0, column=0, padx=2)
		self.txtPayday = Entry(RightFrame2a, textvariable=Payday, font=('arial', 12, 'bold'), justify='right', bd=5, width=21)
		self.txtPayday.grid(row=0, column=1)

		#======================WIDGETS RightFrame2b==================================================================================
		self.lblTaxPeriod = Label(RightFrame2b, text="TaxPeriod", font=('arial', 12, 'bold'), pady=8)
		self.lblTaxPeriod.grid(row=0, column=0, padx=2, sticky= W)
		self.txtTaxPeriod = Entry(RightFrame2b, textvariable=TaxPeriod, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=19)
		self.txtTaxPeriod.grid(row=0, column=1)

		self.lblTaxCode = Label(RightFrame2b, text="TaxCode", font=('arial', 12, 'bold'), pady=8)
		self.lblTaxCode.grid(row=1, column=0, padx=2, sticky= W)
		self.txtTaxCode = Entry(RightFrame2b, textvariable=TaxCode, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=19)
		self.txtTaxCode.grid(row=1, column=1)

		self.lblNINumber = Label(RightFrame2b, text="NI Number", font=('arial', 12, 'bold'), pady=8)
		self.lblNINumber.grid(row=2, column=0, padx=2, sticky= W)
		self.txtNINumber = Entry(RightFrame2b, textvariable=NINumber, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=19)
		self.txtNINumber.grid(row=2, column=1)

		self.lblNICode = Label(RightFrame2b, text="NI Code", font=('arial', 12, 'bold'), pady=8)
		self.lblNICode.grid(row=3, column=0, padx=2, sticky= W)
		self.txtNICode = Entry(RightFrame2b, textvariable=NICode, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=19)
		self.txtNICode.grid(row=3, column=1)

		#======================WIDGETS RightFrame2c==================================================================================
		self.lblTaxablePay = Label(RightFrame2c, text="TaxablePay", font=('arial', 12, 'bold'), pady=8)
		self.lblTaxablePay.grid(row=0, column=0, padx=2, sticky= W)
		self.txtTaxablePay = Entry(RightFrame2c, textvariable=TaxablePay, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=14)
		self.txtTaxablePay.grid(row=0, column=1)

		self.lblPensionablepay = Label(RightFrame2c, text="Pensionable pay", font=('arial', 12, 'bold'), pady=8)
		self.lblPensionablepay.grid(row=1, column=0, padx=2, sticky= W)
		self.txtPensionablepay = Entry(RightFrame2c, textvariable=Pensionablepay, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=14)
		self.txtPensionablepay.grid(row=1, column=1)

		#======================WIDGETS RightFrame2d==================================================================================
		self.lblNetpay = Label(RightFrame2d, text="Netpay", font=('arial', 12, 'bold'), pady=8)
		self.lblNetpay.grid(row=0, column=0, sticky= W)
		self.txtNetpay = Entry(RightFrame2d, textvariable=Netpay, font=('arial', 12, 'bold'), bd=5, width=18)
		self.txtNetpay.grid(row=0, column=1)

		self.lblGrosspay = Label(RightFrame2d, text="Grosspay", font=('arial', 12, 'bold'), pady=8)
		self.lblGrosspay.grid(row=1, column=0, padx=2, sticky= W)
		self.txtGrosspay = Entry(RightFrame2d, textvariable=Grosspay, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=18)
		self.txtGrosspay.grid(row=1, column=1)

		self.lblDeductions = Label(RightFrame2d, text="Deductions", font=('arial', 12, 'bold'))
		self.lblDeductions.grid(row=2, column=0, padx=2, sticky= W)
		self.txtDeductions = Entry(RightFrame2d, textvariable=Deductions, font=('arial', 12, 'bold'), justify=LEFT, bd=5, width=18)
		self.txtDeductions.grid(row=2, column=1)


		#======================WIDGETS RightFrame2d==================================================================================
		self.btnAddNewTotal = Button(TopFrame1, bd=4, command=monthlySalary, width=8,  font=('arial', 16, 'bold'), text="AddNew/Total", padx=20).grid(row=0, column=0, padx=1)
		self.btnPrint = Button(TopFrame1, bd=4, command=iPrint, width=8,  font=('arial', 16, 'bold'), text="Print", padx=19).grid(row=0, column=1, padx=1)
		self.btnDisplay = Button(TopFrame1, bd=4, command=DisplayData, width=8,  font=('arial', 16, 'bold'), text="Display", padx=20).grid(row=0, column=2, padx=1)
		self.btnUpdate = Button(TopFrame1, bd=4, command=Update, width=8,  font=('arial', 16, 'bold'), text="Update", padx=19).grid(row=0, column=3, padx=1)
		self.btnDelete = Button(TopFrame1, bd=4, command=deleteData, width=8,  font=('arial', 16, 'bold'), text="Delete", padx=20).grid(row=0, column=4, padx=1)
		self.btnSearch = Button(TopFrame1, bd=4, command=searchData, width=8,  font=('arial', 16, 'bold'), text="Search", padx=19).grid(row=0, column=5, padx=1)
		self.btnReset = Button(TopFrame1, bd=4, command=Reset, width=8,  font=('arial', 16, 'bold'), text="Reset", padx=20).grid(row=0, column=6, padx=1)
		self.btnExit = Button(TopFrame1, bd=4, command=iExit, width=8,  font=('arial', 16, 'bold'), text="Exit", padx=19).grid(row=0, column=7, padx=1)







if __name__== '__main__':
	root = Tk()
	application = Employee (root)
	root.mainloop()