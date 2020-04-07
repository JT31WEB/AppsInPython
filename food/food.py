from tkinter import *
import random
import time
import datetime
from tkinter import Tk, StringVar, ttk, messagebox 

root = Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

#=HEADING=============================================
Tops = Frame (root, width=1350, height=100, bd=12, relief="raise")
Tops.pack(side=TOP)

lblTitle = Label (Tops, font=('arial', 50, 'bold'), text="\tFast Food Resturant\t")
lblTitle.grid(row=0, column=0)
#=====MAIN FRAME=====================================================
BottomMainFrame = Frame (root, width=1350, height=650, bd=6, relief="raise")
BottomMainFrame.pack(side=BOTTOM)

#====ORDER FRAMES==============================================================
f1 = Frame (BottomMainFrame, width=450, height=650, bd=2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame (BottomMainFrame, width=450, height=650, bd=2, relief="raise")
f2.pack(side=LEFT)
f2top = Frame (f2, width=450, height=350, bd=2, relief="raise")
f2top.pack(side=TOP)
f2bottom = Frame (f2, width=450, height=300, bd=1, relief="raise")
f2bottom.pack(side=BOTTOM)
f3 = Frame (BottomMainFrame, width=450, height=650, bd=2, relief="raise")
f3.pack(side=RIGHT)

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
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)

varFries = StringVar()
varSalad = StringVar()
varHamburger = StringVar()
varOnionRings = StringVar()
varChickenSandwich = StringVar()
varFishSandwich = StringVar()
varCheeseSandwich = StringVar()
varChickenSalad = StringVar()

varHashBrown = StringVar()
varToastedBagal = StringVar()
varPanCakeSyrup = StringVar()
varPineappleStick = StringVar()
varChocolateMuffin = StringVar()
varRedCake = StringVar()

varTea = StringVar()
varCola = StringVar()
varCoffee = StringVar()
varOrange = StringVar()
varBottleWater = StringVar()

varVanillaCone = StringVar()
varVanillaShake = StringVar()
varStrawberryShake = StringVar()

varChange = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varTAX = StringVar()
varVAT = StringVar()
varPayment = StringVar()

varFries.set("0")
varSalad.set("0")
varHamburger.set("0")
varOnionRings.set("0")
varChickenSandwich.set("0")
varFishSandwich.set("0")
varCheeseSandwich.set("0")
varChickenSalad.set("0")

varHashBrown.set("0")
varToastedBagal.set("0")
varPanCakeSyrup.set("0")
varPineappleStick.set("0")
varChocolateMuffin.set("0")
varRedCake.set("0")

varTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varBottleWater.set("0")

varVanillaCone.set("0")
varVanillaShake.set("0")
varStrawberryShake.set("0")

varChange.set("0")
varSubTotal.set("0")
varTotal.set("0")
varVAT.set("0")
varTAX.set("0")
varPayment.set("0")


#=========FUNCTIONS====================================================================
def iExit():
	qExit = messagebox.askyesno("payslip system", "Do you want to exit the system")
	if qExit  == 1:
		root.destroy()
		return

