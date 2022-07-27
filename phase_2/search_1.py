from tkinter import*
from tkinter import ttk
from tkinter import messagebox



class Search1_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Blood Bank")
        self.root.geometry("1000x630+20+70")
        self.root.config(bg="red")
        
        global search_item_name
        global Table_Frame_2
        self.search_item_name = StringVar()
        
        
        Table_Frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="DONOR DETAILS",font=("times new roman",15,"bold"),padx=2)
        Table_Frame.config(bg="red",fg="white")
        Table_Frame.place(x=2,y=2,width=1158,height=622)

        lbl_searchframe=Label(Table_Frame,text="Search:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_searchframe.config(bg="red",fg="white")
        lbl_searchframe.grid(row=0,column=0,sticky=W)
        lbl_searchframe=ttk.Entry(Table_Frame,textvariable=self.search_item_name,width=29,font=("arial",11,"bold"))
        lbl_searchframe.grid(row=0,column=1)

        btnadd=Button(Table_Frame,text="Search",command=self.searchitem,font=("arial",14,"bold"),bg="white",fg="red",width=7)
        btnadd.grid(row=0,column=2,padx=1)
        
        btn_showall=Button(Table_Frame,text="Reset",command=self.resetframe,font=("arial",14,"bold"),bg="white",fg="red",width=7)
        btn_showall.grid(row=0,column=3,padx=1)
        
        btn_showall=Button(Table_Frame,text="Exit",command=self.exitframe,font=("arial",14,"bold"),bg="white",fg="red",width=7)
        btn_showall.grid(row=0,column=4,padx=1)
        
        Table_Frame_2=LabelFrame(self.root,bd=4,relief=RIDGE,font=("times new roman",15,"bold"),padx=2)
        Table_Frame_2.config(bg="red",fg="white")
        Table_Frame_2.place(x=10,y=80,width=1150,height=536)
        
        Label(Table_Frame_2, text='Date ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=0)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=1)
        Label(Table_Frame_2, text='Donor Id', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=2)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=3)
        Label(Table_Frame_2, text='Name', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=4)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=5)
        Label(Table_Frame_2, text='Blood Group ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=6)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=7)
        Label(Table_Frame_2, text='Age ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=8)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=9)
        Label(Table_Frame_2, text='Phone no. ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=10)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=11)
        Label(Table_Frame_2, text='Address ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=12)
        Label(Table_Frame_2, text='           ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=13)
        Label(Table_Frame_2, text='Quantity ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=14)

        
#reseting frame        
    def resetframe(self):
        self.search_item_name.set("")
         
#exiting frame        
    def exitframe(self):
        self.root.destroy() 
    
    
        
                      
#search    
    def searchitem(self):
        if self.search_item_name.get()=="":
            messagebox.showinfo("NOT FOUND","Enter Blood Group to be searched")
        elif self.search_item_name.get():
            search_item=self.search_item_name.get()
            i = 1
            for line in open("user.txt", "r").readlines():
                display = line.split()
                if display[3] == search_item or display[6] == search_item or display[7]==search_item:
                    Label(Table_Frame_2, text=display[0], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=0)
                    Label(Table_Frame_2, text=display[1], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=2)
                    Label(Table_Frame_2, text=display[2], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=4)
                    Label(Table_Frame_2, text=display[3], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=6)
                    Label(Table_Frame_2, text=display[4], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=8)
                    Label(Table_Frame_2, text=display[5], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=10)
                    Label(Table_Frame_2, text=display[6], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=12)
                    Label(Table_Frame_2, text=display[7], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=14)
                    i = i + 1
                    
        
if __name__ == "__main__":
    root = Tk()
    obj=Search1_Window(root)
    root.mainloop()



 
                                     
              
                    
                   
    