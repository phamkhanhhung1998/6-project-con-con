from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

root =Tk()
root.title(" Ứng dụng dịch")
root.geometry("500x630")
#root.iconbitmap("C:/Users/Pro 2004/Downloads/tutorial/img+font/logo.ico")
root.iconbitmap("logo.ico")

#load =Image.open("C:/Users/Pro 2004/Downloads/tutorial/img+font/background.png")
load =Image.open("background.png")
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x=0,y=0)

name =Label(root,text="Translator by Hưng" , fg="#79C895" ,bd=0 , bg="#03152D")
name.config(font=("Transformers Movie",30))
name.pack(pady= 6 )

box =Text(root, width=28, height=8, font=("ROBOTO",16))
box.pack(pady= 20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear1():
    box.delete(1.0,END)
    box1.delete(1.0, END)
def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    t = Translator()
    a = t.translate(INPUT, src="vi", dest="en")
    b = a.text
    box1.delete(1.0,END)
    box1.insert(END,b)
def translateop():
    INPUTS = box.get(1.0, END)
    print(INPUTS)
    v = Translator()
    d = v.translate(INPUTS, src="en", dest="vi")
    e = d.text
    box1.delete(1.0,END)
    box1.insert(END, e)
clear_button= Button(button_frame,text="Xóa text", font=(("Arial"),10,"bold"),bg="#303030" , fg="#FFFFFF", command=clear1)
clear_button.place(x=90,y=300)
trans_button= Button(button_frame,text="Dịch sang EN", font=(("Arial"),10,"bold"),bg="#303030" , fg="#FFFFFF",command=translate)
trans_button.place(x=185,y=300)
trans_button= Button(button_frame,text="Dịch sang VI", font=(("Arial"),10,"bold"),bg="#303030" , fg="#FFFFFF",command=translateop)
trans_button.place(x=310,y=300)

box1 =Text(root, width=28, height=8, font=("ROBOTO",16))
box1.pack(pady= 40)

root.mainloop()