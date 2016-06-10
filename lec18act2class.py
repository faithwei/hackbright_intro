from Tkinter import *

class App(object):
	def __init__(self, master):
		
		var_label_text = StringVar(master)
		var_label_text.set("Display your full name here.")
		lbl_hello = Label(master, textvariable=var_label_text)
		lbl_hello.grid(row=0, column=1)


		Label(master,text="First Name", fg="red", font=("Helvetica", 16)).grid(row=2)
		Label(master,text="Last Name").grid(row=3)

		entry_text1 = Entry(master)
		entry_text1.insert(0, "Enter your first name")
		entry_text1.grid()

		entry_text2 = Entry(master)
		entry_text2.insert(0, "Enter your last name") 
		entry_text2.grid()

		entry_text1.grid(row=2, column=1)
		entry_text2.grid(row=3, column=1)

		btn_ok = Button(master, text='Ok', command=lambda: var_label_text.set("My Name is " + entry_text1.get() + " " + entry_text2.get()))
		btn_ok.grid(row=10, column=1 )

class App2(object):
	def __init__(self, master):
		
		var_label_text = StringVar(master)
		var_label_text.set("Display your full name here.")
		lbl_hello = Label(master, textvariable=var_label_text)
		lbl_hello.grid(row=0, column=1)


		Label(master,text="First Name").grid(row=2)
		Label(master,text="Last Name").grid(row=3)

		entry_text1 = Entry(master)
		entry_text1.insert(0, "Enter your first name")
		entry_text1.grid()

		entry_text2 = Entry(master)
		entry_text2.insert(0, "Enter your last name") 
		entry_text2.grid()

		entry_text1.grid(row=2, column=1)
		entry_text2.grid(row=3, column=1)

		btn_ok = Button(master, text='Ok', command=lambda: var_label_text.set("My Name is " + entry_text1.get() + " " + entry_text2.get()))
		btn_ok.grid(row=10, column=1 )




