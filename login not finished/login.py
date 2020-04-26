from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
from datetime import datetime


def main():
	root = Tk()
	app = Window1(root)
	root.mainloop()


#==============MAIN WINDOW=====================================================================
class Window1:
	def __init__(self, master):
		self.master = master
		self.master.title('Pharmacy Login System')
		self.master.geometry('1350x750+0+0')
		self.frame = Frame(self.master)
		self.frame.pack()

		#===============VARIABLES============================================================================
		self.Username = StringVar()
		self.Password = StringVar()

		#==============WINDOW TITLE==============================================================================================
		self.LabelTitle = Label(self.frame, text='Pharmacy Login System', font=('arial', 50, 'bold'), bd=20)
		self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=40)

		#==============LOGIN BUTTON==============================================================================================

		self.LoginFrame1 = Frame(self.frame, width=1000, height=300, relief='ridge', bd=20)
		self.LoginFrame1.grid(row=1, column=0)

		self.LoginFrame2 = Frame(self.frame, width=1000, height=100, relief='ridge', bd=20)
		self.LoginFrame2.grid(row=2, column=0)

		self.LoginFrame3 = Frame(self.frame, width=1000, height=200, relief='ridge', bd=20)
		self.LoginFrame3.grid(row=3, column=0, pady=2)

		#===============CREDENTIALS============================================================================================

		self.LabelUsername = Label(self.LoginFrame1, text='Username', font=('arial', 30, 'bold'), bd=22)
		self.LabelUsername.grid(row=0, column=0)
		self.txtUsername = Entry(self.LoginFrame1, textvariable=self.Username, font=('arial', 30, 'bold'), bd=22)
		self.txtUsername.grid(row=0, column=1,pady=8, padx=15)

		self.LabelPassword = Label(self.LoginFrame1, text='Password', font=('arial', 30, 'bold'), bd=22)
		self.LabelPassword.grid(row=1, column=0)
		self.txtPassword = Entry(self.LoginFrame1, show="*", textvariable=self.Password, font=('arial', 30, 'bold'), bd=22)
		self.txtPassword.grid(row=1, column=1,pady=8, padx=85)

		self.btnlogin = Button(self.LoginFrame2, text="Log In", width=17, font=('arial', 20, 'bold'), command= self.Login_System)
		self.btnlogin.grid(row=0, column=0)
		self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('arial', 20, 'bold'), command= self.Reset)
		self.btnReset.grid(row=0, column=1 )
		self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('arial', 20, 'bold'), command= self.iExit)
		self.btnExit.grid(row=0, column=2 )


		#==============APPLICATIONS BUTTON==============================================================================================

		self.btnRegistration = Button(self.LoginFrame3, state= DISABLED, text="Patient Registration System", font=('arial', 20, 'bold'), command= self.Registration_window)
		self.btnRegistration.grid(row=0, column=0, pady=8, padx=22)
		self.btnHospital = Button(self.LoginFrame3,  state= DISABLED, text="Hospital Management System", font=('arial', 20, 'bold'), command= self.Hospital_window)
		self.btnHospital.grid(row=0, column=1, pady=8, padx=22)
		
		#===============DETAILS============================================================================================

	def Login_System(self):
			user = (self.Username.get())
			pasw = (self.Password.get())

			if (user == str(12)) and  (pasw == str(12)):
				self.btnRegistration.config(state = NORMAL)
				self.btnHospital.config(state = NORMAL)

			else :
				messagebox.showwarning("Pharmacy Login System", "You have entered invalid details!")
				self.btnRegistration.config(state = DISABLED)
				self.btnHospital.config(state = DISABLED)
				self.Username.set("")
				self.Password.set("")
				self.txtUsername.focus()

	def Reset(self):
		self.btnRegistration.config(state = DISABLED)
		self.btnHospital.config(state = DISABLED)
		self.Username.set("")
		self.Password.set("")
		self.txtUsername.focus()

	def iExit(self):
			qExit = messagebox.askyesno("Pharmacy Login System", "Do you want to EXIT the system")
			if qExit  == 1:
				self.master.destroy()
				return




	#===============CREDENTIALS============================================================================================

	def Registration_window(self):
		self.newWindow = Toplevel(self.master)
		self.app = Window2(self.newWindow)

	def Hospital_window(self):
		self.newWindow = Toplevel(self.master)
		self.app = Window3(self.newWindow)




