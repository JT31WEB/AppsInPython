from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
from datetime import datetime, date, timedelta
import libDATABASE





class Library:
	def __init__(self, root):
		self.root = root
		self.root.title("Library Database System")
		self.root.geometry('1350x750+0+0')
		self.root.config(background="#fff")

		#==============VARIABLES===========================================================================================

		MType = StringVar()
		Ref = StringVar()
		Tit = StringVar()
		FNa = StringVar()
		Sna = StringVar()
		Adr1 = StringVar()
		Adr2 = StringVar()
		PCd = StringVar()
		MNo = StringVar()
		BkID = StringVar()
		BkT = StringVar()
		Atr = StringVar()
		DBo = StringVar()
		DDu = StringVar()
		SPr = StringVar()
		LRF = StringVar()
		DOD = StringVar()
		DOnL = StringVar()


		#==============FUNCTIONS===========================================================================================
		def iExit():
			qExit = messagebox.askyesno("Library DataBase System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

		def ClearData():
			self.txtMType.delete(0,END)
			self.txtRef.delete(0,END)
			self.txtTit.delete(0,END)
			self.txtFNa.delete(0,END)
			self.txtSna.delete(0,END)
			self.txtAdr1.delete(0,END)
			self.txtAdr2.delete(0,END)
			self.txtPCd.delete(0,END)
			self.txtMNo.delete(0,END)
			self.txtBkID.delete(0,END)
			self.txtBkT.delete(0,END)
			self.txtAtr.delete(0,END)
			self.txtDBo.delete(0,END)
			self.txtDDu.delete(0,END)
			self.txtSPr.delete(0,END)
			self.txtLRF.delete(0,END)
			self.txtDOD.delete(0,END)
			self.txtDOnL.delete(0,END)

		def addData():
			if(len(MType.get()) !=0):
				libDATABASE.addDataRec(MType.get(),Ref.get(),Tit.get(),FNa.get(),Sna.get(),Adr1.get(),Adr2.get(),PCd.get(),MNo.get(),BkID.get(),BkT.get(),Atr.get(),DBo.get(),DDu.get(),SPr.get(),LRF.get(),DOD.get(),DOnL.get())

				Booklist.delete(0, END)
				Booklist.insert(END,MType.get(),Ref.get(),Tit.get(),FNa.get(),Sna.get(),Adr1.get(),Adr2.get(),PCd.get(),MNo.get(),BkID.get(),BkT.get(),Atr.get(),DBo.get(),DDu.get(),SPr.get(),LRF.get(),DOD.get(),DOnL.get())

		def DisplayData():
			Booklist.delete(0, END)
			for row in libDATABASE.viewData():
				Booklist.insert(END, row)

		def SelectedBook(event):
			global sb 
			searchBk = Booklist.curselection()[0]
			sb = Booklist.get(searchBk)

			self.txtMType.delete(0,END)
			self.txtMType.insert(END,sb[1])
			self.txtRef.delete(0,END)
			self.txtRef.insert(END,sb[2])
			self.txtTit.delete(0,END)
			self.txtTit.insert(END,sb[3])
			self.txtFNa.delete(0,END)
			self.txtFNa.insert(END,sb[4])
			self.txtSna.delete(0,END)
			self.txtSna.insert(END,sb[5])
			self.txtAdr1.delete(0,END)
			self.txtAdr1.insert(END,sb[6])
			self.txtAdr2.delete(0,END)
			self.txtAdr2.insert(END,sb[7])
			self.txtPCd.delete(0,END)
			self.txtPCd.insert(END,sb[8])
			self.txtMNo.delete(0,END)
			self.txtMNo.insert(END,sb[9])
			self.txtBkID.delete(0,END)
			self.txtBkID.insert(END,sb[10])
			self.txtBkT.delete(0,END)
			self.txtBkT.insert(END,sb[11])
			self.txtAtr.delete(0,END)
			self.txtAtr.insert(END,sb[12])
			self.txtDBo.delete(0,END)
			self.txtDBo.insert(END,sb[13])
			self.txtDDu.delete(0,END)
			self.txtDDu.insert(END,sb[14])
			self.txtSPr.delete(0,END)
			self.txtSPr.insert(END,sb[15])
			self.txtLRF.delete(0,END)
			self.txtLRF.insert(END,sb[16])
			self.txtDOD.delete(0,END)
			self.txtDOD.insert(END,sb[17])
			self.txtDOnL.delete(0,END)
			self.txtDOnL.insert(END,sb[18])


		def DeleteData():
			if(len(MType.get()) !=0):
				libDATABASE.deleteRec(sb[0])
				ClearData()
				DisplayData()

		def searchDatabase():
			Booklist.delete(0, END)
			for row in libDATABASE.SearchData(MType.get(),Ref.get(),Tit.get(),FNa.get(),Sna.get(),Adr1.get(),Adr2.get(),PCd.get(),MNo.get(),BkID.get(),BkT.get(),Atr.get(),DBo.get(),DDu.get(),SPr.get(),LRF.get(),DOD.get(),DOnL.get()):
				Booklist.insert(END, row)

		def updateD():
			if(len(MType.get()) !=0):
				libDATABASE.UpdateData(sb[0],MType.get(),Ref.get(),Tit.get(),FNa.get(),Sna.get(),Adr1.get(),Adr2.get(),PCd.get(),MNo.get(),BkID.get(),BkT.get(),Atr.get(),DBo.get(),DDu.get(),SPr.get(),LRF.get(),DOD.get(),DOnL.get())

		#==============FRAMES===========================================================================================
		MainFrame =Frame(self.root)
		MainFrame.grid()

		TitFrame = Frame(MainFrame, pady=8, padx=200,bd=1, bg="cadet blue", relief=RIDGE)
		TitFrame.grid(row=0, column=0, padx=80, pady=20, sticky=W)

		self.lblTitle = Label(TitFrame, text="Library DataBase System", bg="powder blue", font=('arial', 46, 'bold'))
		self.lblTitle.grid(row=0, column=0)


		ButtonFrame = Frame(MainFrame, pady=20, padx=20, bg="cadet blue", bd=1, width=1300, height=100, relief=RIDGE)
		ButtonFrame.grid(row=3, column=0, sticky=W, padx=10)

		DetailFrame = Frame(MainFrame, bd=0, padx=20, width=1350, height=30, relief=RIDGE)
		DetailFrame.grid(row=2, column=0, sticky=W)

		DataFrame = Frame(MainFrame, bd=1, pady=20, padx=20, width=1300, height=400, relief=RIDGE)
		DataFrame.grid(row=1, column=0, sticky=W, padx=10)

		DataFrameLEFT = LabelFrame(DataFrame, bg="cadet blue", font=('arial', 18, 'bold'), text="Library Membership Info:", bd=1, padx=10,pady=8, width=800, height=300, relief=RIDGE)
		DataFrameLEFT.grid(row=0, column=0)

		DataFrameRIGHT = LabelFrame(DataFrame, bg="cadet blue", font=('arial', 18, 'bold'), text="Book Details:", bd=1, padx=10,pady=5, width=450, height=300, relief=RIDGE)
		DataFrameRIGHT.grid(row=0, column=1)
		#==============LABELS AND ENTRY===========================================================================================

		self.lblMemberType = Label(DataFrameLEFT, text="Member Type:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblMemberType.grid(row=0, column=0)
		self.txtMType = Entry(DataFrameLEFT, textvariable=MType, font=('arial', 12, 'bold'), width=25)
		self.txtMType.grid(row=0, column=1)
		

		self.lblBookID = Label(DataFrameLEFT, text="Book ID:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblBookID.grid(row=0, column=2, sticky= W)
		self.txtBkID = Entry(DataFrameLEFT, textvariable=BkID, font=('arial', 12, 'bold'), width=25)
		self.txtBkID.grid(row=0, column=3)

		self.lblRef = Label(DataFrameLEFT, text="Reference No:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblRef.grid(row=1, column=0, sticky= W)
		self.txtRef = Entry(DataFrameLEFT, textvariable=Ref, font=('arial', 12, 'bold'), width=25)
		self.txtRef.grid(row=1, column=1)

		self.lblBookTitle = Label(DataFrameLEFT, text="Book Title:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblBookTitle.grid(row=1, column=2, sticky= W)
		self.txtBkT = Entry(DataFrameLEFT, textvariable=BkT, font=('arial', 12, 'bold'), width=25)
		self.txtBkT.grid(row=1, column=3)

		self.lblTitle = Label(DataFrameLEFT, text="Title:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblTitle.grid(row=2, column=0, sticky= W)
		self.txtTit = Entry(DataFrameLEFT, textvariable=Tit, font=('arial', 12, 'bold'), width=25)
		self.txtTit.grid(row=2, column=1)
		

		self.lblAuthor = Label(DataFrameLEFT, text="Author:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblAuthor.grid(row=2, column=2, sticky= W)
		self.txtAtr = Entry(DataFrameLEFT, textvariable=Atr, font=('arial', 12, 'bold'), width=25)
		self.txtAtr.grid(row=2, column=3)

		self.lblFirstName = Label(DataFrameLEFT, text="FirstName:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblFirstName.grid(row=3, column=0, sticky= W)
		self.txtFNa = Entry(DataFrameLEFT, textvariable=FNa, font=('arial', 12, 'bold'), width=25)
		self.txtFNa.grid(row=3, column=1)

		self.lblDateBorrowed = Label(DataFrameLEFT, text="Reference No:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblDateBorrowed.grid(row=3, column=2, sticky= W)
		self.txtDBo = Entry(DataFrameLEFT, textvariable=DBo, font=('arial', 12, 'bold'), width=25)
		self.txtDBo.grid(row=3, column=3)

		self.lblSurName = Label(DataFrameLEFT, text="Surame:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblSurName.grid(row=4, column=0, sticky= W)
		self.txtSna = Entry(DataFrameLEFT, textvariable=Sna, font=('arial', 12, 'bold'), width=25)
		self.txtSna.grid(row=4, column=1)

		self.lblDateDue = Label(DataFrameLEFT, text="Due Date:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblDateDue.grid(row=4, column=2, sticky= W)
		self.txtDDu = Entry(DataFrameLEFT, textvariable=DDu, font=('arial', 12, 'bold'), width=25)
		self.txtDDu.grid(row=4, column=3)

		self.lblAddress1 = Label(DataFrameLEFT, text="Address 1:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblAddress1.grid(row=5, column=0, sticky= W)
		self.txtAdr1 = Entry(DataFrameLEFT, textvariable=Adr1, font=('arial', 12, 'bold'), width=25)
		self.txtAdr1.grid(row=5, column=1)

		self.lblDaysOnLoan = Label(DataFrameLEFT, text="Days On Loan:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblDaysOnLoan.grid(row=5, column=2, sticky= W)
		self.txtDOnL = Entry(DataFrameLEFT, textvariable=DOnL, font=('arial', 12, 'bold'), width=25)
		self.txtDOnL.grid(row=5, column=3)

		self.lblAddress2 = Label(DataFrameLEFT, text="Address 2:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblAddress2.grid(row=6, column=0, sticky= W)
		self.txtAdr2 = Entry(DataFrameLEFT, textvariable=Adr2, font=('arial', 12, 'bold'), width=25)
		self.txtAdr2.grid(row=6, column=1)

		self.lblLateReturnFine = Label(DataFrameLEFT, text="Late Return Fine:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblLateReturnFine.grid(row=6, column=2, sticky= W)
		self.txtLRF = Entry(DataFrameLEFT, textvariable=LRF, font=('arial', 12, 'bold'), width=25)
		self.txtLRF.grid(row=6, column=3)

		self.lblPostCode = Label(DataFrameLEFT, text="Post Code:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblPostCode.grid(row=7, column=0, sticky= W)
		self.txtPCd = Entry(DataFrameLEFT, textvariable=PCd, font=('arial', 12, 'bold'), width=25)
		self.txtPCd.grid(row=7, column=1)

		self.lblDateOverDue = Label(DataFrameLEFT, text="Date Over Due:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblDateOverDue.grid(row=7, column=2, sticky= W)
		self.txtDOD = Entry(DataFrameLEFT, textvariable=DOD, font=('arial', 12, 'bold'), width=25)
		self.txtDOD.grid(row=7, column=3)

		self.lblMobileNo = Label(DataFrameLEFT, text="Mobile No:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblMobileNo.grid(row=8, column=0, sticky= W)
		self.txtMNo = Entry(DataFrameLEFT, textvariable=MNo, font=('arial', 12, 'bold'), width=25)
		self.txtMNo.grid(row=8, column=1)

		self.lblSellingPrice = Label(DataFrameLEFT, text="Selling Price:", font=('arial', 12, 'bold'), padx=2, pady=5, bg="cadet blue")
		self.lblSellingPrice.grid(row=8, column=2, sticky= W)
		self.txtSPr = Entry(DataFrameLEFT, textvariable=SPr, font=('arial', 12, 'bold'), width=25)
		self.txtSPr.grid(row=8, column=3)
		#==============LISTBOX AND SCROLLBAR===========================================================================================
		scrollbar = Scrollbar(DataFrameRIGHT)
		scrollbar.grid(row=0, column=1, sticky="ns")


		Booklist = Listbox(DataFrameRIGHT, width=45, height=15, font=('arial', 12, 'bold'), yscrollcommand= scrollbar.set)
		Booklist.bind("<<ListboxSelect>>", SelectedBook)
		Booklist.grid(row=0, column=0, padx=8)
		scrollbar.config(command=Booklist.yview)

		
		#==================BUTTONs===========================================================================
		self.btnAddData = Button(ButtonFrame,command=addData, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Add Data").grid(row=0, column=0)
		self.btnDisplayData = Button(ButtonFrame, command=DisplayData, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Display Data").grid(row=0, column=1)
		self.btnClear = Button(ButtonFrame, command=ClearData, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Clear").grid(row=0, column=2)
		self.btnDeleteData = Button(ButtonFrame, command=DeleteData, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Delete").grid(row=0, column=3)
		self.btnUpdateData = Button(ButtonFrame,command=updateD, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Update").grid(row=0, column=4)
		self.btnSearchData = Button(ButtonFrame,command=searchDatabase, bd=4, width=16, height=2,  font=('arial', 12, 'bold'), text="Search").grid(row=0, column=5)
		self.btnExit = Button(ButtonFrame, bd=4, command=iExit, width=16, height=2,  font=('arial', 12, 'bold'), text="Exit").grid(row=0, column=6)


if __name__== '__main__':
	root = Tk()
	application = Library (root)
	root.mainloop()