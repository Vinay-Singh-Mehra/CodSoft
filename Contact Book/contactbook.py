from tkinter import *
from PIL import Image,ImageTk
from sqlite3 import *
import tkinter.messagebox as tmsg
import edit
import addpage

class Contact(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x900")
        self.maxsize(600,900)
        self.minsize(600,900)

        self.title("Contact Book")
        self.wm_iconbitmap('cb.ico')

        self.bg = PhotoImage(file = "mainy.png")
        self.label1 = Label(self, image = self.bg,borderwidth=0) 
        self.label1.place(x = 0, y = 0) 

        
        self.connection = connect("My Contacts.db")
        self.curser = self.connection.cursor()



    def searchbar(self,event):
        self.lbx.delete(0,END)
        self.curser.execute("select * from Contact where Name like ?",('%'+self.entry.get()+'%',))
        self.fill_contacts()     


        
    def fill_contacts(self):
        contacts = self.curser.fetchall()
    
        for contact in contacts:
            self.lbx.insert(END,contact[0])



    def addClick(self):
        if self.addbutton :
            self.destroy()
            
            wdw = addpage.AddPage()
            wdw.addcont()
            wdw.savebutton()
            wdw.mainloop()


          

    def entry(self):
        self.frame = Frame(self,bg="#FFFFFF") 
        self.frame.pack(padx=12,pady=12)
        self.frame.place(relx=.474,rely=.19,anchor=CENTER)
        
        self.entryvar = StringVar()
        self.entry = Entry(self.frame,font=("Rajdhani Light",20,"bold"),borderwidth=0,bg='#FFFFFF',fg='#0B0907',relief=FLAT)
        self.entry.pack(padx=2,pady=2)
        self.entry.bind('<KeyRelease>',self.searchbar)




    def contactlist(self):
        self.frame = Frame(self)
        self.frame.pack(padx=22,pady=10)
        self.frame.configure(bg="#0B0907")
        self.frame.place(relx=.51,rely=.581,anchor=CENTER,width=380,height=480)
        Label(self.frame,text="Contacts",font=("Rajdhani Regular", 27,"bold"),bg='#0B0907',fg='#E7C47B').pack(padx=6,pady=6,anchor="w")
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.lbx = Listbox(self.frame,yscrollcommand=self.scrollbar.set,bg="#0B0907",fg="#D9D9D9",
                           font=("Rajdhani Light",20,"bold"),highlightthickness=0,relief=FLAT)
        self.lbx.pack(padx=12,pady=12,fill=BOTH,expand=TRUE,side=BOTTOM) 
        self.scrollbar.config(command=YView)


        self.curser.execute("select * from Contact order by Name")
        self.fill_contacts()


        self.lbx.bind('<<ListboxSelect>>',self.contact_select_click)



        self.image1 = Image.open("add.png")
        self.resize_image1 = self.image1.resize((32,32))
        self.img1 = ImageTk.PhotoImage(self.resize_image1)


        self.addbutton = Button(self,image=self.img1,command=self.addClick,bg="white",relief=FLAT)
        self.addbutton.pack(padx=12,pady=12,side="bottom",anchor="s")
        self.addbutton.place(relx=.501,rely=.9335,anchor=S)


    def contact_select_click(self,event):
        self.selectedContact = self.lbx.get(self.lbx.curselection())
        self.curser.execute("select*from Contact where Name = ?",(self.selectedContact,))
        self.contact = self.curser.fetchone()

        if self.selectedContact:
            self.curser.execute("insert into selected(Name,Phone,Email,Address)values(?,?,?,?)",
                                (self.contact[0],self.contact[1],self.contact[2],  self.contact[3]))
            self.connection.commit()        
            self.destroy()
            edit_window = edit.Edit() 
            edit_window.entryform()
            edit_window.mainloop()
       


if __name__ == '__main__':
    window = Contact()
    window.tk.call('tk','scaling',1.5)
    window.entry()
    window.contactlist()
    window.mainloop()
