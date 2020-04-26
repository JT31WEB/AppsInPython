from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
from datetime import datetime, date, timedelta


class Inventory:
	def __init__(self, root):
		self.root = root
		self.root.title("Inventory System")
		self.root.geometry('1350x750+0+0')
		self.root.config(background="powder blue")

		MainFrame =Frame(self.root, bd=16, width=1350, height=700, relief=RAISED, bg="cadet blue")
		MainFrame.grid()

		LeftFrame = Frame(MainFrame, bd=10, width=740, height=700,  padx=5,relief=RIDGE, bg="cadet blue")
		LeftFrame.pack(side=LEFT)

		RightFrame = Frame(MainFrame, bd=10, width=550, height=700,  padx=5,relief=RIDGE, bg="cadet blue")
		RightFrame.pack(side=RIGHT)
		#==================================================================================================================

		LeftFrame0 = Frame(LeftFrame, bd=10, width=700, height=170,  padx=19, pady=5,relief=RIDGE, bg="powder blue")
		LeftFrame0.grid(row=0, column=0,)
		LeftFrame1 = Frame(LeftFrame, bd=10, width=700, height=200,  padx=9,relief=RIDGE, bg="powder blue")
		LeftFrame1.grid(row=1, column=0)
		LeftFrame2 = Frame(LeftFrame, bd=10, width=700, height=170,  padx=2,relief=RIDGE, bg="powder blue")
		LeftFrame2.grid(row=2, column=0 )
		LeftFrame3 = Frame(LeftFrame, bd=10, width=700, height=100,  padx=2,relief=RIDGE, bg="powder blue")
		LeftFrame3.grid(row=3, column=0 )

		LeftFrame2L = Frame(LeftFrame2, bd=10, width=200, height=170,  padx=2,relief=RIDGE, bg="powder blue")
		LeftFrame2L.grid(row=0, column=0 )
		LeftFrame2R = Frame(LeftFrame2, bd=10, width=500, height=170,  padx=2,relief=RIDGE, bg="powder blue")
		LeftFrame2R.grid(row=0, column=1 )

		RightFrame0 = Frame(RightFrame, bd=10, width=500, height=200,  padx=10,relief=RIDGE, bg="powder blue")
		RightFrame0.grid(row=0, column=0 )
		RightFrame1 = Frame(RightFrame, bd=10, width=500, height=350,  padx=2,relief=RIDGE, bg="powder blue")
		RightFrame1.grid(row=1, column=0 )
		RightFrame2 = Frame(RightFrame, bd=10, width=500, height=100,  padx=2,relief=RIDGE, bg="powder blue")
		RightFrame2.grid(row=2, column=0 )
		#=========================VARIABLES============================================================
		AccountOpened = StringVar()
		ApplicationDate = StringVar()
		NxtCreditRev = StringVar()
		LstCreditRev = StringVar()
		DateReview = StringVar()
		ProdCode = StringVar()
		ProdType = StringVar()
		NoDays = StringVar()
		CostPDay = StringVar()
		CreLimit = StringVar()
		CreCheck = StringVar()
		SetDueDay = StringVar()
		paymentD = StringVar()
		Discount = StringVar()
		Deposit = StringVar()
		PayDueDay = StringVar()
		paymentM = StringVar()
		CustomerRef = StringVar()

		var1 = IntVar()
		var2 = IntVar()
		var3 = IntVar()
		var4 = IntVar()
		var5 = IntVar()
		var6 = IntVar()
		var7 = IntVar()
		var8 = IntVar()
		Tax = StringVar()
		SubTotal = StringVar()
		Total = StringVar()

		LstCreditRev.set(0)

		

		#=================FUNCTIONS============================================================================================================================
		def iExit():
			qExit = messagebox.askyesno("Inventory System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

		def Reset():
			AccountOpened.set("")
			ApplicationDate.set("")
			NxtCreditRev.set("")
			LstCreditRev.set("")
			DateReview.set("")
			ProdCode.set("")
			ProdType.set("")
			NoDays.set("")
			CostPDay.set("")
			CreLimit.set("")
			CreCheck.set("")
			SetDueDay.set("")
			paymentD.set("")
			Discount.set("")
			Deposit.set("")
			PayDueDay.set("")
			paymentM.set("")
			self.txtInfo.delete("1.0", END)
			self.txtReceipt.delete("1.0", END)
			self.cboProdType.configure(state= DISABLED)

			var1.set(0)
			var2.set(0)
			var3.set(0)
			var4.set(0)
			Tax.set("")
			SubTotal.set("")
			Total.set("")
			return


		def iDates(evt):
			values = str(self.cboNoDays.get())
			NDays = values

			if (NDays != ''):
				self.cboProdType.configure(state="readonly")
			


			if NDays == "1-30":
				d1 = date.today()
				d2 = timedelta(days= 30)
				d3 = (d1 + d2)
				ApplicationDate.set(d1)
				NxtCreditRev.set(d3)
				LstCreditRev.set(30)
				DateReview.set(d3)

				CreLimit.set("R150")
				Discount.set("5%")
				AccountOpened.set("Yes")
			elif NDays == "31-90":
				d1 = date.today()
				d2 = timedelta(days= 90)
				d3 = (d1 + d2)
				ApplicationDate.set(d1)
				NxtCreditRev.set(d3)
				LstCreditRev.set(90)
				DateReview.set(d3)

				CreLimit.set("R200")
				Discount.set("10%")
				AccountOpened.set("Yes")
			elif NDays == "91-270":
				d1 = date.today()
				d2 = timedelta(days= 270)
				d3 = (d1 + d2)
				ApplicationDate.set(d1)
				NxtCreditRev.set(d3)
				LstCreditRev.set(270)
				DateReview.set(d3)

				CreLimit.set("R250")
				Discount.set("15%")
				AccountOpened.set("Yes")
			elif NDays == "271-365":
				d1 = date.today()
				d2 = timedelta(days= 365)
				d3 = (d1 + d2)
				ApplicationDate.set(d1)
				NxtCreditRev.set(d3)
				LstCreditRev.set(365)
				DateReview.set(d3)

				CreLimit.set("R300")
				Discount.set("20%")
				AccountOpened.set("Yes")

			elif  NDays == "0":
				messagebox.showinfo("Zero selected", "you choose zero")
				Reset()

		def Product (evt):
			values = str(self.cboProdType.get())
			pType = values
			if pType == "Lawn Mower":
				ProdCode.set("LAW981")
				CostPDay.set("R120")
				CreCheck.set("No")
				SetDueDay.set(120)
				paymentD.set("No")
				Deposit.set("No")
				paymentM.set("Cash")

				n = float(LstCreditRev.get())
				s = float(SetDueDay.get())
				price = (n * s)
				TC = "R", str('%.2f'%(price))
				PayDueDay.set(TC)
			elif pType == "Pickup Van":
				ProdCode.set("PV2451")
				CostPDay.set("R190")
				CreCheck.set("No")
				SetDueDay.set(190)
				paymentD.set("No")
				Deposit.set("No")
				paymentM.set("Cash")

				n = float(LstCreditRev.get())
				s = float(SetDueDay.get())
				price = (n * s)
				TC = "R", str('%.2f'%(price))
				PayDueDay.set(TC)

			elif pType == "Cement Mixer":
				ProdCode.set("CM5691")
				CostPDay.set("R210")
				CreCheck.set("No")
				SetDueDay.set(210)
				paymentD.set("No")
				Deposit.set("No")
				paymentM.set("Cash")

				n = float(LstCreditRev.get())
				s = float(SetDueDay.get())
				price = (n * s)
				TC = "R", str('%.2f'%(price))
				PayDueDay.set(TC)

			elif pType == "Elect. Generator":
				ProdCode.set("CM5691")
				CostPDay.set("R250")
				CreCheck.set("No")
				SetDueDay.set(250)
				paymentD.set("No")
				Deposit.set("No")
				paymentM.set("Cash")

				n = float(LstCreditRev.get())
				s = float(SetDueDay.get())
				price = (n * s)
				TC = "R", str('%.2f'%(price))
				PayDueDay.set(TC)

			elif pType == '':
				ProdCode.set("")
				CostPDay.set("")
				CreCheck.set("")
				SetDueDay.set()
				paymentD.set("")
				Deposit.set("")
				paymentM.set("")

				
				price = (0)
				TC = "R", str('%.2f'%(price))
				PayDueDay.set(TC)

		def checkCredit():
			if (var1.get()== 1):
				self.txtInfo.insert(END, "\tCheck credit Approved\n")
			elif (var1.get()== 0):
				self.txtInfo.delete("1.0",END)

		def TermAgreed():
			if (var2.get()== 1):
				self.txtInfo.insert(END, "\tTerms Agreed To\n")
			elif (var1.get()== 0):
				self.txtInfo.delete("1.0", END)

		def AcctOnHold():
			if (var3.get()== 1):
				self.txtInfo.insert(END, "\tAccout On Hold\n")
			elif (var1.get()== 0):
				self.txtInfo.delete("1.0",END)

		def RestrictMailing():
			if (var4.get()== 1):
				self.txtInfo.insert(END, "\tRestricted Mailing\n")
			elif (var1.get()== 0):
				self.txtInfo.delete("1.0", END)


		def TotalCost():
			n = float(LstCreditRev.get())
			s = float(SetDueDay.get())
			price = (n * s)
			ST = "R", str('%.2f'%(price))
			iTax = "R", str('%.2f'%((price)* 0.15))
			Tax.set(iTax)
			SubTotal.set(ST)

			TCost = "R", str('%.2f'%(((price)* 0.15) + price))
			Total.set(TCost)

			self.txtReceipt.delete("1.0", END)
			x = random.randint(10908, 500876)
			randomRef = str(x)
			CustomerRef.set("BILL_" + randomRef)

			self.txtReceipt.insert(END, 'ITEMS\t\t' + 'Customer Ref#:\t\t' + CustomerRef.get() + "\n")
			self.txtReceipt.insert(END, "============================== \n\n")
			self.txtReceipt.insert(END, ' Product Type:\t\t\t\t' + ProdType.get() + "\n")
			self.txtReceipt.insert(END, ' Product Code:\t\t\t\t' + ProdCode.get() + "\n")
			self.txtReceipt.insert(END, ' Number of Days:\t\t\t\t' + NoDays.get() + "\n")
			self.txtReceipt.insert(END, ' Account Opened:\t\t\t\t' + AccountOpened.get() + "\n")
			self.txtReceipt.insert(END, ' Next Credit Review:\t\t\t\t' + NxtCreditRev.get() + "\n")
			self.txtReceipt.insert(END, ' Last Credit Review:\t\t\t\t' + LstCreditRev.get() + "\n")
			self.txtReceipt.insert(END, "============================== \n\n")
			self.txtReceipt.insert(END, "Cost of Items\n\n")

			self.txtReceipt.insert(END, 'Tax Paid:\t\t\t' + str(Tax.get()) + "\n")
			self.txtReceipt.insert(END, 'SubTotal:\t\t\t' + str(SubTotal.get()) + "\n")
			self.txtReceipt.insert(END, 'Total Cost:\t\t\t' +  str(Total.get()) + "\n\n\n")

		
				

		#=========================LEFTFRAME0===============================================================================================
		self.lblProdType = Label(LeftFrame0,  fg="black", font=('arial', 16, 'bold'), text="Product Type:", padx=2, pady=8, bg="powder blue")
		self.lblProdType.grid(row=0, column=0, sticky=W, pady=2)
		self.cboProdType = ttk.Combobox(LeftFrame0, font=('arial', 16, 'bold'), textvariable=ProdType, width=12, state=DISABLED)
		self.cboProdType.bind("<<ComboboxSelected>>", Product)
		self.cboProdType['value'] = ('', 'Lawn Mower', 'Pickup Van', 'Cement Mixer', 'Elect. Generator')
		self.cboProdType.current(0)
		self.cboProdType.grid(row=0, column=1, pady=2)

		self.lblNoDays = Label(LeftFrame0,  fg="black", font=('arial', 16, 'bold'), text="No. of Days:", padx=2, pady=8, bg="powder blue")
		self.lblNoDays.grid(row=0, column=2, sticky=W, pady=2)
		self.cboNoDays = ttk.Combobox(LeftFrame0, font=('arial', 16, 'bold'), textvariable=NoDays, width=12, state='readonly')
		self.cboNoDays.bind("<<ComboboxSelected>>", iDates)
		self.cboNoDays['value'] = ('', '0', '1-30', '31-90', '91-270', '271-365')
		self.cboNoDays.current(0)
		self.cboNoDays.grid(row=0, column=3, sticky=W, pady=2)

		self.lblProdCode = Label(LeftFrame0,  fg="black", font=('arial', 16, 'bold'), text="Product Code:", padx=2, pady=4, bg="powder blue")
		self.lblProdCode.grid(row=1, column=0, sticky=W, pady=2)
		self.txtProdCode = Entry(LeftFrame0, font=('arial', 16, 'bold'), textvariable=ProdCode, width=14)
		self.txtProdCode.grid(row=1, column=1)

		self.lblCostPDay = Label(LeftFrame0,  fg="black", font=('arial', 16, 'bold'), text="Cost Per Day:", padx=2, pady=4, bg="powder blue")
		self.lblCostPDay.grid(row=1, column=2, sticky=W, pady=2)
		self.txtCostPDay = Entry(LeftFrame0, font=('arial', 16, 'bold'), textvariable=CostPDay, width=14)
		self.txtCostPDay.grid(row=1, column=3)
		
		#=========================LEFTFRAME1===============================================================================================
		self.lblCreLimit = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Credit Limit:", padx=2, pady=4, bg="powder blue")
		self.lblCreLimit.grid(row=0, column=0, sticky=W, pady=2)
		self.txtCreLimit = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=CreLimit, width=12, state='readonly')
		self.txtCreLimit['value'] = ('', 'R150', 'R200', 'R250', 'R300')
		self.txtCreLimit.current(0)
		self.txtCreLimit.grid(row=0, column=1, sticky=W, pady=2)

		self.lblCreCheck = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Credit Check:", padx=2, pady=4, bg="powder blue")
		self.lblCreCheck.grid(row=0, column=2, sticky=W, pady=2)
		self.txtCreCheck = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=CreCheck, width=12, state='readonly')
		self.txtCreCheck['value'] = ('', 'Yes', 'No')
		self.txtCreCheck.current(0)
		self.txtCreCheck.grid(row=0, column=3, sticky=W, pady=2)

		self.lblSetDueDay = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Sett. Due:", padx=2, pady=4, bg="powder blue")
		self.lblSetDueDay.grid(row=1, column=0, sticky=W, pady=2)
		self.txtSetDueDay = Entry(LeftFrame1, font=('arial', 16, 'bold'), textvariable=ProdCode, width=14)
		self.txtSetDueDay.grid(row=1, column=1)

		self.lblpaymentD = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Payment Due:", padx=2, pady=4, bg="powder blue")
		self.lblpaymentD.grid(row=1, column=2, sticky=W, pady=2)
		self.cbopaymentD = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=paymentD, width=12, state='readonly')
		self.cbopaymentD['value'] = ('', 'Yes', 'No')
		self.cbopaymentD.current(0)
		self.cbopaymentD.grid(row=1, column=3, sticky=W, pady=2)

		self.lblDiscount = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Discount:", padx=2, pady=4, bg="powder blue")
		self.lblDiscount.grid(row=2, column=0, sticky=W, pady=2)
		self.txtDiscount = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=Discount, width=12, state='readonly')
		self.txtDiscount['value'] = ('', '5%', '10%', '15%')
		self.txtDiscount.current(0)
		self.txtDiscount.grid(row=2, column=1, sticky=W, pady=2)

		self.lblDeposit = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Deposit:", padx=2, pady=4, bg="powder blue")
		self.lblDeposit.grid(row=2, column=2, sticky=W, pady=2)
		self.txtDeposit = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=Deposit, width=12, state='readonly')
		self.txtDeposit['value'] = ('', 'Yes', 'No')
		self.txtDeposit.current(0)
		self.txtDeposit.grid(row=2, column=3, sticky=W, pady=2)

		self.lblPayDueDay = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Pay Due Day:", padx=2, pady=4, bg="powder blue")
		self.lblPayDueDay.grid(row=3, column=0, sticky=W, pady=2)
		self.txtPayDueDay = Entry(LeftFrame1, font=('arial', 16, 'bold'), textvariable=PayDueDay, width=14)
		self.txtPayDueDay.grid(row=3, column=1)

		self.lblpaymentM = Label(LeftFrame1,  fg="black", font=('arial', 16, 'bold'), text="Payment Method:", padx=2, pady=4, bg="powder blue")
		self.lblpaymentM.grid(row=3, column=2, sticky=W, pady=2)
		self.cbopaymentM = ttk.Combobox(LeftFrame1, font=('arial', 16, 'bold'), textvariable=paymentM, width=12, state='readonly')
		self.cbopaymentM['value'] = ('', 'Cash', 'Visa Card', 'Master Card')
		self.cbopaymentM.current(0)
		self.cbopaymentM.grid(row=3, column=3, sticky=W, pady=2)
		#=========================LEFTFRAME2===============================================================================================
		self.chkCheckCredit = Checkbutton(LeftFrame2L, command=checkCredit, pady=5, bg="powder blue", text="Check Credit", variable=var1, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=0, column=0, sticky=W)
		self.chkTermAgreed = Checkbutton(LeftFrame2L, command=TermAgreed, pady=5, bg="powder blue", text="TermAgreed", variable=var2, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=1, column=0, sticky=W)
		self.chkAcctOnHold = Checkbutton(LeftFrame2L, command=AcctOnHold, pady=5, bg="powder blue", text="Accout On Hold", variable=var3, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=2, column=0, sticky=W)
		self.chkRestrictMailing = Checkbutton(LeftFrame2L, command=RestrictMailing, pady=5, bg="powder blue", text="Restrict Mailing ", variable=var4, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=3, column=0, sticky=W)

		self.chkCheckCredit = Checkbutton(LeftFrame2L, command=checkCredit, pady=5, bg="powder blue", text="Accout On Hold", variable=var5, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=0, column=1, sticky=W)
		self.chkTermAgreed = Checkbutton(LeftFrame2L, command=TermAgreed, pady=5, bg="powder blue", text="Restrict Mailing ", variable=var6, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=1, column=1, sticky=W)
		self.chkAcctOnHold = Checkbutton(LeftFrame2L, command=AcctOnHold, pady=5, bg="powder blue", text="Check Credit", variable=var7, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=2, column=1, sticky=W)
		self.chkRestrictMailing = Checkbutton(LeftFrame2L, command=RestrictMailing, pady=5, bg="powder blue", text="TermAgreed", variable=var8, onvalue=1, offvalue=0,font=('arial', 14, 'bold')).grid(row=3, column=1, sticky=W)

		#=========================LEFTFRAME3===============================================================================================
		self.lblTax = Label(LeftFrame3,  fg="black", font=('arial', 16, 'bold'), text="Tax:", padx=2, pady=4, bg="powder blue")
		self.lblTax.grid(row=0, column=0)
		self.txtTax = Entry(LeftFrame3, font=('arial', 16, 'bold'), textvariable=Tax, width=14)
		self.txtTax.grid(row=1, column=0, padx=27, pady=20)

		self.lblSubTotal = Label(LeftFrame3,  fg="black", font=('arial', 16, 'bold'), text="Sub Total:", padx=2, pady=4, bg="powder blue")
		self.lblSubTotal.grid(row=0, column=1)
		self.txtTotal = Entry(LeftFrame3, font=('arial', 16, 'bold'), textvariable=SubTotal, width=14)
		self.txtTotal.grid(row=1, column=1, padx=28, pady=20)

		self.lblTotal = Label(LeftFrame3,  fg="black", font=('arial', 16, 'bold'), text="Total:", padx=2, pady=4, bg="powder blue")
		self.lblTotal.grid(row=0, column=2)
		self.txtTotal = Entry(LeftFrame3, font=('arial', 16, 'bold'), textvariable=Total, width=14)
		self.txtTotal.grid(row=1, column=2, padx=27, pady=20)
		#=========================RIGHTFRAME0===============================================================================================
		self.lblAccountOpened = Label(RightFrame0,  fg="black", font=('arial', 16, 'bold'), text="Accout Opened:", padx=2, pady=4, bg="powder blue")
		self.lblAccountOpened.grid(row=0, column=0, sticky=W, pady=2)
		self.cboAccountOpened = ttk.Combobox(RightFrame0, font=('arial', 16, 'bold'), textvariable=AccountOpened, width=20, state='readonly')
		self.cboAccountOpened['value'] = ('',"")
		self.cboAccountOpened.current(0)
		self.cboAccountOpened.grid(row=0, column=1, sticky=W, pady=2)

		self.lblApplicationDate = Label(RightFrame0,  fg="black", font=('arial', 16, 'bold'), text="Application Date:", padx=2, pady=4, bg="powder blue")
		self.lblApplicationDate.grid(row=1, column=0, sticky=W, pady=2)
		self.cboApplicationDate = ttk.Combobox(RightFrame0, font=('arial', 16, 'bold'), textvariable=ApplicationDate, width=20, state='readonly')
		self.cboApplicationDate['value'] = ('',"")
		self.cboApplicationDate.current(0)
		self.cboApplicationDate.grid(row=1, column=1, sticky=W, pady=2)

		self.lblNxtCreditRev = Label(RightFrame0,  fg="black", font=('arial', 16, 'bold'), text="Next Credit Revue:", padx=2, pady=4, bg="powder blue")
		self.lblNxtCreditRev.grid(row=2, column=0, sticky=W, pady=2)
		self.cboNxtCreditRev = ttk.Combobox(RightFrame0, font=('arial', 16, 'bold'), textvariable=NxtCreditRev, width=20, state='readonly')
		self.cboNxtCreditRev['value'] = ('',"")
		self.cboNxtCreditRev.current(0)
		self.cboNxtCreditRev.grid(row=2, column=1, sticky=W, pady=2)

		self.lblLstCreditRev = Label(RightFrame0,  fg="black", font=('arial', 16, 'bold'), text="Last Credit Revue:", padx=2, pady=4, bg="powder blue")
		self.lblLstCreditRev.grid(row=3, column=0, sticky=W, pady=2)
		self.cboLstCreditRev = ttk.Combobox(RightFrame0, font=('arial', 16, 'bold'), textvariable=LstCreditRev, width=20, state='readonly')
		self.cboLstCreditRev['value'] = ('',"")
		self.cboLstCreditRev.current(0)
		self.cboLstCreditRev.grid(row=3, column=1, sticky=W, pady=2)

		self.lblDateReview = Label(RightFrame0,  fg="black", font=('arial', 16, 'bold'), text="Date Review:", padx=2, pady=4, bg="powder blue")
		self.lblDateReview.grid(row=4, column=0, sticky=W, pady=2)
		self.cboDateReview = ttk.Combobox(RightFrame0, font=('arial', 16, 'bold'), textvariable=DateReview, width=20, state='readonly')
		self.cboDateReview['value'] = ('',"")
		self.cboDateReview.current(0)
		self.cboDateReview.grid(row=4, column=1, sticky=W, pady=2)
		#=========================TEXT, LABELS, ENTRY WIDGETS===============================================================================================

		self.txtInfo = Text(LeftFrame2R, height=11, width=38, font=('arial', 9, 'bold'))
		self.txtInfo.grid(row=0, column=0, )

		self.txtReceipt = Text(RightFrame1, height=20, width=67, font=('arial', 9, 'bold'))
		self.txtReceipt.grid(row=0, column=0, )
		#=========================BUTTONS===============================================================================================
		self.btnTotal = Button(RightFrame2, command=TotalCost, padx=21, pady=2, bd=4, fg="black",bg="powder blue", width=8, height=2,  font=('arial', 16, 'bold'), text="Total").grid(row=0, column=0)
		self.btnReset = Button(RightFrame2, command=Reset, padx=21, pady=2, bd=4, fg="black",bg="powder blue", width=8, height=2,  font=('arial', 16, 'bold'), text="Reset").grid(row=0, column=1)
		self.btnExit = Button(RightFrame2, command=iExit, padx=21, pady=2, bd=4, fg="black",bg="powder blue", width=8, height=2,  font=('arial', 16, 'bold'), text="Exit").grid(row=0, column=2)









if __name__== '__main__':
	root = Tk()
	application = Inventory (root)
	root.mainloop()