#==============WINDOWS/APPLICATONS==============================================================================================
#==============self.frameCULATOR/APPLICATONS==============================================================================================

class Window2:         #the other app window
	def __init__(self, master):
		self.master = master
		self.master.title('Patient Registration System')
		self.master.geometry("360x490+0+0")
		self.frame = Frame(self.master)
		self.frame.pack()
#===================================================================================================
		operator=""
		self.operator= operator
		text_Input =StringVar()
		self.text_Input = text_Input
		numbers=IntVar()
		self.numbers = numbers



		self.txtDisplay = Entry(self.frame, font=('arial', 20, 'bold'), textvariable=self.text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)


		def btnClick(numbers):
			
			self.operator= self.operator + str(numbers)
			self.text_Input.set(operator)

		def btnClearDisplay(self):
			global operator
			operator=""
			text_Input.set("")

		def btnEqualsInput(self):
			global operator
			sumUp=str(eval(operator))
			text_Input.set(sumUp)
			operator=""

		#================================================================================================================================================================
		btn7=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:self.btnClick(7), text="7").grid(row=1, column=0)
		btn8=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(8), text="8").grid(row=1, column=1)
		btn9=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(9), text="9").grid(row=1, column=2)
		Addition=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("+"), text="+").grid(row=1, column=3)

		#================================================================================================================================================================
		btn4=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(4), text="4").grid(row=2, column=0)
		btn5=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(5), text="5").grid(row=2, column=1)
		btn6=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(6), text="6").grid(row=2, column=2)
		Subtraction=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("-"), text="-").grid(row=2, column=3)

		#================================================================================================================================================================
		btn1=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(1), text="1").grid(row=3, column=0)
		btn2=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(2), text="2").grid(row=3, column=1)
		btn3=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(3), text="3").grid(row=3, column=2)
		Multiply=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("*"), text="*").grid(row=3, column=3)

		#================================================================================================================================================================
		btn0=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(0), text="0").grid(row=4, column=0)
		Clear=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command= btnClearDisplay, text="C").grid(row=4, column=1)
		Equal=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=btnEqualsInput, text="=").grid(row=4, column=2)
		Divide=Button(self.frame,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("/"), text="/").grid(row=4, column=3)



#==============CAFE/APPLICATONS==============================================================================================

class Window3:
	def __init__(self, master):
		self.master = master
		self.master.title('Hospital Management System')
		self.master.geometry('1350x750+0+0')
		self.frame = Frame(self.master)
		self.frame.pack()


