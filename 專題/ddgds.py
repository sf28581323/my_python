import tkinter as tk

class Mainapplication(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.pack()
		self.createwidget()
		
	def createwidget(self):
		self.textframe = Mainapplication2(master=self)
		self.textframe.packapplication()
		self.button = tk.Button(self,text="OK",command=self.openfile)
		self.button.pack()
		
	def openfile(self):
		self.textframe.openfile()

		
class Mainapplication2(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.createwidget()
		
	def createwidget(self):
		self.scrollbar = tk.Scrollbar(self)
		self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
		
		self.text = tk.Text(self,yscrollcommand=self.scrollbar.set)
		self.text.pack(side=tk.LEFT,fill=tk.BOTH)
		
		self.scrollbar.config(command=self.text.yview)
		
	def openfile(self):
		with open('1111.txt','r') as f:
			temp = f.read()
			
		self.text.insert(tk.END,temp)
	def packapplication(self):
		self.pack()


if __name__ =='__main__':
	root = tk.Tk()
	app = Mainapplication(master=root)
	root.mainloop()