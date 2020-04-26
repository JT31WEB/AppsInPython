from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox, colorchooser
from datetime import datetime, date, timedelta
import random, time, tempfile, os


class Page:
	def __init__(self, root):
		self.root = root
		self.root.geometry('350x250+0+0')
		self.root.iconbitmap('BSlogo48.ico')

		def pickBG():
			color=colorchooser.askcolor()[1]
			self.root.config(background=color)

		def pickBG1():
			color1=colorchooser.askcolor()[1]
			self.Button[0].config(background=color1)


		self.btn= Button(root, text="Pick background", command=pickBG)
		self.btn.pack(side=TOP)
		self.btn1= Button(root, text="Pick background", command=pickBG1)
		self.btn1.pack(side=BOTTOM)



if __name__== '__main__':
	root = Tk()
	application = Page (root)
	root.mainloop()

