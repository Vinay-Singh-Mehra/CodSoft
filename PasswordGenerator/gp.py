import random
import string
from tkinter import *
def password():
    charValues = string.ascii_letters + string.digits + string.punctuation
    pass_len = int(passValue.get())
    res ="".join([random.choice(charValues) for i in range(pass_len)])
    # print(res)
    with open("pass.txt","w") as f:
        f.write(f"{res}")
        
def click(event):
    global value
    value.set("")
    with open("pass.txt","r") as f:
      data = f.read()
    print(data)
    value.set(data)
    label4.update()

def quit():
    root.destroy()
    with open("pass.txt","w") as f:
        f.close()

def reset():
    passValue.set("")
    value.set("")
# GUI:-
root = Tk()
root.title("Password Generator")
root.geometry("444x344")
label1 = Label(root,text="Password Generator",font="lucida 18 bold",fg="white",bg="blue")
label1.grid(row=0,column=1)
label2 = Label(root,text="Password Length",font="lucida 12 normal",pady=35)
label2.grid(row=5,column=0)

passValue = StringVar()
passEntry= Entry(root,textvariable=passValue,font="lucida 12 italic")
passEntry.grid(row=5,column=1)

GP = Button(text="Generate Password",command=password,fg="green",bg="yellow",font="lucida 15 bold",relief=SUNKEN)
GP.grid(row=6,column=1)
GP.bind('<Button-1>',click)

value = StringVar()
label3 = Label(root,text="Your Password: ",font="lucida 12 normal",pady=35)
label3.grid(row=8,column=0)

label4 = Entry(root,textvariable=value,font="lucida 12 italic")
label4.grid(row=8,column=1)

reset = Button(root,text="Reset",command=reset,bg="green",fg="light yellow",font="lucida 15 normal",relief=SUNKEN)
reset.grid(row=9,column=0)

quit = Button(root,text="Quit",command=quit,font="lucida 15 normal",bg="red",fg="white",relief=SUNKEN)
quit.grid(row=9,column=2)

root.mainloop()

