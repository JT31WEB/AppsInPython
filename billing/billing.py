from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
from datetime import datetime

class Customer:
	def __init__(self, root):
		self.root = root
		self.root.title("Customer Billing System")
		self.root.geometry('1350x750+0+0')
		self.root.config(background="powder blue")

		#=========FRAMES=====================================================================
		ABC = Frame(self.root, bg="powder blue", bd=20, relief=RIDGE)
		ABC.grid()

		ABC1 = Frame(ABC, bd=10, width=1250, height=100,  bg="powder blue", relief=RIDGE)
		ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
		ABC2 = Frame(ABC, bd=10, width=430, height=488,  bg="cadet blue", relief=RIDGE, padx=15)
		ABC2.grid(row=1, column=0, sticky=W)
		ABC3 = Frame(ABC, bd=10, width=430, height=488,  bg="powder blue", relief=RIDGE, padx=15)
		ABC3.grid(row=1, column=1, sticky=W)
		ABC4 = Frame(ABC, bd=10, width=430, height=488,  bg="cadet blue", relief=RIDGE, padx=5)
		ABC4.grid(row=1, column=2, sticky=W)
		ABC5 = Frame(ABC4, bd=10, width=380, height=340,  bg="cadet blue", relief=RIDGE)
		ABC5.grid(row=0, column=0, sticky=W)
		ABC6 = Frame(ABC4, bd=10, width=370, height=120,  bg="cadet blue", relief=RIDGE)
		ABC6.grid(row=1, column=0, columnspan=4, sticky=W)

		Date1 =StringVar()
		Time1 = StringVar()
		Date1.set(time.strftime("%d/%m/%Y"))
		Time1.set(time.strftime("%H:%M:%S"))

		self.lilTitle = Label(ABC1, fg="white" , textvariable=Date1,  font=('arial', 30, 'bold'), pady=9, bd=5, bg="cadet blue").grid(row=0, column=0)
		self.lilTitle = Label(ABC1, fg="white" , justify=CENTER, text="\tCustomer Billing System                  ",  font=('arial', 30, 'bold'), pady=9, bd=5, bg="cadet blue").grid(row=0, column=1)
		self.lilTitle = Label(ABC1, fg="white" , textvariable=Time1,  font=('arial', 30, 'bold'), pady=9, bd=5, bg="cadet blue").grid(row=0, column=2)
		
		#==============VARIABLESS===============================================================================================
		CustomerRef = StringVar()
		FirstName = StringVar()
		Surname =StringVar()
		PostCode = StringVar()
		Address=StringVar()
		Mobile =StringVar()
		Email =StringVar()
		Nationality = StringVar()
		DOB = StringVar()
		IDType =StringVar()
		Gender = StringVar()
		CheckInDate=StringVar()
		CheckInTime= StringVar()
		Meal =StringVar()
		RoomType =StringVar()
		RoomNo = StringVar()
		RoomExtNo = StringVar()
		TotalCost =StringVar()
		Subtotal = StringVar()
		PaidTax=StringVar()
		TotalDays= StringVar()
		
		x = random.randint(10908, 500876)
		randomRef = str(x)
		CustomerRef.set("A_" + randomRef)

		E_latte = StringVar()
		E_Expresso = StringVar()
		E_IcedTea = StringVar()
		E_ValeCoffee = StringVar()
		E_Cuppucchino = StringVar()
		E_AfricanCoffee = StringVar()
		E_AmericanCoffee = StringVar()
		E_IcedCuppucchino = StringVar()

		var1 = IntVar()
		var2 = IntVar()
		var3 = IntVar()
		var4 = IntVar()
		var5 = IntVar()
		var6 = IntVar()
		var7 = IntVar()
		var8 = IntVar()

		var1.set("0")
		var2.set("0")
		var3.set("0")
		var4.set("0")
		var5.set("0")
		var6.set("0")
		var7.set("0")
		var8.set("0")

		E_latte.set("")
		E_Expresso.set("")
		E_IcedTea.set("")
		E_ValeCoffee.set("")
		E_Cuppucchino.set("")
		E_AfricanCoffee.set("")
		E_AmericanCoffee.set("")
		E_IcedCuppucchino.set("")

		FirstName.set("")
		Surname.set("")
		PostCode.set("")
		Address.set("")
		PostCode.set("")
		Mobile.set("")
		Email.set("")
		Nationality.set("")
		DOB.set("")
		IDType.set("")
		Gender.set("")
		CheckInDate.set("")
		CheckInTime.set("")
		Meal.set("")
		RoomType.set("")
		RoomNo.set("")
		RoomExtNo.set("")
		TotalCost.set("")
		Subtotal.set("")
		PaidTax.set("")
		


		#==============functionS============================================================================
		def iExit():
			qExit = messagebox.askyesno("Customer Billing System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

		def chkButton_value():
			if (var1.get() == 1):
				self.txtlatte.configure(state = NORMAL)
				self.txtlatte.configure(background= "powder blue")
				self.txtlatte.focus()
			elif (var1.get() == 0):
				self.txtlatte.configure(state = DISABLED)
				E_latte.set("0")                                     #put 'INT' in for calculation

			if (var2.get() == 1):
				self.txtExpresso.configure(state = NORMAL)
				self.txtExpresso.configure(background= "powder blue")
				self.txtExpresso.focus()
			elif (var2.get() == 0):
				self.txtExpresso.configure(state = DISABLED)
				E_Expresso.set("0")

			if (var3.get() == 1):
				self.txtIcedTea.configure(state = NORMAL)
				self.txtIcedTea.configure(background= "powder blue")
				self.txtIcedTea.focus()
			elif (var3.get() == 0):
				self.txtIcedTea.configure(state = DISABLED)
				E_IcedTea.set("0")

			if (var4.get() == 1):
				self.txtValeCoffee.configure(state = NORMAL)
				self.txtValeCoffee.configure(background= "powder blue")
				self.txtValeCoffee.focus()
			elif (var4.get() == 0):
				self.txtValeCoffee.configure(state = DISABLED)
				E_ValeCoffee.set("0")

			if (var5.get() == 1):
				self.txtCuppucchino.configure(state = NORMAL)
				self.txtCuppucchino.configure(background= "powder blue")
				self.txtCuppucchino.focus()
			elif (var5.get() == 0):
				self.txtCuppucchino.configure(state = DISABLED)
				E_Cuppucchino.set("0")

			if (var6.get() == 1):
				self.txtAfricanCoffee.configure(state = NORMAL)
				self.txtAfricanCoffee.configure(background= "powder blue")
				self.txtAfricanCoffee.focus()
			elif (var6.get() == 0):
				self.txtAfricanCoffee.configure(state = DISABLED)
				E_AfricanCoffee.set("0")

			if (var7.get() == 1):
				self.txtAmericanCoffee.configure(state = NORMAL)
				self.txtAmericanCoffee.configure(background= "powder blue")
				self.txtAmericanCoffee.focus()
			elif (var7.get() == 0):
				self.txtAmericanCoffee.configure(state = DISABLED)
				E_AmericanCoffee.set("0")

			if (var8.get() == 1):
				self.txtIcedCuppucchino.configure(state = NORMAL)
				self.txtIcedCuppucchino.configure(background= "powder blue")
				self.txtIcedCuppucchino.focus()
			elif (var8.get() == 0):
				self.txtIcedCuppucchino.configure(state = DISABLED)
				E_IcedCuppucchino.set("0")

		def Reset():
			E_latte.set("")
			E_Expresso.set("")
			E_IcedTea.set("")
			E_ValeCoffee.set("")
			E_Cuppucchino.set("")
			E_AfricanCoffee.set("")
			E_AmericanCoffee.set("")
			E_IcedCuppucchino.set("")
			self.txtReceipt.delete("1.0", END)

			Date1.set(time.strftime("%d/%m/%Y"))
			Time1.set(time.strftime("%H:%M:%S"))


			x = random.randint(10908, 500876)
			randomRef = str(x)
			CustomerRef.set("A_" + randomRef)
			

			var1.set(0)
			var2.set(0)
			var3.set(0)
			var4.set(0)
			var5.set(0)
			var6.set(0)
			var7.set(0)
			var8.set(0)
			
			self.txtlatte.configure(state= DISABLED)
			self.txtExpresso.configure(state= DISABLED)
			self.txtIcedTea.configure(state= DISABLED)
			self.txtValeCoffee.configure(state= DISABLED)
			self.txtCuppucchino.configure(state= DISABLED)
			self.txtAfricanCoffee.configure(state= DISABLED)
			self.txtAmericanCoffee.configure(state= DISABLED)
			self.txtIcedCuppucchino.configure(state= DISABLED)

			
			FirstName.set("")
			Surname.set("")
			PostCode.set("")
			Address.set("")
			PostCode.set("")
			Mobile.set("")
			Email.set("")
			Nationality.set("")
			DOB.set("")
			IDType.set("")
			Gender.set("")
			CheckInDate.set("")
			CheckInTime.set("")
			Meal.set("")
			RoomType.set("")
			RoomNo.set("")
			RoomExtNo.set("")
			TotalCost.set("")
			Subtotal.set("")
			PaidTax.set("")
			TotalDays.set("")
		

		def costOfItem():
			CustomerRef.set("A_" + randomRef)
			Item1 =  float(E_latte.get())
			Item2 =  float(E_Expresso.get())
			Item3 =  float(E_IcedTea.get())
			Item4 =  float(E_ValeCoffee.get())
			Item5 =  float(E_Cuppucchino.get())
			Item6 =  float(E_AfricanCoffee.get())
			Item7 =  float(E_AmericanCoffee.get())
			Item8 =  float(E_IcedCuppucchino.get())

			PriceOfDrinks =(Item1 * 12) + (Item2 * 15) + (Item3 * 30) + (Item4 * 10) + (Item5 * 35) + (Item6 * 30) + (Item7 * 10) + (Item8 * 35)

			SubTotalofItems = "R", str('%.2f'%(PriceOfDrinks))
			Subtotal.set(SubTotalofItems)

			Tax = "R", str('%.2f'%((PriceOfDrinks)* 0.15))
			PaidTax.set(Tax)

			TTax = ((PriceOfDrinks)* 0.15)
			TCost = "R", str('%.2f'%(PriceOfDrinks + TTax))
			TotalCost.set(TCost)

			self.txtReceipt.insert(END, 'ITEMS\t\t' + 'Customer Ref#:\t\t' + CustomerRef.get() + "\n")
			self.txtReceipt.insert(END, "============================== \n\n")
			self.txtReceipt.insert(END, ' Latte:\t\t\t\t' + E_latte.get() + "\n")
			self.txtReceipt.insert(END, ' Expresso:\t\t\t\t' + E_Expresso.get() + "\n")
			self.txtReceipt.insert(END, ' Iced Tea:\t\t\t\t' + E_IcedTea.get() + "\n")
			self.txtReceipt.insert(END, ' Vale Coffee:\t\t\t\t' + E_ValeCoffee.get() + "\n")
			self.txtReceipt.insert(END, ' Cuppucchino:\t\t\t\t' + E_Cuppucchino.get() + "\n")
			self.txtReceipt.insert(END, ' African Coffee:\t\t\t\t' + E_AfricanCoffee.get() + "\n")
			self.txtReceipt.insert(END, ' American Coffee:\t\t\t\t' + E_AmericanCoffee.get() + "\n")
			self.txtReceipt.insert(END, ' Iced Cuppucchino:\t\t\t\t' + E_IcedCuppucchino.get() + "\n")
			self.txtReceipt.insert(END, "============================== \n\n")
			self.txtReceipt.insert(END, "Cost of Items\n\n")

			self.txtReceipt.insert(END, 'Tax Paid:\t\t\t' + str(PaidTax.get()) + "\n")
			self.txtReceipt.insert(END, 'SubTotal:\t\t\t' + str(Subtotal.get()) + "\n")
			self.txtReceipt.insert(END, 'Total Cost:\t\t\t' +  str(TotalCost.get()) + "\n\n\n")


		#==============ORDER SECTION===================================================================================================================
		self.lblCust_Ref =Label(ABC2, fg="white" , text="Customer Ref:",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblCust_Ref.grid(row=0, column=0, sticky= W)
		self.txtCust_Ref = Entry(ABC2, state = DISABLED, font=('arial', 12, 'bold'), textvariable=CustomerRef, width=20)
		self.txtCust_Ref.grid(row=0, column=1, padx=20, pady=3)

		self.lblFirstName =Label(ABC2, fg="white" , text="First Name",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblFirstName.grid(row=1, column=0, sticky= W)
		self.txtFirstName = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=FirstName, width=20)
		self.txtFirstName.grid(row=1, column=1, padx=20, pady=3)

		self.lblSurname =Label(ABC2, fg="white" , text="Surname",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblSurname.grid(row=2, column=0, sticky= W)
		self.txtSurname = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Surname, width=20)
		self.txtSurname.grid(row=2, column=1, padx=20, pady=3)

		self.lblPostCode =Label(ABC2, fg="white", text="PostCode",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblPostCode.grid(row=3, column=0, sticky= W)
		self.txtPostCode = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=PostCode, width=20)
		self.txtPostCode.grid(row=3, column=1, padx=20, pady=3)

		self.lblAddress =Label(ABC2, fg="white" , text="Address",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblAddress.grid(row=4, column=0, sticky= W)
		self.txtAddress = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Address, width=20)
		self.txtAddress.grid(row=4, column=1, padx=20, pady=3)

		self.lblMobile =Label(ABC2, fg="white" , text="Mobile",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblMobile.grid(row=5, column=0, sticky= W)
		self.txtMobile = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Mobile, width=20)
		self.txtMobile.grid(row=5, column=1, padx=20, pady=3)

		self.lblEmail =Label(ABC2, fg="white" , text="Email",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblEmail.grid(row=6, column=0, sticky= W)
		self.txtEmail = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Email, width=20)
		self.txtEmail.grid(row=6, column=1, padx=20, pady=3)

		self.lblNationality = Label(ABC2,  fg="white", font=('arial', 12, 'bold'), text="Nationality", padx=2, bg="cadet blue")
		self.lblNationality.grid(row=7, column=0, sticky=W)
		self.cboNationality = ttk.Combobox(ABC2, font=('arial', 12, 'bold'), textvariable=Nationality, width=18, state='readonly')
		self.cboNationality['value'] = ('', 'British', 'RSA', 'Kenyan', 'Indian', 'Iranian','Canadian')
		self.cboNationality.current(0)
		self.cboNationality.grid(row=7, column=1, padx=10, pady=3)

		self.lblDOB =Label(ABC2, fg="white" , text="Date of Birth",  font=('arial', 12, 'bold'), padx=2, bg="cadet blue")
		self.lblDOB.grid(row=8, column=0, sticky= W)
		self.txtDOB = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=DOB, width=20)
		self.txtDOB.grid(row=8, column=1, padx=20, pady=3)

		self.lblIDType = Label(ABC2,  fg="white", font=('arial', 12, 'bold'), text="Type  of ID:", padx=2, bg="cadet blue")
		self.lblIDType.grid(row=9, column=0, sticky=W)
		self.cboIDType = ttk.Combobox(ABC2, font=('arial', 12, 'bold'), textvariable=IDType, width=18, state='readonly')
		self.cboIDType['value'] = ('', 'ID Book', 'Drivers License', 'Pilots License', 'Student ID', 'Passport')
		self.cboIDType.current(0)
		self.cboIDType.grid(row=9, column=1, padx=0, pady=3)

		self.lblGender = Label(ABC2, fg="white", font=('arial', 12, 'bold'), text="Gender:", padx=2, bg="cadet blue")
		self.lblGender.grid(row=10, column=0, sticky=W)
		self.cboGender = ttk.Combobox(ABC2, font=('arial', 12, 'bold'), textvariable=Gender, width=18, state='readonly')
		self.cboGender['value'] = ('', 'MALE', 'FEMALE')
		self.cboGender.current(0)
		self.cboGender.grid(row=10, column=1, padx=10, pady=3)

		self.lblCheckInDate = Label(ABC2, fg="white", font=('arial', 12, 'bold'), text="Check In Date:", padx=2, bg="cadet blue")
		self.lblCheckInDate.grid(row=11, column=0, sticky=W)
		self.txtCheckInDate = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Date1, width=20)
		self.txtCheckInDate.grid(row=11, column=1, padx=10, pady=3)

		self.lblCheckInTime = Label(ABC2, fg="white", font=('arial', 12, 'bold'), text="Check In Time:", padx=2, bg="cadet blue")
		self.lblCheckInTime.grid(row=12, column=0, sticky=W)
		self.txtCheckInTime = Entry(ABC2, font=('arial', 12, 'bold'), textvariable=Time1, width=20)
		self.txtCheckInTime.grid(row=12, column=1, padx=10, pady=3)

		self.lblMeal = Label(ABC2, fg="white", font=('arial', 12, 'bold'), text="Meal:", padx=2, bg="cadet blue")
		self.lblMeal.grid(row=13, column=0, sticky=W)
		self.cboMeal = ttk.Combobox(ABC2, font=('arial', 12, 'bold'), textvariable=Meal, width=18, state='readonly')
		self.cboMeal['value'] = ('', 'Breakfast', 'Lunch', 'Dinner')
		self.cboMeal.current(0)
		self.cboMeal.grid(row=13, column=1, padx=10, pady=3)

		self.lblRoomType = Label(ABC2, fg="white", font=('arial', 12, 'bold'), text="Room Type:", padx=2, bg="cadet blue")
		self.lblRoomType.grid(row=14, column=0, sticky=W)
		self.cboRoomType = ttk.Combobox(ABC2, font=('arial', 12, 'bold'), textvariable=RoomType, width=18, state='readonly')
		self.cboRoomType['value'] = ('', 'Single', 'Double', 'Family')
		self.cboRoomType.current(0)
		self.cboRoomType.grid(row=14, column=1, padx=10, pady=3)



		#=================================================================================================================================
		self.lblLatte = Checkbutton(ABC3, command=chkButton_value, text="Latte ", variable=var1, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblLatte.grid(row=0, column=0, sticky=W)
		self.lblExpresso = Checkbutton(ABC3, command=chkButton_value, text="Expresso ", variable=var2, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblExpresso.grid(row=1, column=0, sticky=W)
		self.lblIcedTea = Checkbutton(ABC3, command=chkButton_value, text="Iced Tea ", variable=var3, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblIcedTea.grid(row=2, column=0, sticky=W)
		self.lblValeCoffee = Checkbutton(ABC3, command=chkButton_value, text="Vale Coffee ", variable=var4, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblValeCoffee.grid(row=3, column=0, sticky=W)
		self.lblCuppucchino = Checkbutton(ABC3, command=chkButton_value, text="Cuppucchino ", variable=var5, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblCuppucchino.grid(row=4, column=0, sticky=W)
		self.lblAfricanCoffee = Checkbutton(ABC3, command=chkButton_value, text="African Coffee ", variable=var6, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblAfricanCoffee.grid(row=5, column=0, sticky=W)
		self.lblAmericanCoffee = Checkbutton(ABC3, command=chkButton_value, text="American Coffee ", variable=var7, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblAmericanCoffee.grid(row=6, column=0, sticky=W)
		self.lblIcedCuppucchino = Checkbutton(ABC3, command=chkButton_value, text="Iced Cuppucchino ", variable=var8, onvalue=1, offvalue=0,font=('arial', 18, 'bold'), bg="powder blue")
		self.lblIcedCuppucchino.grid(row=7, column=0, sticky=W)

		self.txtlatte = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_latte  , justify='left', state=DISABLED)
		self.txtlatte.grid(row=0, column=1, sticky=E)
		self.txtExpresso = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_Expresso  , justify='left', state=DISABLED)
		self.txtExpresso.grid(row=1, column=1, sticky=E)
		self.txtIcedTea = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_IcedTea  , justify='left', state=DISABLED)
		self.txtIcedTea.grid(row=2, column=1, sticky=E)
		self.txtValeCoffee = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_ValeCoffee  , justify='left', state=DISABLED)
		self.txtValeCoffee.grid(row=3, column=1, sticky=E)
		self.txtCuppucchino = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_Cuppucchino  , justify='left', state=DISABLED)
		self.txtCuppucchino.grid(row=4, column=1, sticky=E)
		self.txtAfricanCoffee = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_AfricanCoffee  , justify='left', state=DISABLED)
		self.txtAfricanCoffee.grid(row=5, column=1, sticky=E)
		self.txtAmericanCoffee = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_AmericanCoffee  , justify='left', state=DISABLED)
		self.txtAmericanCoffee.grid(row=6, column=1, sticky=E)
		self.txtIcedCuppucchino = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=E_IcedCuppucchino  , justify='left', state=DISABLED)
		self.txtIcedCuppucchino.grid(row=7, column=1, sticky=E)
		#===================TAX AND TOTAL=========================================================================================================
		self.lblFirstName =Label(ABC3, fg="white" , text="Tax and Total Sum", width=20, font=('arial', 20, 'bold'), padx=2, bg="cadet blue")
		self.lblFirstName.grid(row=8, column=0, columnspan=4)
		
		self.lblpaidTax =Label(ABC3, fg="black" , text="Paid Tax", font=('arial', 16, 'bold'), padx=2, bg="powder blue")
		self.lblpaidTax.grid(row=9, column=0, sticky=W)
		self.txtpaidTax = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=PaidTax  , justify='left')
		self.txtpaidTax.grid(row=9, column=1)

		self.lblSubTotal =Label(ABC3, fg="black" , text="Sub Total", font=('arial', 16, 'bold'), padx=2, bg="powder blue")
		self.lblSubTotal.grid(row=10, column=0, sticky=W)
		self.txtSubTotal = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=Subtotal  , justify='left')
		self.txtSubTotal.grid(row=10, column=1)

		self.lblTotalCost =Label(ABC3, fg="black" , text="Total Cost", font=('arial', 16, 'bold'), padx=2, bg="powder blue")
		self.lblTotalCost.grid(row=11, column=0, sticky=W)
		self.txtTotalCost = Entry(ABC3, font=('arial', 16, 'bold'), bd=8, width=10, textvariable=TotalCost  , justify='left')
		self.txtTotalCost.grid(row=11, column=1)



		#================RECEIPT TXT=========================================================================================================================
		self.txtReceipt = Text(ABC5, height=23, width=43, bd=10, font=('arial', 11, 'bold'))
		self.txtReceipt.grid(row=0, column=0, )
		#===============RECEIPT BUTTONS==========================================================================================================================
		self.btnTotal = Button(ABC6, command=costOfItem, padx=14, pady=7, bd=5, fg="black",bg="powder blue", width=6, height=2,  font=('arial', 16, 'bold'), text="Total").grid(row=0, column=0)
		self.btnReset = Button(ABC6, command=Reset, padx=14, pady=7, bd=5, fg="black",bg="powder blue", width=6, height=2,  font=('arial', 16, 'bold'), text="Reset").grid(row=0, column=1)
		self.btnExit = Button(ABC6, command=iExit, padx=14, pady=7, bd=5, fg="black",bg="powder blue", width=6, height=2,  font=('arial', 16, 'bold'), text="Exit").grid(row=0, column=2)



		#=========================================================================================================================================

	



if __name__== '__main__':
	root = Tk()
	application = Customer (root)
	root.mainloop()








