import time
import datetime
from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("payslip system")
root.geometry('1350x700+0+0')

#==============Frames=========================================================
main = Frame(root, width= 1350, height= 700)
main.pack()

Tops = Frame(main, width= 1350, height= 50,bd= 8, relief= "raised")
Tops.pack(side= TOP)

f1 = Frame(main, width= 600, height= 600,bd= 8, relief= "raised")
f1.pack(side= LEFT)
f2 = Frame(main, width= 300, height= 800,bd= 8, relief= "raised")
f2.pack(side= RIGHT)

f1a = Frame(f1, width= 600, height= 200,bd= 10, padx=10, relief= "raised")
f1a.pack(side= TOP)
f1b = Frame(f1, width= 600, height= 300,bd= 10, relief= "ridge")
f1b.pack(side= TOP)

labelInfo= Label(Tops, font=('arial', 60, 'bold'), text="\tPayroll System\t", bd=10 )
labelInfo.grid(row=0, column=0)

#===================================== VARIABLES================================================================================
name = StringVar()
address = StringVar()
employer = StringVar()
IDNum = StringVar()
hours = StringVar()
hourRate = StringVar()
payable = StringVar()
tax = StringVar()
overtime = StringVar()
grosspay = StringVar()
netpay = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()


DateOfOrder.set(time.strftime("%d/%m/%Y"))

#=======================================FUNCTIONS=================================================

def reset():
	name.set("")
	address.set("")
	employer.set("")
	IDNum.set("")
	hours.set("")
	hourRate.set("")
	tax.set("")
	overtime.set("")
	grosspay.set("")
	netpay.set("")
	txtPaySlip.delete("1.0",END)

def EnterInfo():
	txtPaySlip.insert(END, "\t\tPay Slip\n")
	txtPaySlip.insert(END, "Name: \t\t" + name.get() + "\n\n")
	txtPaySlip.insert(END, "ID Number: \t\t" + IDNum.get() + "\n\n")
	txtPaySlip.insert(END, "Address: \t\t" + address.get() + "\n\n")
	txtPaySlip.insert(END, "Employer: \t\t" + employer.get() + "\n\n")
	txtPaySlip.insert(END, "Hours Worked: \t\t" + hours.get() + "\n\n")
	txtPaySlip.insert(END, "Net Payable: \t\t" + netpay.get() + "\n\n")
	txtPaySlip.insert(END, "Wages per hour: \t\t" + hourRate.get() + "\n\n")
	txtPaySlip.insert(END, "Tax paid: \t\t" + tax.get() + "\n\n")
	txtPaySlip.insert(END, "Payable: \t\t" + grosspay.get() + "\n\n")
	#reset()

def weeklyWages():
	hrsWrkPerWeek = float(hours.get())
	wagesPerHour = float(hourRate.get())

	payment = wagesPerHour* hrsWrkPerWeek
	paymentDue = "R", str('%.2f' %(payment))
	payable.set(paymentDue)

	Tax = payment* 0.2
	Taxables="R", str('%0.2f' %(Tax))
	tax.set(Taxables)

	netpayment = payment - float(tax)
	netpayable="R", str('%0.2f' %(netpayment))
	netpay.set(netpayable)

	if hrsWrkPerWeek > 40:
		overTimeH = (hrsWrkPerWeek-40) + wagesPerHour* 1.5
		overTimeHOURS= "R", str('%.2f' % (overTimeH))
		overtime.set(overTimeHOURS)

	elif hrsWrkPerWeek <= 40:
		overtimeP = (hrsWrkPerWeek-40) + wagesPerHour* 1.5
		overTimeHrs= "R", str('%.2f' % (overtimeP))
		overtime.set(overTimeHrs)
	return

def iExit():
	qExit = messagebox.askyesno("payslip system", "Do you want to exit the system")
	if qExit  == 1:
		root.destroy()
		return
#==============================================LABEL WIDGETS===============================================================
labelName= Label(f1a, text="Name", font=('arial', 16, 'bold'), bd=10 ).grid(row=0, column=0, pady=10)
labeladdress= Label(f1a, text="Address", font=('arial', 16, 'bold'), bd=10 ).grid(row=0, column=2, pady=10)
labelEmployer= Label(f1a, text="Employer", font=('arial', 16, 'bold'), bd=10 ).grid(row=1, column=0, pady=10)
labelIDNumber= Label(f1a, text="IDNumber", font=('arial', 16, 'bold'), bd=10 ).grid(row=1, column=2, pady=10)
labelHoursWorked= Label(f1a, text="Hours Worked", font=('arial', 16, 'bold'), bd=10 ).grid(row=2, column=0, pady=10)
labelHourlyRate= Label(f1a, text="Hourly Rate", font=('arial', 16, 'bold'), bd=10 ).grid(row=2, column=2, pady=10)
labeltax= Label(f1a, text="TAX", font=('arial', 16, 'bold'), bd=10 ).grid(row=3, column=0, pady=10)
labelOverTime= Label(f1a, text="Over Time", font=('arial', 16, 'bold'), bd=10 ).grid(row=3, column=2, pady=10)
labelGrossPay= Label(f1a, text="Gross Pay", font=('arial', 16, 'bold'), bd=10 ).grid(row=4, column=0, pady=10)
labelNetPay= Label(f1a, text="NetPay", font=('arial', 16, 'bold'), bd=10 ).grid(row=4, column=2, pady=10)


#===========================================ENTRY WIDGETS=================================================================================
etxtName= Entry(f1a, textvariable=name, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=0, column=1)
etxtAddress= Entry(f1a, textvariable=address, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=0, column=3)
etxtEmployer= Entry(f1a, textvariable=employer, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=1, column=1)
etxtIDNUM= Entry(f1a, textvariable=IDNum, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=1, column=3)
etxthours= Entry(f1a, textvariable=hours, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=2, column=1)
etxthourRate= Entry(f1a, textvariable=hourRate, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=2, column=3)
etxttax= Entry(f1a, textvariable=tax, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=3, column=1)
etxt0vertime= Entry(f1a, textvariable=overtime, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=3,column=3)
etxtgrosspay= Entry(f1a, textvariable=grosspay, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=4, column=1)
etxtnetpay= Entry(f1a, textvariable=netpay, font=('arial', 16, 'bold'), bd=8, width=20, justify='left').grid(row=4, column=3)

#===========================================TEXT WIDGETS===============================================================================================
labelPaySlip= Label(f2, textvariable=DateOfOrder, font=('arial', 20, 'bold')).grid(row=0, column=0)
txtPaySlip= Text(f2, height = 25, width=30, bd=6, font=('arial', 12, 'bold'))
txtPaySlip.grid(row=1, column=0)


#============================================BUTTONS=========================================================================================
btnSalary= Button(f1b, text='Weekly Salary', padx=16, pady=16, bd=8, fg='black', font=('arial', 16, 'bold'), width=12, height=1, command=weeklyWages).grid(row=0, column=0)
btnReset= Button(f1b, text='Reset', padx=16, pady=16, bd=8, fg='black', font=('arial', 16, 'bold'), width=12, height=1, command= reset).grid(row=0, column=1)
btnPayslip= Button(f1b, text='View Payslip', padx=16, pady=16, bd=8, fg='black', font=('arial', 16, 'bold'), width=12, height=1, command=EnterInfo).grid(row=0, column=2)
btnExit= Button(f1b, text='Exit System', padx=16, pady=16, bd=8, fg='black', font=('arial', 16, 'bold'), width=12, height=1, command= iExit).grid(row=0, column=3)


root.mainloop()

