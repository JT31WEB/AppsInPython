from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
from datetime import datetime, date, timedelta

class Library:
	def __init__(self, root):
		self.root = root
		self.root.title("Library System")
		self.root.geometry('1350x750+0+0')
		self.root.config(background="powder blue")

		#==============VARIABLES===========================================================================================

		MType = StringVar()
		Ref = StringVar()
		Title = StringVar()
		FirstName = StringVar()
		Surname = StringVar()
		Address1 = StringVar()
		Address2 = StringVar()
		PostCode = StringVar()
		MobileNo = StringVar()
		BookID = StringVar()
		BookTitle = StringVar()
		BookType = StringVar()
		Author = StringVar()
		DateBorrowed = StringVar()
		DateDue = StringVar()
		SellingPrice = StringVar()
		LateReturnFine = StringVar()
		DateOverDue = StringVar()
		DaysOnLoan = StringVar()
		Prescription = StringVar()

		#==============FUNCTIONS=======================================================================================
		def iExit():
			qExit = messagebox.askyesno("Inventory System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

		def Reset():
			MType.set("")
			Ref.set("")
			Title.set("")
			FirstName.set("")
			Surname.set("")
			Address1.set("")
			Address2.set("")
			PostCode.set("")
			MobileNo.set("")
			BookID.set("")
			BookTitle.set("")
			BookType.set("")
			Author.set("")
			DateBorrowed.set("")
			DateDue.set("")
			SellingPrice.set("")
			LateReturnFine.set("")
			DateOverDue.set("")
			DaysOnLoan.set("")
			Prescription.set("")
			self.txtDisplay.delete("1.0", END)
			self.txtDetail.delete("1.0", END)

		def iDelete():
			Reset()
			self.txtDisplay.delete("1.0", END)

		def iDisplayData():
			self.txtDetail.insert(END, "\t" +MType.get()+ "\t" +Ref.get()+ "\t" +Title.get()+ "\t" +FirstName.get()+ "\t" +Surname.get()+ "\t" +Address1.get()+ "\t" +Address2.get()+ "\t" +PostCode.get()+ "\t" +MobileNo.get()+ "\t" +BookID.get()+ "\t" +BookTitle.get()+ "\t" +BookType.get()+ "\t" +Author.get()+ "\t" +DateBorrowed.get()+ "\t" +SellingPrice.get()+ "\t" +LateReturnFine.get() + "\t" +DateOverDue.get()+ "\t" +DaysOnLoan.get()+ "\t" +Prescription.get() + "\n")

		def iReceipt():
			self.txtDisplay.insert(END, ' Member Type:\t\t\t\t' + MType.get()+ "\n")
			self.txtDisplay.insert(END, ' Ref No:\t\t\t\t' + Ref.get() + "\n")
			self.txtDisplay.insert(END, ' Title:\t\t\t\t' + Title.get() + "\n")
			self.txtDisplay.insert(END, ' First Name:\t\t\t\t' + FirstName.get() + "\n")
			self.txtDisplay.insert(END, ' Surname:\t\t\t\t' + Surname.get() + "\n")
			self.txtDisplay.insert(END, ' Address 1:\t\t\t\t' + Address1.get() + "\n")
			self.txtDisplay.insert(END, ' Address 2:\t\t\t\t' + Address2.get() + "\n")
			self.txtDisplay.insert(END, ' PostCode:\t\t\t\t' + PostCode.get() + "\n")
			self.txtDisplay.insert(END, ' Mobile No:\t\t\t\t' + MobileNo.get() + "\n")
			self.txtDisplay.insert(END, ' Book ID:\t\t\t\t' + BookID.get() + "\n")
			self.txtDisplay.insert(END, ' BookTitle:\t\t\t\t' + BookTitle.get() + "\n")
			self.txtDisplay.insert(END, ' BookType:\t\t\t\t' + BookType.get() + "\n")
			self.txtDisplay.insert(END, ' Author:\t\t\t\t' + Author.get() + "\n")
			self.txtDisplay.insert(END, ' Date Borrowed:\t\t\t\t' + DateBorrowed.get() + "\n")
			self.txtDisplay.insert(END, ' Selling Price:\t\t\t\t' + SellingPrice.get() + "\n")
			self.txtDisplay.insert(END, ' Late Return Fine:\t\t\t\t' + LateReturnFine.get() + "\n")
			self.txtDisplay.insert(END, ' Date Over Due:\t\t\t\t' + DateOverDue.get() + "\n")
			self.txtDisplay.insert(END, ' Days On Loan:\t\t\t\t' + DaysOnLoan.get() + "\n")
			self.txtDisplay.insert(END, ' Number of Days:\t\t\t\t' + Prescription.get() + "\n")

		def SelectedBook(evt):
			value= str(Booklist.get(Booklist.curselection()))
			w = value

 		#','', ''

			if (w== 'Cinderella'):
				BookID.set("ISBN 78945213")
				BookTitle.set("Cinderella")
				Author.set("Peter Parker")
				SellingPrice.set("R99.99")
				LateReturnFine.set("R30")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Game Design'):
				BookID.set("ISBN 78961313")
				BookTitle.set("Cinderella")
				Author.set("Bob Jones")
				SellingPrice.set("R89.99")
				LateReturnFine.set("R35")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Ancient Rome'):
				BookID.set("ISBN 21961913")
				BookTitle.set("Ancient Rome")
				Author.set("Ken James")
				SellingPrice.set("R109.99")
				LateReturnFine.set("R45")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Made In Africa'):
				BookID.set("ISBN 21961913")
				BookTitle.set("Made In Africa")
				Author.set("Sipho Zulu")
				SellingPrice.set("R79.99")
				LateReturnFine.set("R25")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Sleeping Beauty'):
				BookID.set("ISBN 21961913")
				BookTitle.set("Sleeping Beauty")
				Author.set("Thomas King")
				SellingPrice.set("R69.99")
				LateReturnFine.set("R25")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'London'):
				BookID.set("ISBN 91364923")
				BookTitle.set("London")
				Author.set("James Cameron")
				SellingPrice.set("R99.99")
				LateReturnFine.set("R30")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Nigeria'):
				BookID.set("ISBN 83346921")
				BookTitle.set("Nigeria")
				Author.set("Sam Smith")
				SellingPrice.set("R109.99")
				LateReturnFine.set("R35")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Snow White'):
				BookID.set("ISBN 734429241")
				BookTitle.set("Snow White")
				Author.set("Adele")
				SellingPrice.set("R79.99")
				LateReturnFine.set("R25")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'Shrek 3'):
				BookID.set("ISBN 331426241")
				BookTitle.set("Shrek 3")
				Author.set("Bob Marley")
				SellingPrice.set("R89.99")
				LateReturnFine.set("R30")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'I Love Lagos'):
				BookID.set("ISBN 637423251")
				BookTitle.set("I Love Lagos")
				Author.set("Fella Kuti")
				SellingPrice.set("R129.99")
				LateReturnFine.set("R50")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'I Love Kenya'):
				BookID.set("ISBN 126823251")
				BookTitle.set("I Love Kenya")
				Author.set("K'naan")
				SellingPrice.set("R79.99")
				LateReturnFine.set("R20")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")

			elif (w== 'I love Mzansi'):
				BookID.set("ISBN 469832168")
				BookTitle.set("I love Mzansi")
				Author.set("Fella Kuti")
				SellingPrice.set("R159.99")
				LateReturnFine.set("R100")
				DaysOnLoan.set("14")
				iReceipt()
				d1 = date.today()
				d2 = timedelta(days= 14)
				d3 = (d1 + d2)
				DateBorrowed.set(d1)
				DateDue.set(d3)
				DateOverDue.set("No")



		#=============FRAMES==========================================================================
		MainFrame =Frame(self.root)
		MainFrame.grid()

		TitleFrame = Frame(MainFrame, width=1350, padx=10,bd=20, relief=RIDGE)
		TitleFrame.grid(row=0, column=0,sticky= W)

		self.lblTitle = Label(TitleFrame, justify="center", width=37, text="\tLibrary Manangement System\t", font=('arial', 40, 'bold'), padx=12)
		self.lblTitle.grid(row=0, column=0)


		ButtonFrame = Frame(MainFrame, bd=10, width=1350, height=50, relief=RIDGE)
		ButtonFrame.grid(row=3, column=0, sticky=W)

		DetailFrame = Frame(MainFrame, bd=10, width=1350, height=100, relief=RIDGE)
		DetailFrame.grid(row=2, column=0, sticky=W)

		DataFrame = Frame(MainFrame, bd=10, width=1300, height=400,  padx=5,relief=RIDGE)
		DataFrame.grid(row=1, column=0, sticky= W)

		DataFrameLEFT = LabelFrame(DataFrame, font=('arial', 18, 'bold'), text="Library Membership Info:", bd=10, width=800, height=300, relief=RIDGE)
		DataFrameLEFT.grid(row=0, column=0)

		DataFrameRIGHT = LabelFrame(DataFrame, font=('arial', 18, 'bold'), text="Book Details:", bd=10, width=450, height=300, relief=RIDGE)
		DataFrameRIGHT.grid(row=0, column=1)
		#===================Dispaly======================================================================================
		self.txtDisplay = Text(DataFrameRIGHT, bg="cyan", height=13, width=30, padx=8, pady=20, font=('arial', 12, 'bold'))
		self.txtDisplay.grid(row=0, column=2)


		#==================LISTBOX=============================================================
		scrollbar = Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0, column=1, sticky="ns")

		ListOfBooks = ['Cinderella','Game Design', 'Ancient Rome','Made In Africa','Sleeping Beauty','London', 'Nigeria','Snow White', 'Shrek 3', 'I Love Lagos','I Love Kenya', 'I love Mzansi', 'Cinderella','Game Design', 'ancient Rome','Made In Africa','Sleeping Beauty','London']

		Booklist = Listbox(DataFrameRIGHT, width=20, height=12,  font=('arial', 12, 'bold'))
		Booklist.bind("<<ListboxSelect>>", SelectedBook)
		Booklist.grid(row=0, column=0, padx=8)
		scrollbar.config(command=Booklist.yview)

		for items in ListOfBooks:
			Booklist.insert(END, items)

		#==================LISTBOX=============================================================
		self.lblTitle = Label(DetailFrame, text="Member Type\tReference No.\tTitle\tFirstName\tSurname\tAddress 1\tAddress 2\tPostCode\tBook Title\tDate Borrowed\tDays On Loan", font=('arial', 10, 'bold'), pady=8)
		self.lblTitle.grid(row=0, column=0)

		self.txtDetail = Text(DetailFrame, bg="cyan", height=5, width=140, pady=4, font=('arial', 12, 'bold'))
		self.txtDetail.grid(row=1, column=0)


		#===================WIDGETS======================================================================================
		self.lblMemberType = Label(DataFrameLEFT, text="Member Type:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblMemberType.grid(row=0, column=0)
		self.cboMemberType = ttk.Combobox(DataFrameLEFT, textvariable=MType, font=('arial', 12, 'bold'), width=23, state='readonly')
		self.cboMemberType['value'] = ('', 'Student', 'Lecturer', 'Admin Staff')
		self.cboMemberType.current(0)
		self.cboMemberType.grid(row=0, column=1, sticky= W)

		self.lblBookID = Label(DataFrameLEFT, text="Book ID:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblBookID.grid(row=0, column=2, sticky= W)
		self.txtBookID = Entry(DataFrameLEFT, textvariable=BookID, font=('arial', 12, 'bold'), width=25)
		self.txtBookID.grid(row=0, column=3)

		self.lblRef = Label(DataFrameLEFT, text="Reference No:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblRef.grid(row=1, column=0, sticky= W)
		self.txtRef = Entry(DataFrameLEFT, textvariable=Ref, font=('arial', 12, 'bold'), width=25)
		self.txtRef.grid(row=1, column=1)

		self.lblBookTitle = Label(DataFrameLEFT, text="Book Title:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblBookTitle.grid(row=1, column=2, sticky= W)
		self.txtBookTitle = Entry(DataFrameLEFT, textvariable=BookTitle, font=('arial', 12, 'bold'), width=25)
		self.txtBookTitle.grid(row=1, column=3)

		self.lblTitle = Label(DataFrameLEFT, text="Title:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblTitle.grid(row=2, column=0, sticky= W)
		self.cboTitle = ttk.Combobox(DataFrameLEFT, textvariable=Title, font=('arial', 12, 'bold'), width=23, state='readonly')
		self.cboTitle['value'] = ('', 'Mr', 'Miss', 'Mrs', 'Dr', 'Capt',)
		self.cboTitle.current(0)
		self.cboTitle.grid(row=2, column=1, sticky= W)

		self.lblAuthor = Label(DataFrameLEFT, text="Author:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblAuthor.grid(row=2, column=2, sticky= W)
		self.cboAuthor = Entry(DataFrameLEFT, textvariable=Author, font=('arial', 12, 'bold'), width=25)
		self.cboAuthor.grid(row=2, column=3)

		self.lblFirstName = Label(DataFrameLEFT, text="FirstName:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblFirstName.grid(row=3, column=0, sticky= W)
		self.txtFirstName = Entry(DataFrameLEFT, textvariable=FirstName, font=('arial', 12, 'bold'), width=25)
		self.txtFirstName.grid(row=3, column=1)

		self.lblDateBorrowed = Label(DataFrameLEFT, text="Reference No:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblDateBorrowed.grid(row=3, column=2, sticky= W)
		self.lblDateBorrowed = Entry(DataFrameLEFT, textvariable=DateBorrowed, font=('arial', 12, 'bold'), width=25)
		self.lblDateBorrowed.grid(row=3, column=3)

		self.lblSurName = Label(DataFrameLEFT, text="Surame:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblSurName.grid(row=4, column=0, sticky= W)
		self.txtSurName = Entry(DataFrameLEFT, textvariable=Surname, font=('arial', 12, 'bold'), width=25)
		self.txtSurName.grid(row=4, column=1)

		self.lblDateDue = Label(DataFrameLEFT, text="Due Date:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblDateDue.grid(row=4, column=2, sticky= W)
		self.txtDateDue = Entry(DataFrameLEFT, textvariable=DateDue, font=('arial', 12, 'bold'), width=25)
		self.txtDateDue.grid(row=4, column=3)

		self.lblAddress1 = Label(DataFrameLEFT, text="Address 1:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblAddress1.grid(row=5, column=0, sticky= W)
		self.txtAddress1 = Entry(DataFrameLEFT, textvariable=Address1, font=('arial', 12, 'bold'), width=25)
		self.txtAddress1.grid(row=5, column=1)

		self.lblDaysOnLoan = Label(DataFrameLEFT, text="Days On Loan:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblDaysOnLoan.grid(row=5, column=2, sticky= W)
		self.txtDaysOnLoan = Entry(DataFrameLEFT, textvariable=DaysOnLoan, font=('arial', 12, 'bold'), width=25)
		self.txtDaysOnLoan.grid(row=5, column=3)

		self.lblAddress2 = Label(DataFrameLEFT, text="Address 2:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblAddress2.grid(row=6, column=0, sticky= W)
		self.txtAddress2 = Entry(DataFrameLEFT, textvariable=Address2, font=('arial', 12, 'bold'), width=25)
		self.txtAddress2.grid(row=6, column=1)

		self.lblLateReturnFine = Label(DataFrameLEFT, text="Late Return Fine:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblLateReturnFine.grid(row=6, column=2, sticky= W)
		self.txtLateReturnFine = Entry(DataFrameLEFT, textvariable=LateReturnFine, font=('arial', 12, 'bold'), width=25)
		self.txtLateReturnFine.grid(row=6, column=3)

		self.lblPostCode = Label(DataFrameLEFT, text="Post Code:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblPostCode.grid(row=7, column=0, sticky= W)
		self.txtPostCode = Entry(DataFrameLEFT, textvariable=PostCode, font=('arial', 12, 'bold'), width=25)
		self.txtPostCode.grid(row=7, column=1)

		self.lblDateOverDue = Label(DataFrameLEFT, text="Date Over Due:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblDateOverDue.grid(row=7, column=2, sticky= W)
		self.txtDateOverDue = Entry(DataFrameLEFT, textvariable=DateOverDue, font=('arial', 12, 'bold'), width=25)
		self.txtDateOverDue.grid(row=7, column=3)

		self.lblMobileNo = Label(DataFrameLEFT, text="Mobile No:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblMobileNo.grid(row=8, column=0, sticky= W)
		self.txtMobileNo = Entry(DataFrameLEFT, textvariable=MobileNo, font=('arial', 12, 'bold'), width=25)
		self.txtMobileNo.grid(row=8, column=1)

		self.lblSellingPrice = Label(DataFrameLEFT, text="Selling Price:", font=('arial', 12, 'bold'), padx=2, pady=5)
		self.lblSellingPrice.grid(row=8, column=2, sticky= W)
		self.txtSellingPrice = Entry(DataFrameLEFT, textvariable=Prescription, font=('arial', 12, 'bold'), width=25)
		self.txtSellingPrice.grid(row=8, column=3)

		#==================BUTTONs===========================================================================
		self.btnDisplay = Button(ButtonFrame, bd=4, width=30,  font=('arial', 12, 'bold'), text="Display Data").grid(row=0, column=0)
		self.btnDelete = Button(ButtonFrame, command=iDelete, bd=4, width=30,  font=('arial', 12, 'bold'), text="Delete").grid(row=0, column=1)
		self.btnReset = Button(ButtonFrame,command=Reset, bd=4, width=30,  font=('arial', 12, 'bold'), text="Reset").grid(row=0, column=2)
		self.btnExit = Button(ButtonFrame, command=iExit, bd=4, width=30,  font=('arial', 12, 'bold'), text="Exit").grid(row=0, column=3)




if __name__== '__main__':
	root = Tk()
	application = Library (root)
	root.mainloop()