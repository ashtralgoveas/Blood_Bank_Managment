
from tkinter import*
from tkinter import ttk


class Display_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Blood Bank Management System")
        self.root.geometry("870x630+200+70")
        self.root.config(bg="red")
       

        Table_Frame=LabelFrame(self.root,bd=4,relief=RIDGE,text="BLOOD PACKET AVAILABILITY",font=("times new roman",15,"bold"),bg="red",fg="white",padx=2)
        Table_Frame.place(x=0,y=0,width=865,height=626) 
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE,bg="red")
        details_table.place(x=4,y=10,width=848,height=580)

        Label(details_table, text='Blood Group', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=0)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=1)
        Label(details_table, text='350 ml ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=2)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=3)
        Label(details_table, text='450 ml ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=4)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=5)
        Label(details_table, text='Total Count', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=6)
        Label(details_table, text='       ', font=('arial',14,"bold"),bg="red",fg="white").grid(row=0, column=7)

        count_A3_Plus=StringVar()
        count_B3_Plus=StringVar()
        count_AB3_Plus=StringVar()
        count_O3_Plus = StringVar()
        count_A4_Plus=StringVar()
        count_B4_Plus=StringVar()
        count_AB4_Plus=StringVar()
        count_O4_Plus = StringVar()

        count_A3_Minus =StringVar()
        count_B3_Minus=StringVar()
        count_AB3_Minus=StringVar()
        count_O3_Minus=StringVar()
        count_A4_Minus =StringVar()
        count_B4_Minus=StringVar()
        count_AB4_Minus=StringVar()
        count_O4_Minus=StringVar()

        count_APlusTotal = StringVar()
        count_BPlusTotal = StringVar()
        count_ABPlusTotal = StringVar()
        count_OPlusTotal = StringVar()

        count_AMinusTotal=StringVar()
        count_BMinusTotal=StringVar()
        count_ABMinusTotal=StringVar()
        count_OMinusTotal=StringVar()

        def unpack(s):
            ind=s.split('|')
            return ind

        def bloodAvailable():
            buf=''
            addd=[]
            bg=[]
            qty = []
            with open("bloodStored.txt","r") as file:
                while True:
                    ch=file.read(1)
                    if not ch:
                        break
                    if ch!='#':
                        buf=buf+ch
                    else:
                        pos=file.tell()
                        lenbuf=len(buf)
                        fields=unpack(buf)
                        finalpos=pos-lenbuf-1
                        if fields[0][0]!='*':
                            addd.append(finalpos)
                            bg.append(fields[0])
                            qty.append(fields[1])

                        buf=''
                        continue
            file.close()
            return bg,qty,addd

        def displayBloodPackets():
            bg,qty,addd=bloodAvailable()
            countAPlus=0
            countBPlus=0
            countABPlus=0
            countOPlus=0
            countAMinus=0
            countBMinus=0
            countABMinus=0
            countOMinus=0
            count_350A_Plus=0
            count_450A_Plus=0
            count_350B_Plus=0
            count_450B_Plus=0
            count_350AB_Plus=0
            count_450AB_Plus=0
            count_350O_Plus=0
            count_450O_Plus=0
            count_350A_Minus=0
            count_450A_Minus=0
            count_350B_Minus=0
            count_450B_Minus=0
            count_350AB_Minus=0
            count_450AB_Minus=0
            count_350O_Minus=0
            count_450O_Minus=0
            for i in range(len(bg)):
                if bg[i] == 'A+':
                    if qty[i] == '350':
                        count_350A_Plus += 1
                    else:
                        count_450A_Plus += 1
                    countAPlus = count_350A_Plus + count_450A_Plus
                elif bg[i] == 'B+':
                    if qty[i] == '350':
                        count_350B_Plus+= 1
                    else:
                        count_450B_Plus += 1
                    countBPlus = count_350B_Plus + count_450B_Plus
                elif bg[i] == 'AB+':
                    if qty[i] == '350':
                        count_350AB_Plus+= 1
                    else:
                        count_450AB_Plus += 1
                    countABPlus = count_350AB_Plus + count_450AB_Plus
                elif bg[i] == 'O+':
                    if qty[i] == '350':
                        count_350O_Plus+= 1
                    else:
                        count_450O_Plus += 1
                    countOPlus = count_350O_Plus + count_450O_Plus
                elif bg[i] == 'A-':
                    if qty[i] == '350':
                        count_350A_Minus+= 1
                    else:
                        count_450A_Minus += 1
                    countAMinus = count_350A_Minus + count_450A_Minus
                elif bg[i] == 'B-':
                    if qty[i] == '350':
                        count_350B_Minus+= 1
                    else:
                        count_450B_Minus += 1
                    countBMinus = count_350B_Minus + count_450B_Minus
                elif bg[i] == 'AB-':
                    if qty[i] == '350':
                        count_350AB_Minus+= 1
                    else:
                        count_450AB_Minus += 1
                    countABMinus = count_350AB_Minus+ count_450AB_Minus
                elif bg[i] == 'O-':
                    if qty[i] == '350':
                        count_350O_Minus+= 1
                    else:
                        count_450O_Minus += 1
                    countOMinus = count_350O_Minus + count_450O_Minus
            

            count_A3_Plus.set(count_350A_Plus)
            count_B3_Plus.set(count_350B_Plus)
            count_AB3_Plus.set(count_350AB_Plus)
            count_O3_Plus.set(count_350O_Plus)
            count_A4_Plus.set(count_450A_Plus)
            count_B4_Plus.set(count_450B_Plus)
            count_AB4_Plus.set(count_450AB_Plus)
            count_O4_Plus.set(count_450O_Plus)
            count_A3_Minus.set(count_350A_Minus)
            count_B3_Minus.set(count_350B_Minus)
            count_AB3_Minus.set(count_350AB_Minus)
            count_O3_Minus.set(count_350O_Minus)
            count_A4_Minus.set(count_450A_Minus)
            count_B4_Minus.set(count_450B_Minus)
            count_AB4_Minus.set(count_450AB_Minus)
            count_O4_Minus.set(count_450O_Minus)

            count_APlusTotal.set(countAPlus)
            count_BPlusTotal.set(countBPlus)
            count_ABPlusTotal.set(countABPlus)
            count_OPlusTotal.set(countOPlus)
            count_AMinusTotal.set(countAMinus)
            count_BMinusTotal.set(countBMinus)
            count_ABMinusTotal.set(countABMinus)
            count_OMinusTotal.set(countOMinus)



        p1 =Label(details_table,text = 'A+',font=('arial',12,"bold"),bg="red",fg="white").grid(row=1, column=0)
        p2 =Label(details_table,text = 'B+',font=('arial',12,"bold"),bg="red",fg="white").grid(row=5, column=0)
        p3 =Label(details_table,text = 'AB+',font=('arial',12,"bold"),bg="red",fg="white").grid(row=9, column=0)
        p4 =Label(details_table,text = 'O+',font=('arial',12,"bold"),bg="red",fg="white").grid(row=13, column=0)
        p5 =Label(details_table,text = 'A-',font=('arial',12,"bold"),bg="red",fg="white").grid(row=17, column=0)
        p6 =Label(details_table,text = 'B-',font=('arial',12,"bold"),bg="red",fg="white").grid(row=21, column=0)
        p7 =Label(details_table,text = 'AB-',font=('arial',12,"bold"),bg="red",fg="white").grid(row=25, column=0)
        p8 =Label(details_table,text = 'O-',font=('arial',12,"bold"),bg="red",fg="white").grid(row=29, column=0)


        p9 =Label(details_table,textvariable=count_A3_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=1, column=2)
        p10 =Label(details_table,textvariable=count_B3_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=5, column=2)
        p11 =Label(details_table,textvariable=count_AB3_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=9, column=2)
        p12 =Label(details_table,textvariable=count_O3_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=13, column=2)
        p13 =Label(details_table,textvariable=count_A4_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=1, column=4)
        p14 =Label(details_table,textvariable=count_B4_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=5, column=4)
        p15 =Label(details_table,textvariable=count_AB4_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=9, column=4)
        p16 =Label(details_table,textvariable=count_O4_Plus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=13, column=4)
        p17 =Label(details_table,textvariable=count_A3_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=17, column=2)
        p18 =Label(details_table,textvariable=count_B3_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=21, column=2)
        p19 =Label(details_table,textvariable=count_AB3_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=25, column=2)
        p20 =Label(details_table,textvariable=count_O3_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=29, column=2)
        p21 =Label(details_table,textvariable=count_A4_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=17, column=4)
        p22 =Label(details_table,textvariable=count_B4_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=21, column=4)
        p23 =Label(details_table,textvariable=count_AB4_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=25, column=4)
        p24 =Label(details_table,textvariable=count_O4_Minus,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=29, column=4)
        

        p25=Label(details_table,textvariable=count_APlusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=1, column=6)
        p26=Label(details_table,textvariable=count_BPlusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=5, column=6)
        p27=Label(details_table,textvariable=count_ABPlusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=9, column=6)
        p28=Label(details_table,textvariable=count_OPlusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=13, column=6)

        p29=Label(details_table,textvariable=count_AMinusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=17, column=6)
        p29=Label(details_table,textvariable=count_BMinusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=21, column=6)
        p29=Label(details_table,textvariable=count_ABMinusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=25, column=6)
        p29=Label(details_table,textvariable=count_OMinusTotal,font=('arial',12,"bold"),bg="red",fg="white",function=displayBloodPackets()).grid(row=29, column=6)

        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj=Display_Window(root)
    root.mainloop()        