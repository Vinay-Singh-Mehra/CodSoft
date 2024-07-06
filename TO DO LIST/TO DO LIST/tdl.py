from  tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as tmsg
root = Tk()
root.title("TO DO LIST")
root.geometry("544x744")
root.maxsize(544,744)
root.wm_iconbitmap('3.ico')
bg = PhotoImage(file = "bg.png")
# Show image using label 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 

def add():
    task = taskValue.get()
    if task:
        listbox.insert(END,"   •  "+task)
        taskValue.set("")
    else:
        tmsg.showerror("Error!","Please! enter a task")


def remove():
    selectedTask = listbox.curselection()
    if selectedTask:
        listbox.delete(selectedTask)
    else:
        tmsg.showerror("Error!","Please! select a task to remove")


image = Image.open("m1.png")
resize_image = image.resize((95,95))
img = ImageTk.PhotoImage(resize_image)
label2 = Label(root,image=img,borderwidth=4,relief=RIDGE)
label2.config(bg="tan")
label2.pack(pady=2)



taskValue = StringVar()
taskEntry = Entry(root,textvariable=taskValue,font="cambria 16 normal",bg="beige",borderwidth=7).pack(pady=4)

image1 = Image.open("plus.png")
resize_image1 = image1.resize((47,47))
img1 = ImageTk.PhotoImage(resize_image1)

b1 = Button(root,image=img1,command=add,borderwidth=7)
b1.pack(pady=12)

f = Frame(root,bg="chocolate",borderwidth=2)
listbox = Listbox(f,selectmode=SINGLE,font="cambria 20 normal")
scrollbar = Scrollbar(f,orient=VERTICAL,bg="black")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
f.pack(padx=22,pady=10)
listbox.pack(side=RIGHT,expand=True,fill=BOTH)
scrollbar.pack(side=LEFT,fill=Y)

image2 = Image.open("minus.png")
resize_image2 = image2.resize((47,47))
img2 = ImageTk.PhotoImage(resize_image2)
b2 = Button(root,image=img2,command=remove,borderwidth=7)
b2.pack(pady=12)

root.mainloop()

