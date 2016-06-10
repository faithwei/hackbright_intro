from lec18act2class import App
from lec18act2class import App2
from Tkinter import *







root_widget = Tk() # create a window widget
root_widget.geometry("600x300") # set the size of the window
root_widget.title("Simple GUI Demo") # set the title


photo = PhotoImage(file="cat1.gif")
root_widget = Label(image=photo)
root_widget.photo = photo
root_widget.grid()






main = App(root_widget)

root_widget2 = Tk() # create a window widget
root_widget2.geometry("300x100") # set the size of the window
root_widget2.title("Simple GUI Demo2") # set the title
# root_widget2 = Label(root_widget2, text="Rouge", fg="red")

main2 = App2(root_widget2)

root_widget.mainloop()