def Reset():
	varFries.set("0")
	varSalad.set("0")
	varHamburger.set("0")
	varOnionRings.set("0")
	varChickenSandwich.set("0")
	varFishSandwich.set("0")
	varCheeseSandwich.set("0")
	varChickenSalad.set("0")

	varHashBrown.set("0")
	varToastedBagal.set("0")
	varPanCakeSyrup.set("0")
	varPineappleStick.set("0")
	varChocolateMuffin.set("0")
	varRedCake.set("0")

	varTea.set("0")
	varCola.set("0")
	varCoffee.set("0")
	varOrange.set("0")
	varBottleWater.set("0")

	varVanillaCone.set("0")
	varVanillaShake.set("0")
	varStrawberryShake.set("0")

	varChange.set("0")
	varSubTotal.set("0")
	varTotal.set("0")
	varVAT.set("0")
	varTAX.set("0")
	varPayment.set("Cash")

	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var6.set(0)
	var7.set(0)
	var8.set(0)
	var9.set(0)
	var10.set(0)
	var11.set(0)
	var12.set(0)
	var13.set(0)
	var14.set(0)
	var15.set(0)
	var16.set(0)
	var17.set(0)
	var18.set(0)
	var19.set(0)
	var20.set(0)
	var21.set(0)
	var22.set(0)
	var23.set(0)

	txtFries.configure(state = DISABLED)
	txtSalad.configure(state = DISABLED)
	txtHamburger.configure(state = DISABLED)
	txtOnionRings.configure(state = DISABLED)
	txtChickenSandwich.configure(state = DISABLED)
	txtFishSandwich.configure(state = DISABLED)
	txtCheeseSandwich.configure(state = DISABLED)
	txtChickenSalad.configure(state = DISABLED)

	txtHashBrown.configure(state = DISABLED)
	txtToastedBagal.configure(state = DISABLED)
	txtPanCakeSyrup.configure(state = DISABLED)
	txtPineappleStick.configure(state = DISABLED)
	txtChocolateMuffin.configure(state = DISABLED)
	txtRedCake.configure(state = DISABLED)

	txtTea.configure(state = DISABLED)
	txtCola.configure(state = DISABLED)
	txtCoffee.configure(state = DISABLED)
	txtOrange.configure(state = DISABLED)
	txtBottleWater.configure(state = DISABLED)

	txtVanillaCone.configure(state = DISABLED)
	txtVanillaShake.configure(state = DISABLED)
	txtStrawberryShake.configure(state = DISABLED)


    #======ITEM SELECT FUNC=================================================================

def chkFries():
	if (var1.get() == 1):
		txtFries.configure(state = NORMAL)
		varFries.set("")
	elif (var1.get() == 0):
		txtFries.configure(state = DISABLED)
		varFries.set("0")

def chkSalad():
	if (var2.get() == 1):
		txtSalad.configure(state = NORMAL)
		varSalad.set("")
	elif (var2.get() == 0):
		txtSalad.configure(state = DISABLED)
		varSalad.set("0")

def chkHamburger():
	if (var3.get() == 1):
		txtHamburger.configure(state = NORMAL)
		varHamburger.set("")
	elif (var3.get() == 0):
		txtHamburger.configure(state = DISABLED)
		varHamburger.set("0")

def chkOnionRings():
	if (var4.get() == 1):
		txtOnionRings.configure(state = NORMAL)
		varOnionRings.set("")
	elif (var4.get() == 0):
		txtOnionRings.configure(state = DISABLED)
		varOnionRings.set("0")

def chkChickenSalad():
	if (var5.get() == 1):
		txtChickenSalad.configure(state = NORMAL)
		varChickenSalad.set("")
	elif (var5.get() == 0):
		txtChickenSalad.configure(state = DISABLED)
		varChickenSalad.set("0")

def chkChickenSandwich():
	if (var7.get() == 1):
		txtChickenSandwich.configure(state = NORMAL)
		varChickenSandwich.set("")
	elif (var7.get() == 0):
		txtChickenSandwich.configure(state = DISABLED)
		varChickenSandwich.set("0")

def chkFishSandwich():
	if (var6.get() == 1):
		txtFishSandwich.configure(state = NORMAL)
		varFishSandwich.set("")
	elif (var6.get() == 0):
		txtFishSandwich.configure(state = DISABLED)
		varFishSandwich.set("0")

def chkCheeseSandwich():
	if (var8.get() == 1):
		txtCheeseSandwich.configure(state = NORMAL)
		varCheeseSandwich.set("")
	elif (var8.get() == 0):
		txtCheeseSandwich.configure(state = DISABLED)
		varCheeseSandwich.set("0")

def chkHashBrown():
	if (var9.get() == 1):
		txtHashBrown.configure(state = NORMAL)
		varHashBrown.set("")
	elif (var9.get() == 0):
		txtHashBrown.configure(state = DISABLED)
		varHashBrown.set("0")

def chkToastedBagal():
	if (var10.get() == 1):
		txtToastedBagal.configure(state = NORMAL)
		varToastedBagal.set("")
	elif (var10.get() == 0):
		txtToastedBagal.configure(state = DISABLED)
		varToastedBagal.set("0")

