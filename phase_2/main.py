from tkinter import*
from tkinter import messagebox
from add import Add_Window
from display import Display_Window
from search_1 import Search1_Window
from update import Update_Window
from delete import Delete_Window


#======class=====================================
class BBManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Blood Bank Management System")
        self.root.geometry("500x500+100+500")
        self.root.config(bg="red")

#======title========================================
        lbl_title=Label(self.root,text="BLOOD BANK MANAGEMENT SYSTEM",font=("times new roman",20,"bold"),bg="Red",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=50)


#====mainframe=======================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        main_frame.place(x=0,y=50,width=1400,height=700)

#======menu==========================================
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="red",fg="white",bd=8,relief=RIDGE)
        lbl_menu.place(x=600,y=85,width=185)


#======btn frame========================================
        btn_frame=Frame(main_frame,bd=3,relief=RIDGE)
        btn_frame.place(x=600,y=139,width=185,height=260)

        add_btn=Button(btn_frame,text="ADD DONOR DETAILS",command=self.logic_part1,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        add_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="DISPLAY DETAILS",command=self.logic_part2,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        update_btn.grid(row=1,column=0)
        
        update_btn=Button(btn_frame,text="SEARCH DONOR",command=self.logic_part3,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        update_btn.grid(row=2,column=0)
        
        update_btn=Button(btn_frame,text="UPDATE DONOR DETAILS",command=self.logic_part4,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        update_btn.grid(row=3,column=0)
        
        delete_btn=Button(btn_frame,text="DELETE DONOR DETAILS",command=self.logic_part5,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        delete_btn.grid(row=4,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",10,"bold"),bg="red",fg="white",bd=10,cursor="hand1")
        logout_btn.grid(row=5,column=0)

#=======def============================================= 

#add data      
    def logic_part1(self):
            self.new_window=Toplevel(self.root)
            self.app=Add_Window(self.new_window)
#display data            
    def logic_part2(self):
            self.new_window=Toplevel(self.root)
            self.app=Display_Window(self.new_window)
#search data            
    def logic_part3(self):
            self.new_window=Toplevel(self.root)
            self.app=Search1_Window(self.new_window)                        
#update data            
    def logic_part4(self):
            self.new_window=Toplevel(self.root)
            self.app=Update_Window(self.new_window)   
#delete data            
    def logic_part5(self):
            self.new_window=Toplevel(self.root)
            self.app=Delete_Window(self.new_window)            
#logout
    def logout(self):
        messagebox.showinfo("SUCCESS","Logged out Successfully")
        self.root.destroy()




if __name__ == "__main__":
        root = Tk()
        obj=BBManagementSystem(root)
        root.mainloop()
