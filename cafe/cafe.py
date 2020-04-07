from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Management System")
root.configure(background='cadet blue')

#===========FRAMES==========================================================
Tops = Frame (root, width=1350, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame (root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (root, width=450, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame (f1, width=900, height=330, bd=8, relief="ridge")
f1a.pack(side=TOP)
f2a = Frame (f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

ft2 = Frame (f2, width=440, height=450, bd=2, relief="raise")
ft2.pack(side=TOP)
fb2 = Frame (f2, width=440, height=250, bd=2, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame (f1a, width=400, height=330, bd=10, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame (f1a, width=400, height=330, bd=10, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame (f2a, width=450, height=330, bd=10, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame (f2a, width=450, height=330, bd=10, relief="raise")
f2ab.pack(side=RIGHT)

Tops.configure(background='cadet blue')
f1.configure(background='powder blue')
f2.configure(background='powder blue')

lblTitle = Label (Tops, font=('arial', 60, 'bold'), text="     Cafe Management System     ", bd=10)
lblTitle.grid(row=0, column=0)

#=============VARIABLES=================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateOfOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostOfCakes = StringVar()
CostOfDrinks = StringVar()
Servicecharge = StringVar()

E_latte = StringVar()
E_Expresso = StringVar()
E_IcedTea = StringVar()
E_ValeCoffee = StringVar()
E_Cuppucchino = StringVar()
E_AfricanCoffee = StringVar()
E_AmericanCoffee = StringVar()
E_IcedCuppucchino = StringVar()

E_CoffeeCake = StringVar()
E_RedVelvetCake = StringVar()
E_BlackForestCake = StringVar()
E_BostonCreamCake = StringVar()
E_LagosChocolateCake = StringVar()
E_KilburnChocolateCake = StringVar()
E_CarltonHillChocolateCake = StringVar()
E_QueensParkChocolateCake = StringVar()

E_latte.set("")
E_Expresso.set("")
E_IcedTea.set("")
E_ValeCoffee.set("")
E_Cuppucchino.set("")
E_AfricanCoffee.set("")
E_AmericanCoffee.set("")
E_IcedCuppucchino.set("")

E_CoffeeCake.set("")
E_RedVelvetCake.set("")
E_BlackForestCake.set("")
E_BostonCreamCake.set("")
E_LagosChocolateCake.set("")
E_KilburnChocolateCake.set("")
E_CarltonHillChocolateCake.set("")
E_QueensParkChocolateCake.set("")

DateOfOrder.set(time.strftime("%d/%m/%Y"))
Receipt_Ref.set("")
PaidTax.set("")
SubTotal.set("")
TotalCost.set("")
CostOfCakes.set("")
CostOfDrinks.set("")
Servicecharge.set("")

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")
var13.set("0")
var14.set("0")
var15.set("0")
var16.set("0")


#==============FUNCTIONS=================================================================================
def getTotal():
	Item1 =  float(E_latte.get())
	Item2 =  float(E_Expresso.get())
	Item3 =  float(E_IcedTea.get())
	Item4 =  float(E_ValeCoffee.get())
	Item5 =  float(E_Cuppucchino.get())
	Item6 =  float(E_AfricanCoffee.get())
	Item7 =  float(E_AmericanCoffee.get())
	Item8 =  float(E_IcedCuppucchino.get())

	Item9 =  float(E_CoffeeCake.get())
	Item10 =  float(E_RedVelvetCake.get())
	Item11 =  float(E_BlackForestCake.get())
	Item12 =  float(E_BostonCreamCake.get())
	Item13 =  float(E_LagosChocolateCake.get())
	Item14 =  float(E_KilburnChocolateCake.get())
	Item15 =  float(E_CarltonHillChocolateCake.get())
	Item16 =  float(E_QueensParkChocolateCake.get())

	PriceOfDrinks =(Item1 * 12) + (Item2 * 15) + (Item3 * 30) + (Item4 * 10) + (Item5 * 35) + (Item6 * 30) + (Item7 * 10) + (Item8 * 35)
	PriceOfCakes =(Item9 * 15) + (Item10 * 25) + (Item11 * 30) + (Item12 * 10) + (Item13 * 35) + (Item14 * 30) + (Item15 * 10) + (Item16 * 35)

	DrinksPrice = "R", str('%.2f'%(PriceOfDrinks))
	CakesPrice = "R", str('%.2f'%(PriceOfCakes))
	CostOfCakes.set(CakesPrice)
	CostOfDrinks.set(DrinksPrice)

	SC = "R", str('%.2f'%(12.99))
	Servicecharge.set(SC)

	SubTotalofItems = "R", str('%.2f'%(PriceOfDrinks + PriceOfCakes + 12.99))
	SubTotal.set(SubTotalofItems)

	Tax = "R", str('%.2f'%((PriceOfDrinks + PriceOfCakes + 12.99)* 0.15))
	PaidTax.set(Tax)

	TT = ((PriceOfDrinks + PriceOfCakes + 12.99)* 0.15)
	TC = "R", str('%.2f'%(PriceOfDrinks + PriceOfCakes + 12.99 + TT))
	TotalCost.set(TC)

def chkButton_value():
	if (var1.get() == 1):
		txtlatte.configure(state = NORMAL)
		txtlatte.configure(background= "powder blue")      #change box color
	elif (var1.get() == 0):
		txtlatte.configure(state = DISABLED)
		E_latte.set("0")                                     #put 'INT' in for calculation

	if (var2.get() == 1):
		txtExpresso.configure(state = NORMAL)
		txtExpresso.configure(background= "powder blue")
	elif (var2.get() == 0):
		txtExpresso.configure(state = DISABLED)
		E_Expresso.set("0")

	if (var3.get() == 1):
		txtIcedTea.configure(state = NORMAL)
		txtIcedTea.configure(background= "powder blue")
	elif (var3.get() == 0):
		txtIcedTea.configure(state = DISABLED)
		E_IcedTea.set("0")

	if (var4.get() == 1):
		txtValeCoffee.configure(state = NORMAL)
		txtValeCoffee.configure(background= "powder blue")
	elif (var4.get() == 0):
		txtValeCoffee.configure(state = DISABLED)
		E_ValeCoffee.set("0")

	if (var5.get() == 1):
		txtCuppucchino.configure(state = NORMAL)
		txtCuppucchino.configure(background= "powder blue")
	elif (var5.get() == 0):
		txtCuppucchino.configure(state = DISABLED)
		E_Cuppucchino.set("0")

	if (var6.get() == 1):
		txtAfricanCoffee.configure(state = NORMAL)
		txtAfricanCoffee.configure(background= "powder blue")
	elif (var6.get() == 0):
		txtAfricanCoffee.configure(state = DISABLED)
		E_AfricanCoffee.set("0")

	if (var7.get() == 1):
		txtAmericanCoffee.configure(state = NORMAL)
		txtAmericanCoffee.configure(background= "powder blue")
	elif (var7.get() == 0):
		txtAmericanCoffee.configure(state = DISABLED)
		E_AmericanCoffee.set("0")

	if (var8.get() == 1):
		txtIcedCuppucchino.configure(state = NORMAL)
		txtIcedCuppucchino.configure(background= "powder blue")
	elif (var8.get() == 0):
		txtIcedCuppucchino.configure(state = DISABLED)
		E_IcedCuppucchino.set("0")

	if (var9.get() == 1):
		txtCoffeeCake.configure(state = NORMAL)
		txtCoffeeCake.configure(background= "powder blue")
	elif (var9.get() == 0):
		txtCoffeeCake.configure(state = DISABLED)
		E_CoffeeCake.set("0")

	if (var10.get() == 1):
		txtRedVelvetCake.configure(state = NORMAL)
		txtRedVelvetCake.configure(background= "powder blue")
	elif (var10.get() == 0):
		txtRedVelvetCake.configure(state = DISABLED)
		E_RedVelvetCake.set("0")

	if (var11.get() == 1):
		txtBlackForestCake.configure(state = NORMAL)
		txtBlackForestCake.configure(background= "powder blue")
	elif (var11.get() == 0):
		txtBlackForestCake.configure(state = DISABLED)
		E_BlackForestCake.set("0")

	if (var12.get() == 1):
		txtBostonCreamCake.configure(state = NORMAL)
		txtBostonCreamCake.configure(background= "powder blue")
	elif (var12.get() == 0):
		txtBostonCreamCake.configure(state = DISABLED)
		E_BostonCreamCake.set("0")

	if (var13.get() == 1):
		txtLagosChocolateCake.configure(state = NORMAL)
		txtLagosChocolateCake.configure(background= "powder blue")
	elif (var13.get() == 0):
		txtLagosChocolateCake.configure(state = DISABLED)
		E_LagosChocolateCake.set("0")

	if (var14.get() == 1):
		txtKilburnChocolateCake.configure(state = NORMAL)
		txtKilburnChocolateCake.configure(background= "powder blue")
	elif (var14.get() == 0):
		txtKilburnChocolateCake.configure(state = DISABLED)
		E_KilburnChocolateCake.set("0")

	if (var15.get() == 1):
		txtCarltonHillChocolateCake.configure(state = NORMAL)
		txtCarltonHillChocolateCake.configure(background= "powder blue")
	elif (var15.get() == 0):
		txtCarltonHillChocolateCake.configure(state = DISABLED)
		E_CarltonHillChocolateCake.set("0")

	if (var16.get() == 1):
		txtQueensParkChocolateCake.configure(state = NORMAL)
		txtQueensParkChocolateCake.configure(background= "powder blue")
	elif (var16.get() == 0):
		txtQueensParkChocolateCake.configure(state = DISABLED)
		E_QueensParkChocolateCake.set("0")



def iExit():
			qExit = messagebox.askyesno("Cafe Management System", "Do you want to EXIT the system")
			if qExit  == 1:
				root.destroy()
				return

def Reset():
	E_latte.set("")
	E_Expresso.set("")
	E_IcedTea.set("")
	E_ValeCoffee.set("")
	E_Cuppucchino.set("")
	E_AfricanCoffee.set("")
	E_AmericanCoffee.set("")
	E_IcedCuppucchino.set("")

	E_CoffeeCake.set("")
	E_RedVelvetCake.set("")
	E_BlackForestCake.set("")
	E_BostonCreamCake.set("")
	E_LagosChocolateCake.set("")
	E_KilburnChocolateCake.set("")
	E_CarltonHillChocolateCake.set("")
	E_QueensParkChocolateCake.set("")

	DateOfOrder.set(time.strftime("%d/%m/%Y"))
	Receipt_Ref.set("")
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	CostOfCakes.set("")
	CostOfDrinks.set("")
	Servicecharge.set("")
	txtReceipt.delete("1.0", END)

	var1.set("0")
	var2.set("0")
	var3.set("0")
	var4.set("0")
	var5.set("0")
	var6.set("0")
	var7.set("0")
	var8.set("0")
	var9.set("0")
	var10.set("0")
	var11.set("0")
	var12.set("0")
	var13.set("0")
	var14.set("0")
	var15.set("0")
	var16.set("0")

	txtlatte.configure(state= DISABLED)
	txtExpresso.configure(state= DISABLED)
	txtIcedTea.configure(state= DISABLED)
	txtValeCoffee.configure(state= DISABLED)
	txtCuppucchino.configure(state= DISABLED)
	txtAfricanCoffee.configure(state= DISABLED)
	txtAmericanCoffee.configure(state= DISABLED)
	txtIcedCuppucchino.configure(state= DISABLED)
	txtCoffeeCake.configure(state= DISABLED)
	txtRedVelvetCake.configure(state= DISABLED)
	txtBlackForestCake.configure(state= DISABLED)
	txtBostonCreamCake.configure(state= DISABLED)
	txtLagosChocolateCake.configure(state= DISABLED)
	txtKilburnChocolateCake.configure(state= DISABLED)
	txtCarltonHillChocolateCake.configure(state= DISABLED)
	txtQueensParkChocolateCake.configure(state= DISABLED)

def Receipt():
	txtReceipt.delete("1.0", END)
	x = random.randint(10908, 500876)
	randomRef = str(x)
	Receipt_Ref.set("BILL_" + randomRef)

	txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + '\t\t' + DateOfOrder.get() + "\n")
	txtReceipt.insert(END, 'Items\t\t\t\t' + "Cost of Items\n\n")
	txtReceipt.insert(END, 'Latte:\t\t\t\t' + E_latte.get() + "\n")
	txtReceipt.insert(END, 'Expresso:\t\t\t\t' + E_Expresso.get() + "\n")
	txtReceipt.insert(END, 'Iced Tea:\t\t\t\t' + E_IcedTea.get() + "\n")
	txtReceipt.insert(END, 'Vale Coffee:\t\t\t\t' + E_ValeCoffee.get() + "\n")
	txtReceipt.insert(END, 'Cuppucchino:\t\t\t\t' + E_Cuppucchino.get() + "\n")
	txtReceipt.insert(END, 'African Coffee:\t\t\t\t' + E_AfricanCoffee.get() + "\n")
	txtReceipt.insert(END, 'American Coffee:\t\t\t\t' + E_AmericanCoffee.get() + "\n")
	txtReceipt.insert(END, 'Iced Cuppucchino:\t\t\t\t' + E_IcedCuppucchino.get() + "\n")
	txtReceipt.insert(END, 'Coffee Cake:\t\t\t\t' + E_CoffeeCake.get() + "\n")
	txtReceipt.insert(END, 'Red Velvet Cake:\t\t\t\t' + E_RedVelvetCake.get() + "\n")
	txtReceipt.insert(END, 'Black Forest Cake:\t\t\t\t' + E_BlackForestCake.get() + "\n")
	txtReceipt.insert(END, 'Boston Cream Cake:\t\t\t\t' + E_BostonCreamCake.get() + "\n")
	txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t\t' + E_LagosChocolateCake.get() + "\n")
	txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t\t' + E_KilburnChocolateCake.get() + "\n")
	txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:\t\t\t\t' + E_CarltonHillChocolateCake.get() + "\n")
	txtReceipt.insert(END, 'Queens Park Chocolate Cake:\t\t\t\t' + E_QueensParkChocolateCake.get() + "\n\n")
	txtReceipt.insert(END, 'Cost of Drinks:\t' + CostOfDrinks.get()+ '\t\t  Paid Tax:\t' + PaidTax.get() + "\n\n")
	txtReceipt.insert(END, 'Cost of Cakes:\t' + CostOfCakes.get()+ '\t\t  SubTotal:\t' + SubTotal.get() + "\n\n")
	txtReceipt.insert(END, 'Service Charge:\t' + Servicecharge.get()+ '\t\t  Total Cost:\t' + TotalCost.get() + "\n")



#============FRAME 1 DRINKS=============================================================
latte = Checkbutton(f1aa, command=chkButton_value, text="Latte ", variable=var1, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=0, column=0, sticky=W)
Expresso = Checkbutton(f1aa, command=chkButton_value, text="Expresso ", variable=var2, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
IcedTea = Checkbutton(f1aa, command=chkButton_value, text="Iced Tea ", variable=var3, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
ValeCoffee = Checkbutton(f1aa, command=chkButton_value, text="Vale Coffee ", variable=var4, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
Cuppucchino = Checkbutton(f1aa, command=chkButton_value, text="Cuppucchino ", variable=var5, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
AfricanCoffee = Checkbutton(f1aa, command=chkButton_value, text="African Coffee ", variable=var6, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
AmericanCoffee = Checkbutton(f1aa, command=chkButton_value, text="American Coffee ", variable=var7, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=6, column=0, sticky=W)
IcedCuppucchino = Checkbutton(f1aa, command=chkButton_value, text="Iced Cuppucchino ", variable=var8, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=7, column=0, sticky=W)

#==============FRAME 2 CAKES===============================================================================
CoffeeCake = Checkbutton(f1ab, command=chkButton_value, text="Coffee Cake ", variable=var9, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=0, column=0, sticky=W)
RedVelvetCake = Checkbutton(f1ab, command=chkButton_value, text="Red Velvet Cake ", variable=var10, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
BlackForestCake = Checkbutton(f1ab, command=chkButton_value, text="Black Forest Cake ", variable=var11, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
BostonCreamCake = Checkbutton(f1ab, command=chkButton_value, text="Boston Cream Cake ", variable=var12, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
LagosChocolateCake = Checkbutton(f1ab, command=chkButton_value, text="Lagos Chocolate Cake ", variable=var13, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
KilburnChocolateCake = Checkbutton(f1ab, command=chkButton_value, text="Kilburn Chocolate Cake ", variable=var14, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
CarltonHillChocolateCake = Checkbutton(f1ab, command=chkButton_value, text="Carlton Hill Chocolate Cake ", variable=var15, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=6, column=0, sticky=W)
QueensParkChocolateCake = Checkbutton(f1ab, command=chkButton_value, text="Queens Park Chocolate Cake ", variable=var16, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=7, column=0, sticky=W)

#================ENTRY FOR DRINKS==============================================================================
txtlatte = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_latte  , justify='left', state=DISABLED)
txtlatte.grid(row=0, column=1, sticky=E)
txtExpresso = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_Expresso  , justify='left', state=DISABLED)
txtExpresso.grid(row=1, column=1, sticky=E)
txtIcedTea = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_IcedTea  , justify='left', state=DISABLED)
txtIcedTea.grid(row=2, column=1, sticky=E)
txtValeCoffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_ValeCoffee  , justify='left', state=DISABLED)
txtValeCoffee.grid(row=3, column=1, sticky=E)
txtCuppucchino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_Cuppucchino  , justify='left', state=DISABLED)
txtCuppucchino.grid(row=4, column=1, sticky=E)
txtAfricanCoffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_AfricanCoffee  , justify='left', state=DISABLED)
txtAfricanCoffee.grid(row=5, column=1, sticky=E)
txtAmericanCoffee = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_AmericanCoffee  , justify='left', state=DISABLED)
txtAmericanCoffee.grid(row=6, column=1, sticky=E)
txtIcedCuppucchino = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_IcedCuppucchino  , justify='left', state=DISABLED)
txtIcedCuppucchino.grid(row=7, column=1, sticky=E)

#================ENTRY FOR CAKES==============================================================================
txtCoffeeCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_CoffeeCake  , justify='left', state=DISABLED)
txtCoffeeCake.grid(row=0, column=1, sticky=E)
txtRedVelvetCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_RedVelvetCake  , justify='left', state=DISABLED)
txtRedVelvetCake.grid(row=1, column=1, sticky=E)
txtBlackForestCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_BlackForestCake  , justify='left', state=DISABLED)
txtBlackForestCake.grid(row=2, column=1, sticky=E)
txtBostonCreamCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_BostonCreamCake  , justify='left', state=DISABLED)
txtBostonCreamCake.grid(row=3, column=1, sticky=E)
txtLagosChocolateCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_LagosChocolateCake  , justify='left', state=DISABLED)
txtLagosChocolateCake.grid(row=4, column=1, sticky=E)
txtKilburnChocolateCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_KilburnChocolateCake  , justify='left', state=DISABLED)
txtKilburnChocolateCake.grid(row=5, column=1, sticky=E)
txtCarltonHillChocolateCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_CarltonHillChocolateCake  , justify='left', state=DISABLED)
txtCarltonHillChocolateCake.grid(row=6, column=1, sticky=E)
txtQueensParkChocolateCake = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, textvariable=E_QueensParkChocolateCake  , justify='left', state=DISABLED)
txtQueensParkChocolateCake.grid(row=7, column=1, sticky=E)

#=============INFORMATION=================================================
lblReceipt = Label (ft2, font=('arial', 18, 'bold'), text="Receipt", bd=2)
lblReceipt.grid(row=0, column=0)
txtReceipt = Text(ft2, font=('arial', 10, 'bold'), bd=6, width=50, height=27,bg="white")
txtReceipt.grid(row=1, column=0, sticky=W)

#=============COST ITEM INFORMATION=================================================
lblCostOfDrinks = Label(f2aa, font=('arial', 16, 'bold'), text="Cost Of Drinks", bd=7, fg="black")
lblCostOfDrinks.grid(row=0, column=0, sticky=W)
txtCostOfDrinks = Entry(f2aa, textvariable=CostOfDrinks, font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtCostOfDrinks.grid(row=0, column=1, sticky=W)

lblCostOfCakes = Label(f2aa, font=('arial', 16, 'bold'), text="Cost Of Cakes", bd=7, fg="black")
lblCostOfCakes.grid(row=1, column=0, sticky=W)
txtCostOfCakes = Entry(f2aa, textvariable=CostOfCakes, font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtCostOfCakes.grid(row=1, column=1, sticky=W)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text="Service Charge", bd=7, fg="black")
lblServiceCharge.grid(row=2, column=0, sticky=W)
txtServiceCharge = Entry(f2aa,textvariable=Servicecharge , font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtServiceCharge.grid(row=2, column=1, sticky=W)


#=============PAYMENT INFORMATION=================================================
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text="Tax", bd=7, fg="black")
lblPaidTax.grid(row=0, column=0, sticky=W)
txtPaidTax = Entry(f2ab, textvariable=PaidTax, font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtPaidTax.grid(row=0, column=1, sticky=W)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Sub Total", bd=7, fg="black")
lblSubTotal.grid(row=1, column=0, sticky=W)
txtSubTotal = Entry(f2ab, textvariable=SubTotal, font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtSubTotal.grid(row=1, column=1, sticky=W)

lblTotal = Label(f2ab, font=('arial', 16, 'bold'), text="Total", bd=7, fg="black")
lblTotal.grid(row=2, column=0, sticky=W)
txtTotal = Entry(f2ab, textvariable=TotalCost, font=('arial', 16, 'bold'), bd=7,insertwidth=2, justify=LEFT)
txtTotal.grid(row=2, column=1, sticky=W)

#=============BUTTONS=================================================
btnTotal= Button(fb2, command=getTotal, text='Total', padx=5, pady=1, bd=3, fg='black', bg="cadet blue", font=('arial', 16, 'bold'), width=5).grid(row=0, column=0, padx=3)
btnReceipt= Button(fb2, command=Receipt, text='Receipt', padx=5, pady=1, bd=3, fg='black', bg="cadet blue", font=('arial', 16, 'bold'), width=5).grid(row=0, column=1, padx=3)
btnReset= Button(fb2, command=Reset, text='Reset', padx=5, pady=1, bd=3, fg='black', bg="cadet blue", font=('arial', 16, 'bold'), width=5).grid(row=0, column=2, padx=3)
btnExit= Button(fb2, command=iExit, text='Exit', padx=5, pady=1, bd=3, fg='black', bg="cadet blue", font=('arial', 16, 'bold'), width=5).grid(row=0, column=3, padx=3)



root.mainloop()