def chkPancakeSyrup():
	if (var12.get() == 1):
		txtPanCakeSyrup.configure(state = NORMAL)
		varPanCakeSyrup.set("")
	elif (var12.get() == 0):
		txtPanCakeSyrup.configure(state = DISABLED)
		varPanCakeSyrup.set("0")

def chkPineappleStick():
	if (var13.get() == 1):
		txtPineappleStick.configure(state = NORMAL)
		varPineappleStick.set("")
	elif (var13.get() == 0):
		txtPineappleStick.configure(state = DISABLED)
		varPineappleStick.set("0")

def chkChocoMuffin():
	if (var14.get() == 1):
		txtChocolateMuffin.configure(state = NORMAL)
		varChocolateMuffin.set("")
	elif (var14.get() == 0):
		txtChocolateMuffin.configure(state = DISABLED)
		varChocolateMuffin.set("0")

def chkRedCake():
	if (var11.get() == 1):
		txtRedCake.configure(state = NORMAL)
		varRedCake.set("")
	elif (var11.get() == 0):
		txtRedCake.configure(state = DISABLED)
		varRedCake.set("0")

def chkTea():
	if (var15.get() == 1):
		txtTea.configure(state = NORMAL)
		varTea.set("")
	elif (var15.get() == 0):
		txtTea.configure(state = DISABLED)
		varTea.set("0")

def chkCola():
	if (var16.get() == 1):
		txtCola.configure(state = NORMAL)
		varCola.set("")
	elif (var16.get() == 0):
		txtCola.configure(state = DISABLED)
		varCola.set("0")

def chkCoffee():
	if (var17.get() == 1):
		txtCoffee.configure(state = NORMAL)
		varCoffee.set("")
	elif (var17.get() == 0):
		txtCoffee.configure(state = DISABLED)
		varCoffee.set("0")

def chkOrange():
	if (var18.get() == 1):
		txtOrange.configure(state = NORMAL)
		varOrange.set("")
	elif (var18.get() == 0):
		txtOrange.configure(state = DISABLED)
		varOrange.set("0")

def chkBottleWater():
	if (var19.get() == 1):
		txtBottleWater.configure(state = NORMAL)
		varBottleWater.set("")
	elif (var19.get() == 0):
		txtBottleWater.configure(state = DISABLED)
		varBottleWater.set("0")

def chkVanillaCone():
	if (var20.get() == 1):
		txtVanillaCone.configure(state = NORMAL)
		varVanillaCone.set("")
	elif (var20.get() == 0):
		txtVanillaCone.configure(state = DISABLED)
		varVanillaCone.set("0")

def chkVanillaShake():
	if (var21.get() == 1):
		txtVanillaShake.configure(state = NORMAL)
		varVanillaShake.set("")
	elif (var21.get() == 0):
		txtVanillaShake.configure(state = DISABLED)
		varVanillaShake.set("0")

def chkStrawberryShake():
	if (var22.get() == 1):
		txtStrawberryShake.configure(state = NORMAL)
		varStrawberryShake.set("")
	elif (var22.get() == 0):
		txtStrawberryShake.configure(state = DISABLED)
		varStrawberryShake.set("0")

