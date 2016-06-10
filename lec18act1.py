from Tkinter import *

root_widget = Tk() # create a window widget
root_widget.geometry("300x100") # set the size of the window
root_widget.title("Simple GUI Demo") # set the title


var_label_text = StringVar()
var_label_text.set("Display your full name here.")
lbl_hello = Label(root_widget, textvariable=var_label_text)
lbl_hello.grid(row=0, column=1)




Label(root_widget,text="First Name").grid(row=2)

Label(root_widget,text="Last Name").grid(row=3)



entry_text1 = Entry()
entry_text1.insert(0, "Enter your first name")
entry_text1.grid()

entry_text2 = Entry()
entry_text2.insert(0, "Enter your last name") 
entry_text2.grid()


entry_text1.grid(row=2, column=1)
entry_text2.grid(row=3, column=1)

btn_ok = Button(text='Ok', command=lambda: var_label_text.set("My Name is " + entry_text1.get() + " " + entry_text2.get()))
btn_ok.grid(row=10, column=1 )

root_widget.mainloop()