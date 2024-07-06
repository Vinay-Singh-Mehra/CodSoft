from tkinter import *
from PIL import Image,ImageTk
import contactbook
from sqlite3 import *
import tkinter.messagebox as tmsg


class AddPage(Tk):
    def __init__(self): 
        super().__init__()
        self.title("Add Contacts")
        self.geometry("600x900")
        self.maxsize(600,900)
        self.minsize(600,900)
        self.wm_iconbitmap("cb.ico")
    
        self.bg = PhotoImage(file = "addpage.png")
        self.label1 = Label(self, image = self.bg,borderwidth=0) 
        self.label1.place(x = 0, y = 0) 

        self.connection = connect("My Contacts.db")
        self.curser = self.connection.cursor()

    def backclick(self):
        if self.backbutton :
            self.destroy()
            window = contactbook.Contact()
            window.entry()
            window.contactlist()
            window.mainloop()
    

    def saveclick(self):
    
        self.curser.execute("select*from Contact where Email = ?",(self.emailEntry.get(),))
        self.contact = self.curser.fetchone()
        if self.contact == None:
            self.curser.execute("insert into Contact(Name,Phone,Email,Address)values(?,?,?,?)",
                                (self.nameEntry.get(),self.phoneEntry.get(),self.emailEntry.get(), self.addEntry.get()))
            self.connection.commit()
            tmsg.showinfo("Added Message","Contacts details are added")
        else:
            tmsg.showerror("Error!","Contacts details are already added")


        self.destroy()
        window = contactbook.Contact()
        window.entry()
        window.contactlist()

    def addcont(self):

        self.image1 = Image.open("back.png")
        self.resize_image1 = self.image1.resize((42,42))
        self.back = ImageTk.PhotoImage(self.resize_image1)

        self.backbutton = Button(self,image=self.back,command=self.backclick,relief=FLAT,bg='#0B0907')
        self.backbutton.grid(row=1,column=1)
        self.backbutton.place(relx=.23,rely=.22,anchor=CENTER)


        self.image2 = Image.open("save2.png")
        self.resize_image2 = self.image2.resize((33,33))
        self.save = ImageTk.PhotoImage(self.resize_image2)

        self.savebutton = Button(self,image=self.save,command=self.saveclick,relief=FLAT,bg='#0B0907')
        self.savebutton.grid(row=1,column=1)
        self.savebutton.place(relx=.77,rely=.22,anchor=CENTER)

        self.namevar = StringVar()
        self.phonevar = StringVar()
        self.emailvar = StringVar()
        self.addvar = StringVar()
        
        self.nameEntry = Entry(self,textvariable=self.namevar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.nameEntry.grid(row=1,column=4,sticky=EW,padx=12,pady=12)
        self.nameEntry.place(relx=.583,rely=.375,anchor=CENTER)
        

        self.phoneEntry = Entry(self,textvariable=self.phonevar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.phoneEntry.grid(row=2,column=4,sticky=EW,padx=12,pady=12)
        self.phoneEntry.place(relx=.583,rely=.458,anchor=CENTER)

        self.emailEntry = Entry(self,textvariable=self.emailvar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.emailEntry.grid(row=3,column=4,sticky=EW,padx=12,pady=12)
        self.emailEntry.place(relx=.583,rely=.541,anchor=CENTER)

        self.addEntry = Entry(self,textvariable=self.addvar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.addEntry.grid(row=4,column=4,sticky=EW,padx=12,pady=12)
        self.addEntry.place(relx=.583,rely=.624,anchor=CENTER)      