def CostOfMeal():
	meal1 = float(varFries.get())
	meal2 = float(varSalad.get())
	meal3 = float(varHamburger.get())
	meal4 = float(varOnionRings.get())
	meal5 = float(varChickenSalad.get())
	meal6 = float(varChickenSandwich.get())
	meal7 = float(varFishSandwich.get())
	meal8 = float(varCheeseSandwich.get())
	meal9 = float(varHashBrown.get())
	meal10 = float(varToastedBagal.get())
	meal11 = float(varPanCakeSyrup.get())
	meal12 = float(varPineappleStick.get())
	meal13 = float(varChocolateMuffin.get())
	meal14 = float(varRedCake.get())
	meal15 = float(varTea.get())
	meal16 = float(varCola.get())
	meal17 = float(varCoffee.get())
	meal18 = float(varOrange.get())
	meal19 = float(varBottleWater.get())
	meal20 = float(varVanillaCone.get())
	meal21 = float(varVanillaShake.get())
	meal22 = float(varStrawberryShake.get())

	TotalMeal =(meal1 * 15) + (meal2 * 25) + (meal3 * 30) + (meal4 * 10) + (meal5 * 35)
	TotalSandwich =(meal6 * 25) + (meal7 * 25) + (meal8 * 15)
	TotalDessert = (meal9 * 8) + (meal10 * 10) + (meal11 * 25) + (meal12 * 10) + (meal13 * 5) + (meal14 * 6)
	TotalDrink = (meal15 * 6) + (meal16 * 9) + (meal17 * 8) + (meal18 * 5) + (meal19 * 10) 
	TotalShakes = (meal20 * 6) + (meal21 * 15) + (meal22 * 15)

	if (varPayment.get() == "Cash"):
		iChange = float(var23.get())
		iCost =(TotalMeal + TotalShakes + TotalDrink + TotalSandwich + TotalDessert)
		iTax = (iCost * 3.4)/100
		varTAX.set(iTax)

		iCostq = "R", str('%.2f'%(iCost))  #string formatting for number
		varSubTotal.set(iCostq)
		iTotalq = "R", str('%.2f'%(iCost + iTax))
		varTotal.set(iTotalq)
		cChange = (iChange - (iCost + iTax))
		cChangeq = "R", str('%.2f'%(cChange))
		varChange.set(cChangeq)
		
	elif (varPayment.get() == "Master Card" or "Visa card" or "Debit card"):
		varPayment.set("")
		varChange.set("")
		iCost =(TotalMeal + TotalShakes + TotalDrink + TotalSandwich + TotalDessert)
		iTax = (iCost * 3.4)/100
		varTAX.set(iTax)
		iCostq = "R", str('%.2f'%(iCost))  #string formatting for number
		varSubTotal.set(iCostq)
		iTotalq = "R", str('%.2f'%(iCost + iTax))
		varTotal.set(iTotalq)
		cChange = (iChange - (iCost + iTax))
		cChangeq = "R", str('%.2f'%(cChange))
		varChange.set(cChangeq)



#=========FRAME 1 MEAL===============================================
lblMeal = Label (f1, font=('arial', 20, 'bold'), text="\nFast Meals and Veggies\n")
lblMeal.grid(row=0, column=0)
#====ITEMS==============================================================
Fries = Checkbutton(f1, command=chkFries, text="Fries\t\tR15", variable=var1, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtFries = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varFries, width=6, state=DISABLED)
txtFries.grid(row=1, column=1)

Salad = Checkbutton(f1, command=chkSalad, text="Salad\t\tR25", variable=var2, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
txtSalad = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varSalad, width=6, state=DISABLED)
txtSalad.grid(row=2, column=1)

Hamburger = Checkbutton(f1, command=chkHamburger , text="Hamburger\tR30", variable=var3, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
txtHamburger = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varHamburger, width=6, state=DISABLED)
txtHamburger.grid(row=3, column=1)

OnionRings = Checkbutton(f1, command=chkOnionRings, text="Onion Rings\tR10", variable=var4, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
txtOnionRings = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varOnionRings, width=6, state=DISABLED)
txtOnionRings.grid(row=4, column=1)

ChickenSalad = Checkbutton(f1, command=chkChickenSalad, text="Chicken Salad\tR35", variable=var5, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
txtChickenSalad = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varChickenSalad, width=6, state=DISABLED)
txtChickenSalad.grid(row=5, column=1)

#====== sandwich=================================================
lblSandwich = Label (f1, font=('arial', 20, 'bold'), text="\nSANDWICH\n")
lblSandwich.grid(row=6, column=0)

FishSandwich = Checkbutton(f1, command=chkFishSandwich, text="Fish Sandwich\tR25", variable=var6, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=7, column=0, sticky=W)
txtFishSandwich = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varFishSandwich, width=6, state=DISABLED)
txtFishSandwich.grid(row=7, column=1)

ChickenSandwich = Checkbutton(f1, command=chkChickenSandwich, text="Chicken Sandwich R25", variable=var7, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=8, column=0, sticky=W)
txtChickenSandwich = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varChickenSandwich, width=6, state=DISABLED)
txtChickenSandwich.grid(row=8, column=1)

