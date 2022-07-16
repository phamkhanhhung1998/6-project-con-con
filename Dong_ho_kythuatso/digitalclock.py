from tkinter import *
from tkinter.ttk import *
from time import strftime
root =Tk()
root.title("Digital Clock by Hưng")

def clock():
    string= strftime("%I:%M:%S:%p") #%H cũng được
    labels.config(text=string)
    labels.after(100,clock) #100 miligiay sẽ gọi lại hàm clock

labels = Label(root, font=("",100) , background="black", foreground="green")
labels.pack(anchor="center") #đặt label ở giữa
clock()
root.mainloop()