from tkinter import *

def display():
    print("Button Clicked")

root = Tk()

root.geometry("455x455")

button = Button(root, text="Click Me!", fg="blue", bg="red", command= display)

button.pack()

root.mainloop()
