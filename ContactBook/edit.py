from tkinter import *
from PIL import Image,ImageTk
from  contactbook import *
from sqlite3 import *
import tkinter.messagebox as tmsg
class Edit(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x900")
        self.title("Edit")
        self.maxsize(600,900)
        self.minsize(600,900)
        self.wm_iconbitmap("cb.ico")
   
        self.bg = PhotoImage(file = "addpage.png")
        self.label1 = Label(self,image = self.bg,borderwidth=0) 
        self.label1.place(x = 0, y = 0) 

        
        self.connection = connect("My Contacts.db")
        self.curser = self.connection.cursor()



    def entryform(self):
        global contact
        self.image1 = Image.open("back.png")
        self.resize_image1 = self.image1.resize((42,42))
        self.back = ImageTk.PhotoImage(self.resize_image1)

        self.backbutton = Button(self,image=self.back,command=self.backclick,relief=FLAT,bg='#0B0907')
        self.backbutton.grid(row=1,column=1)
        self.backbutton.place(relx=.23,rely=.22,anchor=CENTER)

        
        self.curser.execute("select * from selected")
        contacts = self.curser.fetchall()
    
        
        self.namevar = StringVar()
        self.phonevar = StringVar()
        self.emailvar = StringVar()
        self.addvar = StringVar()
        
        self.nameEntry = Entry(self,textvariable=self.namevar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.nameEntry.grid(row=1,column=4,sticky=EW,padx=12,pady=12)
        self.nameEntry.place(relx=.583,rely=.375,anchor=CENTER)
        self.nameEntry.insert(END,contacts[-1][0])

    

        self.phoneEntry = Entry(self,textvariable=self.phonevar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.phoneEntry.grid(row=2,column=4,sticky=EW,padx=12,pady=12)
        self.phoneEntry.place(relx=.583,rely=.458,anchor=CENTER)
        self.phoneEntry.insert(END,contacts[-1][1])


        self.emailEntry = Entry(self,textvariable=self.emailvar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.emailEntry.grid(row=3,column=4,sticky=EW,padx=12,pady=12)
        self.emailEntry.place(relx=.583,rely=.541,anchor=CENTER)
        self.old_emailEntry = contacts[-1][2]
        self.emailEntry.insert(END,contacts[-1][2])


        self.addEntry = Entry(self,textvariable=self.addvar,bg='#e7c47b',fg='#0B0907',font=("Rajdhani Medium",18, "normal"))
        self.addEntry.grid(row=4,column=4,sticky=EW,padx=12,pady=12)
        self.addEntry.place(relx=.583,rely=.624,anchor=CENTER)  
        self.addEntry.insert(END,contacts[-1][3])


        self.image2 = Image.open("save.png")
        self.resize_image2 = self.image2.resize((33,33))
        self.edit = ImageTk.PhotoImage(self.resize_image2)

        self.savebutton = Button(self,image=self.edit,command=self.save_click,relief=FLAT,bg='#0B0907')
        self.savebutton.grid(row=9,column=1)
        self.savebutton.place(relx=.23,rely=.79,anchor=CENTER)

        self.image3 = Image.open("delete.png")
        self.resize_image3 = self.image3.resize((33,33))
        self.delete = ImageTk.PhotoImage(self.resize_image3)

        self.deletebutton = Button(self,image=self.delete,command=self.delete_click,relief=FLAT,bg='#0B0907')
        self.deletebutton.grid(row=9,column=4)
        self.deletebutton.place(relx=.77,rely=.79,anchor=CENTER)
    


    def backclick(self):
        if self.backbutton :
            self.destroy()
            window = Contact()
            window.entry()
            window.contactlist()
            window.mainloop()



    def save_click(self):
        self.curser.execute("update Contact set Name=?,Phone=?,Email=?,Address=? where Email=?",
            (self.nameEntry.get(),self.phoneEntry.get(),self.emailEntry.get(),self.addEntry.get(),self.old_emailEntry))
        self.connection.commit()
        tmsg.showinfo("Edit Contact","Contact details are updated")

        self.destroy()
        window = Contact()
        window.entry()
        window.contactlist()
        window.mainloop()



    def delete_click(self):
        if(tmsg.askquestion("Delete","Are you sure to delete") == 'yes'):
            self.curser.execute("delete from Contact where Email=?",
            (self.old_emailEntry,))
            self.connection.commit()
            tmsg.showinfo("Delete Contact","Contact details are deleted")

        self.destroy()
        window = Contact()
        window.entry()
        window.contactlist()
        window.mainloop()        


