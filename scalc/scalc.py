#============SCIENTIFIC CALCULATOR===========================================================
from tkinter import*
import math
import parser
from tkinter import messagebox


root = Tk()
root.title("Scientific Calculator")
root.geometry("480x568+0+0")
root.configure(background="powder blue")

calc = Frame(root)
calc.grid()
#==========object and methods==========================================================================
class Calc():
	def __init__(self):
		self.total = 0
		self.current = ""
		self.input_value = True
		self.check_sum = False
		self.op = ""
		self.result = False

	def numberEnter(self, num):
		self.result = False
		firstnum = txtDisplay.get()
		secondnum = str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value = False
		else:
			if secondnum == ".":
				if secondnum in firstnum:
					return
			self.current = firstnum + secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result = True
		self.current = float(self.current)
		if self.check_sum == True:
			self.valid_function()

	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "Sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value = True
		self.check_sum = False
		self.display(self.total)

	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total = self.current
			self.input_value = True
		self.check_sum = True
		self.op = op
		self.result = False

	def clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value = True

	def all_clear_Entry(self):
		self.clear_Entry()
		self.total = 0

	def mathsPM(self):
		self.result = False
		self.current = - (float(txtDisplay.get()))
		self.display(self.current)

	def squared(self):
		self.result = False
		self.current = math.sqrt (float(txtDisplay.get()))
		self.display(self.current)

	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))  
		self.display(self.current)

	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))  
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))  
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))  
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))  
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)

	def exp(self):
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)

	def expm1(self):
		self.result = False
		self.current = math.expm1(float(txtDisplay.get()))
		self.display(self.current)

	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)

	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)

	def log2(self):
		self.result = False
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)

	def log10(self):
		self.result = False
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)

	def log1p(self):
		self.result = False
		self.current = math.log1p(float(txtDisplay.get()))
		self.display(self.current)

	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)

	def asinh(self):
		self.result = False
		self.current = math.asinh(float(txtDisplay.get()))
		self.display(self.current)

	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)

	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)


added_value = Calc()

#=============DISPLAY===========================================================================
txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bd=30, width=28, bg="powder blue", justify='right')
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")
#==============NUMBER BUTTONS=================================================================================

numberpad = "789456123"
i = 0
btn = []
for j in range (2, 5):
	for k in range (3):
		btn.append(Button(calc, width=6, height= 2, font=('arial', 20, 'bold'), bd= 4, text= numberpad[i]))
		btn[i].grid(row= j, column = k, pady = 1)
		btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
		i += 1
#================TOP BUTTONS==========================================================================================
btnClear = Button(calc, command = added_value.clear_Entry, text=chr(67), width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 0, pady= 1)
btnAllClear = Button(calc, command = added_value.all_clear_Entry, text="CE", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 1, pady= 1)
btnSqr = Button(calc, command = added_value.squared, text="SqRt", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 2, pady= 1)
btnAdd = Button(calc, command = lambda: added_value.operation("add"), text=chr(247), width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 3, pady= 1)


btnSub = Button(calc, command = lambda: added_value.operation("sub"), text="-", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 2, column= 3, pady= 1)
btnMult = Button(calc, command = lambda: added_value.operation("multi"), text="*", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 3, column= 3, pady= 1)
btnDiv = Button(calc, command = lambda: added_value.operation("divide"), text="/", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 4, column= 3, pady= 1)



btnZero = Button(calc, command = lambda: added_value.numberEnter(0), text="0", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 0, pady= 1)
btnDot = Button(calc, command = lambda: added_value.numberEnter("."), text=".", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 1, pady= 1)
btnPM = Button(calc, command = added_value.mathsPM, text=chr(177), width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 2, pady= 1)
btnEquals = Button(calc, command = added_value.sum_of_total, text="=", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 3, pady= 1)

#================SCIENTIFIC CALCULATOR========================================================================================
btnPi = Button(calc, command = added_value.pi, text="Pi", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 4, pady= 1)
btncos = Button(calc, command = added_value.cos, text="cos", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 5, pady= 1)
btntan = Button(calc, command = added_value.tan, text="tan", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 6, pady= 1)
btnsin = Button(calc, command = added_value.sin, text="sin", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 1, column= 7, pady= 1)


btn2Pi = Button(calc, command = added_value.tau, text="2Pi", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 2, column= 4, pady= 1)
btncosh = Button(calc, command = added_value.cosh, text="cosh", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 2, column= 5, pady= 1)
btntanh = Button(calc, command = added_value.tanh, text="tanh", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 2, column= 6, pady= 1)
btnsinh = Button(calc, command = added_value.sinh, text="sinh", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 2, column= 7, pady= 1)

btnlog = Button(calc, command = added_value.log, text="log", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 3, column= 4, pady= 1)
btnExp = Button(calc, command = added_value.exp, text="Exp", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 3, column= 5, pady= 1)
btnMod = Button(calc, command = lambda: added_value.operation("mod") , text="Mod", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 3, column= 6, pady= 1)
btnE = Button(calc, command = added_value.e, text="e", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 3, column= 7, pady= 1)

btnlog2 = Button(calc, command = added_value.log2, text="log2", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 4, column= 4, pady= 1)
btndeg = Button(calc, command = added_value.degrees, text="deg", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 4, column= 5, pady= 1)
btnacosh = Button(calc, command = added_value.acosh, text="acosh", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 4, column= 6, pady= 1)
btnasinh = Button(calc, command = added_value.asinh, text="asinh", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 4, column= 7, pady= 1)

btnlog10 = Button(calc, command = added_value.log10, text="log10", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 4, pady= 1)
btndeg = Button(calc, command = added_value.degrees, text="log1p", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 5, pady= 1)
btnexpm1 = Button(calc, command = added_value.expm1, text="expml", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 6, pady= 1)
btnlgamma = Button(calc, command = added_value.lgamma, text="lgamma", width=6, height= 2, background="powder blue", font=('arial', 20, 'bold'), bd= 4,).grid(row= 5, column= 7, pady= 1)

lblDisplay = Label(calc, text="Scientific Calculator", font=('arial', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row= 0, column= 4, columnspan=4)


#=============MENU==============================================================
def iExit():
	qExit = messagebox.askyesno("Scientific Calculator", "Do you want to EXIT the system")
	if qExit  == 1:
		root.destroy()
		return

def Scientific():
	root.resizable(width=False, height=False)
	root.geometry("944x568+0+0")

def Standard():
	root.resizable(width=False, height=False)
	root.geometry("480x568+0+0")



menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu=filemenu) 
filemenu.add_command(label = "Standard", command=Standard)
filemenu.add_command(label = "Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command= iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu=editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label = "View Help")


root.configure(menu = menubar)
root.mainloop()




