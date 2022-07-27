
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import ItemsView
from tkcalendar import *



class Update_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Blood Bank Management System")
        self.root.geometry("1330x630+20+70")
        self.root.config(bg="red")


#===============declaring==================
        global donor_last_date
        global donor_id
        global donor_name
        global donor_bg
        global donor_age
        global donor_phone
        global donor_addr
        global details_table
        global qty
                

        donor_last_date=StringVar()
        donor_id=StringVar()
        donor_name=StringVar()
        donor_bg=StringVar()
        donor_age=StringVar()
        donor_phone=StringVar()
        donor_addr=StringVar()
        qty=IntVar()






#============labelframe=========================
        labelframeleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="UPDATE DONOR DETAILS",font=("times new roman",15,"bold"),pady=2)
        labelframeleft.config(bg="red",fg="white")
        labelframeleft.place(x=5,y=25,width=420,height=600)
      

#==========label=================================
       

#==========label=================================
        # Date  
        Label(labelframeleft,text="Donation Date Date:",font=("arial",14,"bold"),bg="red",fg="white").grid(row=0,column=0,padx=2,pady=6,sticky=W)
        entry_ref=DateEntry(labelframeleft,textvariable=  donor_last_date,width=15,font=("arial",12,"bold"))
        entry_ref.grid(row=0,column=1,padx=2,pady=6)

                # id
        lbl_id=Label(labelframeleft,text="Donor Id:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_id.config(bg="red",fg="white")
        lbl_id.grid(row=1,column=0,sticky=W)
        entry_id= Entry(labelframeleft,textvariable=  donor_id,width=18,font=("arial",13,"bold"))
        entry_id.grid(row=1,column=1)        
                
                # name
        lbl__name=Label(labelframeleft,text="Donor Name:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl__name.config(bg="red",fg="white")
        lbl__name.grid(row=2,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  donor_name,width=18,font=("arial",12,"bold"))
        entry_ref.grid(row=2,column=1)
                
                # bg
        lbl_bg=Label(labelframeleft,text="Blood Group:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_bg.config(bg="red",fg="white")
        lbl_bg.grid(row=3,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  donor_bg,width=18,font=("arial",12,"bold"))
        entry_ref.grid(row=3,column=1) 
                        
                # age
        lbl_age=Label(labelframeleft,text="Age:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_age.config(bg="red",fg="white")
        lbl_age.grid(row=4,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  donor_age,width=18,font=("arial",13,"bold"))
        entry_ref.grid(row=4,column=1)        
                # mobile No.
        lbl_mob=Label(labelframeleft,text="Mobile No.:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_mob.config(bg="red",fg="white")
        lbl_mob.grid(row=5,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  donor_phone,width=18,font=("arial",13,"bold"))
        entry_ref.grid(row=5,column=1)  

                # address
        lbl_adrs=Label(labelframeleft,text="Address              ",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_adrs.config(bg="red",fg="white")
        lbl_adrs.grid(row=6,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  donor_addr,width=18,font=("arial",12,"bold"))
        entry_ref.grid(row=6,column=1)      
                        
                # Quantity 
        lbl_quantity=Label(labelframeleft,text="Quantity:",font=("arial",14,"bold"),padx=2,pady=6)
        lbl_quantity.config(bg="red",fg="white")
        lbl_quantity.grid(row=7,column=0,sticky=W)
        entry_ref= Entry(labelframeleft,textvariable=  qty,width=18,font=("arial",12,"bold"))
        entry_ref.grid(row=7,column=1)

#========btn===============================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=95,y=400,width=277,height=36)

        
        # update
        btnupdate=Button(btn_frame,text="Update",command=self.confirm_update,font=("arial",12,"bold"),bg="white",fg="red",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        # reset
        btnreset=Button(btn_frame,text="Reset",command=self.resetframe,font=("arial",12,"bold"),bg="white",fg="red",width=8)
        btnreset.grid(row=0,column=2,padx=1)
        # exit
        btnreset=Button(btn_frame,text="Exit",command=self.exitframe,font=("arial",12,"bold"),bg="white",fg="red",width=8)
        btnreset.grid(row=0,column=3,padx=1)


#========table_frame=============================
        Table_Frame=LabelFrame(  root,bd=4,relief=RIDGE,text="DONOR DETAILS",font=("times new roman",15,"bold"),padx=2)
        Table_Frame.config(bg="red",fg="white")
        Table_Frame.place(x=390,y=25,width=1018,height=600)
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE,bg="red")
        details_table.place(x=4,y=10,width=995,height=550)

        Label(details_table, text='Date ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=0)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=1)
        Label(details_table, text='Donor Id', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=2)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=3)
        Label(details_table, text='Name', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=4)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=5)
        Label(details_table, text='Blood_Group ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=6)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=7)
        Label(details_table, text='Age ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=8)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=9)
        Label(details_table, text='Mobile no. ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=10)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=11)
        Label(details_table, text='Address ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=12)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=13)
        Label(details_table, text='Quantity ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=14)
        self.fetch_data()
                
        

    def fetch_data(self):
            i = 1
            for line in open("user.txt", "r").readlines():
                    display = line.split()
                    Label(details_table, text=display[0], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=0)
                    Label(details_table, text=display[1], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=2)
                    Label(details_table, text=display[2], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=4)
                    Label(details_table, text=display[3], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=6)
                    Label(details_table, text=display[4], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=8)
                    Label(details_table, text=display[5], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=10)
                    Label(details_table, text=display[6], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=12)
                    Label(details_table, text=display[7], font=('arial',12,"bold"),bg="red",fg="white").grid(row=i, column=14)
                    i = i + 1           

                


    def resetframe():
              donor_last_date.set("")
              donor_id.set("")
              donor_name.set("")
              donor_bg.set("")
              donor_age.set("")
              donor_addr.set("")
              donor_phone.set("")
              qty.set("")
            

    def exitframe(self):
            self.root.destroy()        
                            
                 
                            
    def confirm_update(self):
                if   donor_last_date.get()=="":
                    messagebox.showinfo("Date is required")
                elif   donor_id.get()=="":
                        messagebox.showinfo("Id cannot be empty")
                elif   donor_name.get()=="":
                        messagebox.showinfo("name cannot be empty")
                elif   donor_bg.get()=="":
                        messagebox.showinfo("Blood_group cannot be empty")
                elif   donor_age.get()=="":
                        messagebox.showinfo("Age cannot be empty")
                elif   donor_phone.get()=="":
                        messagebox.showinfo("Mobile no. is required")
                elif   donor_addr.get()=="":
                        messagebox.showinfo("Address is required")  
                elif   qty.get()=="":
                        messagebox.showinfo("QuaNtity is required")
                else:
                        item_1 =   donor_last_date.get()
                        item_2=   donor_id.get()
                        item_3=   donor_name.get()
                        item_4 =   donor_bg.get()
                        item_5 =   donor_age.get()
                        item_6 =   donor_phone.get()
                        item_7 =   donor_addr.get()
                        item_8=   qty.get()
                    
                file=open("sample.txt","w")
                res = item_1 +" "+ str(item_2)+" "+ item_3+" "+ item_4 +" "+ str(item_5)+" "+ item_6+" "+ item_7+" "+str(item_8)
                file.write(res)
                file.close()
                    
                global items
                global found
                found=False
                    
                fhand=open("user.txt","r")
                data = fhand.read()
                fhand.close()
                records = data.split("\n")
                del records[-1]
                for record in records:
                        items=record.split(" ")
                        if items[1]==item_2:
                                records.remove(record)
                                found=True
                                break
                        
                        if found==True:
                            fhand = open("user.txt", "w")
                            for record in records:
                                    fhand.write(record)
                                    fhand.write('\n')  
                                    fhand.close()   
                                        
                    
                with open('sample.txt','r') as sample, open('user.txt','a') as user:
                        for record in sample:
                                user.write(record)
                                user.write('\n')
                                    
                sample.close()
                user.close()      
                    
                                
                dum = open("sample.txt","r+")
                dum.seek(0)
                dum.truncate()
                dum.close()
                self.fetch_data()
                messagebox.showinfo("SUCCESS","Donor Details Updated Successfully")
                self.resetframe()                           






if __name__ == "__main__":
    root = Tk()
    obj=Update_Window(root)
    root.mainloop()
