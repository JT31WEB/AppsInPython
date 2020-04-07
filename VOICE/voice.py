import tkinter as tk
import win32com.client

class Application (tk.frame):
	def read(self):
		print("reading..")
		speaker = win32com.client.Dispatch("SAPI.SpVoice")
		file = open("text_speech.txt", "r")
		string = file.read()
		speaker.Speak(string)

	def create_Widget(self):
		self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
		self.quit.pack(side="right")

		self.start = tk.Button(self, text="Read", fg="green")
		self.start["command"] = self.read
		self.start.pack(side="left")


	def __init__(self, master=none):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_Widget()

root = tk.Tk()
root.geometry("400x30")
app = Application(master = root)
app.master.title("Speech app in Python")
app.mainloop()