CheeseSandwich = Checkbutton(f1, command=chkCheeseSandwich, text="Cheese Sandwich  R15", variable=var8, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=9, column=0, sticky=W)
txtCheeseSandwich = Entry(f1, font=('arial', 18, 'bold'), justify='right',textvariable=varCheeseSandwich, width=6, state=DISABLED)
txtCheeseSandwich.grid(row=9, column=1)

lblSpace = Label (f1, font=('arial', 20, 'bold'), text="\n\n\n\n")
lblSpace.grid(row=10, column=0)



#=========FRAME 2 MEALS===============================================
lblMeal = Label (f2top, font=('arial', 20, 'bold'), text="DESSERTS")
lblMeal.grid(row=0, column=0)
#====ITEMS==============================================================
HashBrown = Checkbutton(f2top, command=chkHashBrown , text="Hash Brown\tR8", variable=var9, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtHashBrown = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varHashBrown, width=6, state=DISABLED)
txtHashBrown.grid(row=1, column=1)

ToastedBagal = Checkbutton(f2top, command=chkToastedBagal, text="Toasted Bagal\tR10", variable=var10, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
txtToastedBagal = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varToastedBagal, width=6, state=DISABLED)
txtToastedBagal.grid(row=2, column=1)

RedCake = Checkbutton(f2top, command=chkRedCake, text="RedCake\t\tR6", variable=var11, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
txtRedCake = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varRedCake, width=6, state=DISABLED)
txtRedCake.grid(row=3, column=1)

PanCakeSyrup = Checkbutton(f2top, command=chkPancakeSyrup, text="PanCakes and Syrup R25", variable=var12, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
txtPanCakeSyrup = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varPanCakeSyrup, width=6, state=DISABLED)
txtPanCakeSyrup.grid(row=4, column=1)

PineappleStick = Checkbutton(f2top, command=chkPineappleStick, text="Pineapple Stick\tR10", variable=var13, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
txtPineappleStick = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varPineappleStick, width=6, state=DISABLED)
txtPineappleStick.grid(row=5, column=1)

ChocolateMuffin = Checkbutton(f2top, command=chkChocoMuffin, text="Chocolate Muffin R5", variable=var14, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=6, column=0, sticky=W)
txtChocolateMuffin = Entry(f2top, font=('arial', 18, 'bold'), justify='right',textvariable=varChocolateMuffin, width=6, state=DISABLED)
txtChocolateMuffin.grid(row=6, column=1)



#=========FRAME 3 MEAL===============================================
lblMeal = Label (f3, font=('arial', 20, 'bold'), text="\nDRINKS\n")
lblMeal.grid(row=0, column=0)
#====ITEMS==============================================================
Tea = Checkbutton(f3, command=chkTea, text="Tea\t\tR5", variable=var15, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=1, column=0, sticky=W)
txtTea = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varTea, width=6, state=DISABLED)
txtTea.grid(row=1, column=1)

Cola = Checkbutton(f3, command=chkCola, text="Cola\t\tR9", variable=var16, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=2, column=0, sticky=W)
txtCola = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varCola, width=6, state=DISABLED)
txtCola.grid(row=2, column=1)

Coffee = Checkbutton(f3, command=chkCoffee, text="Coffee\t\tR8", variable=var17, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=3, column=0, sticky=W)
txtCoffee = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varCoffee, width=6, state=DISABLED)
txtCoffee.grid(row=3, column=1)

Orange = Checkbutton(f3, command=chkOrange, text="Orange Juice\tR5", variable=var18, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=4, column=0, sticky=W)
txtOrange = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varOrange, width=6, state=DISABLED)
txtOrange.grid(row=4, column=1)

BottleWater = Checkbutton(f3, command=chkBottleWater, text="Bottle Water\tR10", variable=var19, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=5, column=0, sticky=W)
txtBottleWater = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varBottleWater, width=6, state=DISABLED)
txtBottleWater.grid(row=5, column=1)

#======SHAKES=================================================
lblSandwich = Label (f3, font=('arial', 20, 'bold'), text="\nSHAKES\n")
lblSandwich.grid(row=6, column=0)