#=============APP================================================

		TopFrame = Frame(self.frame, bd=14, width=1350, height=550, padx=30,relief=RIDGE, bg="cadet blue")
		TopFrame.grid(row=0, column=0, sticky=W)

		LeftFrame = Frame(TopFrame, bd=10, width=450, height=550, padx=8,relief=RIDGE, bg="powder blue")
		LeftFrame.grid(row=0, column=0)

		RightFrame = Frame(TopFrame, bd=10, width=800, height=550, padx=0,relief=RIDGE, bg="cadet blue")
		RightFrame.grid(row=0, column=1)

		BottomFrame = Frame(self.frame, bd=10, width=1350, height=150, padx=2,relief=RAISED, bg="powder blue")
		BottomFrame.grid(row=1, column=0, sticky=W)

		#=========FUNCTIONS======================================================================
		def iExit():
			qExit = messagebox.askyesno("Hotel Management System", "Do you want to EXIT the system")
			if qExit  == 1:
				self.master.destroy()
				return

		def Receipt():
			self.txtReceipt.insert(END, CustomerRef.get()+"\t"+FirstName.get()+"\t"+ Surname.get()+"\t"+Address.get()+"\t"+PostCode.get()+"\t"+Mobile.get()+"\t"+Nationality.get()+"\t"+CheckInDate.get()+ "\t"+CheckOutDate.get()+"\t"+PaidTax.get()+"\t"+Subtotal.get()+"\t"+TotalCost.get()+ "\n")

		def Reset():
			CustomerRef.set("")
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
			CheckOutDate.set("")
			Meal.set("")
			RoomType.set("")
			RoomNo.set("")
			RoomExtNo.set("")
			TotalCost.set("")
			Subtotal.set("")
			PaidTax.set("")
			TotalDays.set("")
			self.txtReceipt.delete("1.0",END)

		def TotalCostandDate():
			InDate = CheckInDate.get()
			OutDate = CheckOutDate.get()
			InDate = datetime.strptime(InDate, "%d/%m/%Y")
			OutDate = datetime.strptime(OutDate, "%d/%m/%Y")
			TotalDays.set(abs((OutDate - InDate).days))

			
			#=========Breakfast=====================================
			if (Meal.get() == "Breakfast" and RoomType.get() == "Single"):
				q1 = float(17)
				q2 = float(34)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Breakfast" and RoomType.get() == "Double"):
				q1 = float(35)
				q2 = float(43)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Breakfast" and RoomType.get() == "Family"):
				q1 = float(45)
				q2 = float(63)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			#=========LUNCH=====================================
			elif (Meal.get() == "Lunch" and RoomType.get() == "Single"):
				q1 = float(29)
				q2 = float(39)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Lunch" and RoomType.get() == "Double"):
				q1 = float(39)
				q2 = float(53)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Lunch" and RoomType.get() == "Family"):
				q1 = float(49)
				q2 = float(73)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			#=========LUNCH=====================================
			elif (Meal.get() == "Dinner" and RoomType.get() == "Single"):
				q1 = float(29)
				q2 = float(35)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Dinner" and RoomType.get() == "Double"):
				q1 = float(39)
				q2 = float(55)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

			elif (Meal.get() == "Dinner" and RoomType.get() == "Family"):
				q1 = float(45)
				q2 = float(75)
				q3 = float(TotalDays.get())
				q4 = float(q1 + q2)
				q5 = float(q3 * q4)
				Tax = "R" + str('%.2f' %((q5) * 0.9))
				ST = "R" + str('%.2f' %((q5)))
				TT = "R" + str('%.2f' %(q5 + (q5) * 0.9))
				PaidTax.set(Tax)
				Subtotal.set(ST)
				TotalCost.set(TT)

		#=========VARIABLES====================================================
		CustomerRef = StringVar()
		FirstName = StringVar()
		Surname =StringVar()
		PostCode = StringVar()
		Address=StringVar()
		PostCode= StringVar()
		Mobile =StringVar()
		Email =StringVar()
		Nationality = StringVar()
		DOB = StringVar()
		IDType =StringVar()
		Gender = StringVar()
		CheckInDate=StringVar()
		CheckOutDate= StringVar()
		Meal =StringVar()
		RoomType =StringVar()
		RoomNo = StringVar()
		RoomExtNo = StringVar()
		TotalCost =StringVar()
		Subtotal = StringVar()
		PaidTax=StringVar()
		TotalDays= StringVar()

		#========WIDGET===================================================================================================
		self.lblCustomer_Ref = Label(LeftFrame, font=('arial', 12, 'bold'), text="Customer Ref:", padx=2, bg="powder blue")
		self.lblCustomer_Ref.grid(row=0, column=0, sticky=W)
		self.lblCustomer_Ref = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=CustomerRef, width=20)
		self.lblCustomer_Ref.grid(row=0, column=1, padx=10, pady=3)

		self.lblFirstName = Label(LeftFrame, font=('arial', 12, 'bold'), text="First Name:", padx=2, bg="powder blue")
		self.lblFirstName.grid(row=1, column=0, sticky=W)
		self.lblFirstName = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=FirstName, width=20)
		self.lblFirstName.grid(row=1, column=1, padx=10, pady=3)

		self.lblSurname = Label(LeftFrame, font=('arial', 12, 'bold'), text="Surname:", padx=2, bg="powder blue")
		self.lblSurname.grid(row=2, column=0, sticky=W)
		self.lblSurname = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=Surname, width=20)
		self.lblSurname.grid(row=2, column=1, padx=10, pady=3)

		self.lblAddress = Label(LeftFrame, font=('arial', 12, 'bold'), text="Address:", padx=2, bg="powder blue")
		self.lblAddress.grid(row=3, column=0, sticky=W)
		self.lblAddress = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=Address, width=20)
		self.lblAddress.grid(row=3, column=1, padx=10, pady=3)

		self.lblPostCode = Label(LeftFrame, font=('arial', 12, 'bold'), text="Post Code:", padx=2, bg="powder blue")
		self.lblPostCode.grid(row=4, column=0, sticky=W)
		self.lblPostCode = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=PostCode, width=20)
		self.lblPostCode.grid(row=4, column=1, padx=10, pady=3)

		self.lblMobile = Label(LeftFrame, font=('arial', 12, 'bold'), text="Mobile:", padx=2, bg="powder blue")
		self.lblMobile.grid(row=5, column=0, sticky=W)
		self.lblMobile = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=Mobile, width=20)
		self.lblMobile.grid(row=5, column=1, padx=10, pady=3)

		self.lblEmail = Label(LeftFrame, font=('arial', 12, 'bold'), text="Email:", padx=2, bg="powder blue")
		self.lblEmail.grid(row=6, column=0, sticky=W)
		self.lblEmail = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=Email, width=20)
		self.lblEmail.grid(row=6, column=1, padx=10, pady=3)

		self.lblNationality = Label(LeftFrame, font=('arial', 12, 'bold'), text="Nationality:", padx=2, bg="powder blue")
		self.lblNationality.grid(row=7, column=0, sticky=W)
		self.cboNationality = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=Nationality, width=18, state='readonly')
		self.cboNationality['value'] = ('', 'British', 'RSA', 'Kenyan', 'Indian', 'Iranian','Canadian')
		self.cboNationality.current(0)
		self.cboNationality.grid(row=7, column=1, padx=10, pady=3)

		self.lblDOB = Label(LeftFrame, font=('arial', 12, 'bold'), text="Date Of Birth:", padx=2, bg="powder blue")
		self.lblDOB.grid(row=8, column=0, sticky=W)
		self.txtDOB = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=DOB, width=20)
		self.txtDOB.grid(row=8, column=1, padx=10, pady=3)

		self.lblIDType = Label(LeftFrame, font=('arial', 12, 'bold'), text="Type  of ID:", padx=2, bg="powder blue")
		self.lblIDType.grid(row=9, column=0, sticky=W)
		self.cboIDType = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=IDType, width=18, state='readonly')
		self.cboIDType['value'] = ('', 'ID Book', 'Drivers License', 'Pilots License', 'Student ID', 'Passport')
		self.cboIDType.current(0)
		self.cboIDType.grid(row=9, column=1, padx=0, pady=3)

		self.lblGender = Label(LeftFrame, font=('arial', 12, 'bold'), text="Gender:", padx=2, bg="powder blue")
		self.lblGender.grid(row=10, column=0, sticky=W)
		self.cboGender = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=Gender, width=18, state='readonly')
		self.cboGender['value'] = ('', 'MALE', 'FEMALE')
		self.cboGender.current(0)
		self.cboGender.grid(row=10, column=1, padx=10, pady=3)

		self.lblCheckInDate = Label(LeftFrame, font=('arial', 12, 'bold'), text="Check In Date:", padx=2, bg="powder blue")
		self.lblCheckInDate.grid(row=11, column=0, sticky=W)
		self.txtCheckInDate = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=CheckInDate, width=20)
		self.txtCheckInDate.grid(row=11, column=1, padx=10, pady=3)

		self.lblCheckOutDate = Label(LeftFrame, font=('arial', 12, 'bold'), text="Check Out Date:", padx=2, bg="powder blue")
		self.lblCheckOutDate.grid(row=12, column=0, sticky=W)
		self.txtCheckOutDate = Entry(LeftFrame, font=('arial', 12, 'bold'), textvariable=CheckOutDate, width=20)
		self.txtCheckOutDate.grid(row=12, column=1, padx=10, pady=3)

		self.lblMeal = Label(LeftFrame, font=('arial', 12, 'bold'), text="Meal:", padx=2, bg="powder blue")
		self.lblMeal.grid(row=13, column=0, sticky=W)
		self.cboMeal = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=Meal, width=18, state='readonly')
		self.cboMeal['value'] = ('', 'Breakfast', 'Lunch', 'Dinner')
		self.cboMeal.current(0)
		self.cboMeal.grid(row=13, column=1, padx=10, pady=3)

		self.lblRoomType = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room Type:", padx=2, bg="powder blue")
		self.lblRoomType.grid(row=14, column=0, sticky=W)
		self.cboRoomType = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=RoomType, width=18, state='readonly')
		self.cboRoomType['value'] = ('', 'Single', 'Double', 'Family')
		self.cboRoomType.current(0)
		self.cboRoomType.grid(row=14, column=1, padx=10, pady=3)

		self.lblRoomNo = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room Number:", padx=2, bg="powder blue")
		self.lblRoomNo.grid(row=15, column=0, sticky=W)
		self.cboRoomNo = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=RoomNo, width=18, state='readonly')
		self.cboRoomNo['value'] = ('', '01', '02', '03','04','05','06','07','08','09')
		self.cboRoomNo.current(0)
		self.cboRoomNo.grid(row=15, column=1, padx=10, pady=3)

		self.lblRoomExtNo = Label(LeftFrame, font=('arial', 12, 'bold'), text="Room Number:", padx=2, bg="powder blue")
		self.lblRoomExtNo.grid(row=16, column=0, sticky=W)
		self.cboRoomExtNo = ttk.Combobox(LeftFrame, font=('arial', 12, 'bold'), textvariable=RoomExtNo, width=18, state='readonly')
		self.cboRoomExtNo['value'] = ('', '101', '102', '103','104','105','106','107','108','109')
		self.cboRoomExtNo.current(0)
		self.cboRoomExtNo.grid(row=16, column=1, padx=10, pady=3)

				#=====================RECEIPT==============================================================
		self.lblLABEL = Label(RightFrame, font=('arial', 10, 'bold'), text="Ref #\tFirst Name\tSurname\tAddress\tPostCode\tMobile\tNationality\tCheckInDate\tCheckOutDate", pady=5, bg="cadet blue")
		self.lblLABEL.grid(row=0, columnspan=10)

		self.txtReceipt = Text(RightFrame, height=15, width=100, bd=10, font=('arial', 11, 'bold'))
		self.txtReceipt.grid(row=1, column=0,columnspan=20, pady=2)
		#=====================RECEIPT==============================================================
		self.lblDays = Label(RightFrame, font=('arial', 14, 'bold'), text="No of days:", bd=7, bg="cadet blue", fg="black")
		self.lblDays.grid(row=2, column=0, sticky=W)
		self.txtDays = Entry(RightFrame, font=('arial', 14, 'bold'), textvariable=TotalDays, bd=7, bg="white", width=60, justify=LEFT)
		self.txtDays.grid(row=2, column=1)

		self.lblPaidTax = Label(RightFrame, font=('arial', 14, 'bold'), text="Paid Tax:", bd=7, bg="cadet blue", fg="black")
		self.lblPaidTax.grid(row=3, column=0, sticky=W)
		self.txtPaidTax = Entry(RightFrame, font=('arial', 14, 'bold'), textvariable=PaidTax, bd=7, bg="white", width=60, justify=LEFT)
		self.txtPaidTax.grid(row=3, column=1)

		self.lblSubTotal = Label(RightFrame, font=('arial', 14, 'bold'), text="Sub Total:", bd=7, bg="cadet blue", fg="black")
		self.lblSubTotal.grid(row=4, column=0, sticky=W)
		self.txtSubTotal = Entry(RightFrame, font=('arial', 14, 'bold'), textvariable=Subtotal, bd=7, bg="white", width=60, justify=LEFT)
		self.txtSubTotal.grid(row=4, column=1)

		self.lblTotalCost = Label(RightFrame, font=('arial', 14, 'bold'), text="Total Cost:", bd=7, bg="cadet blue", fg="black")
		self.lblTotalCost.grid(row=5, column=0, sticky=W)
		self.txtTotalCost = Entry(RightFrame, font=('arial', 14, 'bold'), textvariable=TotalCost, bd=7, bg="white", width=60, justify=LEFT)
		self.txtTotalCost.grid(row=5, column=1)
		
		#===============BUTTONS=============================================================================================
		self.btnTotal= Button(BottomFrame, text='Total', padx=16, pady=1, bd=4, fg='black', bg="powder blue", font=('arial', 16, 'bold'), width=20, height=2, command=TotalCostandDate).grid(row=0, column=4, padx=6)
		self.btnReceipt= Button(BottomFrame, text='Receipt', padx=16, pady=1, bd=4, fg='black', bg="powder blue", font=('arial', 16, 'bold'), width=20, height=2, command=Receipt).grid(row=0, column=5, padx=6)
		self.btnReset= Button(BottomFrame, text='Reset', padx=16, pady=1, bd=4, fg='black', bg="powder blue", font=('arial', 16, 'bold'), width=20, height=2, command=Reset).grid(row=0, column=6, padx=6)
		self.btnExit= Button(BottomFrame, text='Exit', padx=16, pady=1, bd=4, fg='black', bg="powder blue", font=('arial', 16, 'bold'), width=20, height=2, command=iExit).grid(row=0, column=7, padx=6)



if __name__ == '__main__':    #main loop function defined at the top
	main()

