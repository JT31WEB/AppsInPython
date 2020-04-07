from tkinter import*

def btnClick(numbers):
	global operator
	operator=operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumUp=str(eval(operator))
	text_Input.set(sumUp)
	operator=""

cal = Tk()
cal.title("Calculator")
operator=""
text_Input =StringVar()

txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

#================================================================================================================================================================
btn7=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(7), text="7").grid(row=1, column=0)
btn8=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(8), text="8").grid(row=1, column=1)
btn9=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(9), text="9").grid(row=1, column=2)
Addition=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("+"), text="+").grid(row=1, column=3)

#================================================================================================================================================================
btn4=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(4), text="4").grid(row=2, column=0)
btn5=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(5), text="5").grid(row=2, column=1)
btn6=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(6), text="6").grid(row=2, column=2)
Subtraction=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("-"), text="-").grid(row=2, column=3)

#================================================================================================================================================================
btn1=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(1), text="1").grid(row=3, column=0)
btn2=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(2), text="2").grid(row=3, column=1)
btn3=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(3), text="3").grid(row=3, column=2)
Multiply=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("*"), text="*").grid(row=3, column=3)

#================================================================================================================================================================
btn0=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick(0), text="0").grid(row=4, column=0)
Clear=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command= btnClearDisplay, text="C").grid(row=4, column=1)
Equal=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=btnEqualsInput, text="=").grid(row=4, column=2)
Divide=Button(cal,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'), bg="powder blue",command=lambda:btnClick("/"), text="/").grid(row=4, column=3)


cal.mainloop()