VanillaCone = Checkbutton(f3, command=chkVanillaCone, text="Vanilla Ice Cream R6", variable=var20, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=7, column=0, sticky=W)
txtVanillaCone = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varVanillaCone, width=6, state=DISABLED)
txtVanillaCone.grid(row=7, column=1)

VanillaShake = Checkbutton(f3, command=chkVanillaShake, text="Vanilla Milkshake\tR15", variable=var21, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=8, column=0, sticky=W)
txtVanillaShake = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varVanillaShake, width=6, state=DISABLED)
txtVanillaShake.grid(row=8, column=1)

StrawberryShake = Checkbutton(f3, command=chkStrawberryShake, text="Strawberry Milkshake R15", variable=var22, onvalue=1, offvalue=0,font=('arial', 18, 'bold')).grid(row=9, column=0, sticky=W)
txtStrawberryShake = Entry(f3, font=('arial', 18, 'bold'), justify='right',textvariable=varStrawberryShake, width=6, state=DISABLED)
txtStrawberryShake.grid(row=9, column=1)

lblSpace = Label (f3, text="\n\n\n\n")
lblSpace.grid(row=10, column=0)

#================================FRAME 2 BOTTOM=================================================
lblPaymentMethod = Label (f2bottom, font=('arial', 14, 'bold'), text="Payment Method", bd=10, width=16, anchor="w")
lblPaymentMethod.grid(row=0, column=0)

lblChange =Label (f2bottom, font=('arial', 14, 'bold'), text="Change", bd=10, anchor="w")
lblChange.grid(row=0, column=1)
lblChange = Entry(f2bottom, font=('arial', 16, 'bold'), justify='right',textvariable=varChange, width=6, state=DISABLED)
lblChange.grid(row=0, column=2)

cmbPaymentMethod = ttk.Combobox (f2bottom, justify='right',textvariable=varPayment, font=('arial', 12, 'bold'), state="readonly", width=20)
cmbPaymentMethod['value'] = ('Cash', 'Master card', 'Visa card','Debit card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column=0)

lblTax =Label (f2bottom, font=('arial', 14, 'bold'), text="Tax", bd=10,  anchor="w")
lblTax.grid(row=1, column=1)
lblTax = Entry(f2bottom, font=('arial', 16, 'bold'), justify='right',textvariable=varTAX, width=6, state=DISABLED)
lblTax.grid(row=1, column=2)

txtPayment = Entry(f2bottom, font=('arial', 18, 'bold'), justify='right',textvariable=var23, width=6, state=NORMAL)
txtPayment.grid(row=2, column=0)
lblSubTotal =Label (f2bottom, font=('arial', 14, 'bold'), text="Sub Total", width=6, bd=10,  anchor="w")
lblSubTotal.grid(row=2, column=1)
txtSubTotal = Entry(f2bottom, font=('arial', 18, 'bold'), justify='right',textvariable=varSubTotal, width=6,  state=DISABLED)
txtSubTotal.grid(row=2, column=2)

lblTotal =Label (f2bottom, font=('arial', 14, 'bold'), text="Total", bd=10,  anchor="w")
lblTotal.grid(row=3, column=1)
lblTotal = Entry(f2bottom, font=('arial', 16, 'bold'), justify='right',textvariable=varTotal, width=6, state=DISABLED)
lblTotal.grid(row=3, column=2)

#=======FRAME 2 BUTTONS===============================================================================
btnTotal = Button(f2bottom, command=CostOfMeal, padx=16, pady=1, bd=4, width=5, fg="black", font=('arial', 16, 'bold'), text="Total").grid(row=4, column=0)
btnReset = Button(f2bottom, command=Reset, padx=16, pady=1, bd=4, width=5, fg="black", font=('arial', 16, 'bold'), text="Reset").grid(row=4, column=1)
btnExit = Button(f2bottom, command=iExit, padx=16, pady=1, bd=4, width=5, fg="black", font=('arial', 16, 'bold'), text="Exit").grid(row=4, column=2)

lblSpace = Label (f2bottom, text="\n\n\n\n\n\n")
lblSpace.grid(row=5, column=0)


root.mainloop()