from tkinter import *

def display():
    data = entry.get()
    print(data)

root = Tk()
root.geometry("455x455")

entry = Entry(root)
entry.pack()


button = Button(root, text="Click Me!", fg="blue", bg="red", command= display)
button.pack()

answer = Label()
answer.pack()

root.mainloop()