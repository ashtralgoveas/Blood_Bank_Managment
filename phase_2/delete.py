from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from typing import ItemsView


class Delete_Window:
        def __init__(self,root):
                self.root=root
                self.root.title("Blood Bank Management System")
                self.root.geometry("1430x630+20+70")
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
                labelframeleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="DELETE DONOR DETAILS",font=("times new roman",15,"bold"),pady=2)
                labelframeleft.place(x=30,y=100,width=340,height=370)
                labelframeleft.config(bg="red",fg="white")
      

#==========label================================= 
                  
                # Donor
                lbl_bid=Label(labelframeleft,text="Donor Id:",font=("arial",14,"bold"),padx=2,pady=5)
                lbl_bid.config(bg="red",fg="white")
                lbl_bid.grid(row=0,column=1,sticky=W)
                entry_ref=ttk.Entry(labelframeleft,textvariable=donor_id,width=19,font=("arial",13,"bold"))
                entry_ref.grid(row=0,column=2)
        

#========btn===============================
                btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
                btn_frame.config(bg="red")
                btn_frame.place(x=70,y=200,width=277,height=36)

                # delete
                btndelete=Button(btn_frame,text=" Delete ",command=confirmdelete,font=("arial",12,"bold"),bg="white",fg="red",width=7)
                btndelete.grid(row=0,column=0,padx=1)
                # reset
                btnreset=Button(btn_frame,text="Reset",command=resetframe,font=("arial",12,"bold"),bg="white",fg="red",width=8)
                btnreset.grid(row=0,column=1,padx=1)
                # exit
                btnreset=Button(btn_frame,text=" Exit ",command=exitframe,font=("arial",12,"bold"),bg="white",fg="red",width=8)
                btnreset.grid(row=0,column=2,padx=1)
 


#==========data_table==============================
                Table_Frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="DONOR DETAILS",font=("times new roman",15,"bold"),fg="white",padx=2)
                Table_Frame.place(x=380,y=25,width=990,height=600)
                Table_Frame.config(bg="red")
                details_table=Frame(Table_Frame,bd=2,relief=RIDGE,bg="red")
                details_table.place(x=0,y=10,width=985,height=550)

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
                fetch_data()


def fetch_data():
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
                

#reseting frame
def resetframe():
            donor_id.set("")
            
#exiting frame            
def exitframe():
            root.destroy()        

#deleting data
def confirmdelete():
            if donor_id.get()=="":
                    messagebox.showinfo("NOT FOUND","Enter the donor name to be deleted")
            else:
                    global items
                    global found
                    found=False
                    item_name_info = donor_id.get()
                    temp = list()
                    fhand=open("user.txt","r")
                    data = fhand.read()
                    fhand.close()
                    records = data.split("\n")
                    del records[-1]
                    for record in records:
                            items=record.split(" ")
                            if items[1]==item_name_info:
                                    records.remove(record)
                                    found=True
                                    break
                        
                    if found==True:
                            fhand = open("user.txt", "w")
                            for record in records:
                                    fhand.write(record)
                                    fhand.write('\n')  
                                    fhand.close()   
                                    fetch_data()     
                                    messagebox.showinfo("SUCCESS","Donor details Deleted Successfully")
                                    resetframe()
                                    
                            
                
                    

            
                 
                            
if __name__ == "__main__":
    root = Tk()
    obj=Delete_Window(root)
    root.mainloop()


