
# coding: utf-8

# In[ ]:


import datetime 
from tkinter import*
import tkinter.messagebox as msg
import time
import sqlite3



root =Tk()
root.title("Employee Managment System")
root.geometry('1350x655+0+0')

Tops=Frame(root,width=1350 ,height=50,bd=8 ,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=600 ,height=600,bd=8 ,relief="raise")
f1.pack(side=LEFT)


f2=Frame(root,width=300 ,height=700,bd=8 ,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=600 ,height=300,bd=20 ,relief="raise")
f1a.pack(side=TOP)


f1b=Frame(f1,width=600 ,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)


#info title
lbinfo=Label(Tops, font=('times new roman',60,'bold'),text="Employee Managment Systems",bd=10)
lbinfo.grid(row=0,column=0)


#Define Name

Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
Department=StringVar()
HourlyRate=StringVar()
Taxable=StringVar()
OverTimeHours=StringVar()
GrossPayable=StringVar()
NetPayable=StringVar()
wageshour=StringVar()
Payable=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
DateOfOrder.set(time.strftime("%d/%m/%Y"))


def database():
        name1=Name.get()
        add1=Address.get()
        hrd=HoursWorked.get()
        dep=Department.get()
        rate=HourlyRate.get()
        tax=Taxable.get()
        ovr=OverTimeHours.get()
        gross=GrossPayable.get()
        net=NetPayable.get()
    
        conn = sqlite3.connect('emp.db')
        with conn:
          cursor=conn.cursor()
          cursor.execute('CREATE TABLE IF NOT EXISTS emp (name1 TEXT,add1 TEXT,hrd TEXT,dep TEXT,rate TEXT,tax TEXT,ovr TEXT,gross TEXT,net TEXT)')
          cursor.execute('INSERT INTO emp (name1,add1,hrd,dep,rate,tax,ovr,gross,net) VALUES(?,?,?,?,?,?,?,?,?)',(name1,add1,hrd,dep,rate,tax,ovr,gross,net))
          conn.commit()
            
    
def reset():
        Name.set("")
        Address.set("")
        Department.set("")
        HoursWorked.set("")
        HourlyRate.set("")
        Taxable.set("")
        OverTimeHours.set("")
        GrossPayable.set("")
        NetPayable.set("")
        wageshour.set("")
        txtPaySlip.delete("1.0",END)
        Payable.set("")

def Enterinfo():
        txtPaySlip.insert(END,"\t\tPAY-SLIP\n\n")
        txtPaySlip.insert(END,"Name:\t\t"+Name.get()+"\n\n")
        txtPaySlip.insert(END,"Address:\t\t"+Address.get()+"\n\n")
        txtPaySlip.insert(END,"Employer\t\t"+Department.get()+"\n\n")
        txtPaySlip.insert(END,"Hours Worked\t\t"+HoursWorked.get()+"\n\n")
        txtPaySlip.insert(END,"Net Payable\t\t"+NetPayable.get()+"\n\n")
        txtPaySlip.insert(END,"Wages Per Hour\t\t"+HourlyRate.get()+"\n\n")
        txtPaySlip.insert(END,"Tax Paid\t\t"+Taxable.get()+"\n\n")
        txtPaySlip.insert(END," Payable\t\t"+ GrossPayable.get()+"\n\n")

def dailywages():
        HoursWorkedPerWeek=float(HoursWorked.get())
        WagesPerHours=float(HourlyRate.get())
        
        paydue=WagesPerHours*HoursWorkedPerWeek
        PaymentDue="Rs.",str('%.2f'%(paydue))
        GrossPayable.set(PaymentDue)

        tax=paydue*0.2
        Taxables="Rs.",str('%.2f'%(tax))
        Taxable.set(Taxables)

        netpay=paydue-tax
        NetPays="Rs.",str('%.2f'%(netpay))
        NetPayable.set(NetPays)

    
        if HoursWorkedPerWeek>40:
            overTimeHours=(HoursWorkedPerWeek-40)+WagesPerHours*1.5
            Overtimehrs="Rs.",str('%.2f'%( overTimeHours))
            OverTimeHours.set(Overtimehrs)
            
        elif HoursWorkedPerWeek<=40:
            overTimePay=(HoursWorkedPerWeek-40)+WagesPerHours*1.5
            Overtimehrs="Rs.",str('%.2f'%( overtimePay))
            OverTimeHours.set(Overtimehrs)
        
    
        return
            
   

            
#Labels Display
lbName=Label(f1a,text="Name",font=('arial',16,'bold'),bd=20).grid(row=0,column=0)
lbAddress=Label(f1a,text="Address",font=('arial',16,'bold'),bd=20).grid(row=0,column=2)
lbDepartment=Label(f1a,text="Department",font=('arial',16,'bold'),bd=20).grid(row=1,column=0)
lbHoursWorked=Label(f1a,text="Hours Worked",font=('arial',16,'bold'),bd=20).grid(row=2,column=0)
lbHourlyRate=Label(f1a,text="Hourly Rate",font=('arial',16,'bold'),bd=20).grid(row=1,column=2)
llTax=Label(f1a,text="Tax",font=('arial',16,'bold'),bd=20 ,anchor='w').grid(row=3,column=0)
lblOvertime=Label(f1a,text="OverTime",font=('arial',16,'bold'),bd=20).grid(row=2,column=2)
lbGrossPay=Label(f1a,text="GrossPay",font=('arial',16,'bold'),bd=20).grid(row=4,column=0)
lbNetPay=Label(f1a,text="NetPay",font=('arial',16,'bold'),bd=20).grid(row=3,column=2)

#Entry

etxName=Entry(f1a,textvariable=Name ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxName.grid(row=0,column=1)


etxAddress=Entry(f1a,textvariable=Address ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxAddress.grid(row=0,column=3)

etxDepartment=Entry(f1a,textvariable=Department ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxDepartment.grid(row=1,column=1)

etxHoursWorked=Entry(f1a,textvariable=HoursWorked ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxHoursWorked.grid(row=2,column=1)

etxHourlyRate=Entry(f1a,textvariable=HourlyRate ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxHourlyRate.grid(row=1,column=3)

etxTaxable=Entry(f1a,textvariable=Taxable ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxTaxable.grid(row=3,column=1)

etxOverTimeHours=Entry(f1a,textvariable=OverTimeHours ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxOverTimeHours.grid(row=2,column=3)

etxGrossPayable=Entry(f1a,textvariable=GrossPayable ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxGrossPayable.grid(row=4,column=1)

etxNetPayable=Entry(f1a,textvariable=NetPayable ,font=('arial',16,'bold'),bd=16,width=22,justify='left')
etxNetPayable.grid(row=3,column=3)



#Text widget

lbPaySlip=Label(f2,font=('times new roman',21,'bold'),textvariable=DateOfOrder).grid(row=0,column=0)
txtPaySlip=Text(f2, height=22,width=34,bd=16,font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)



#Belo buttons

btnSalary=Button(f1b,text="Weekly Salary",padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold')
                 ,width=14,height=1,command=dailywages).grid(row=0,column=0)


btnReset=Button(f1b,text="Reset",padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),
                width=14,height=1,command=reset).grid(row=0,column=1)


btnPaySlip=Button(f1b,text="View PaySlip",padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),
                width=14,height=1,command=Enterinfo).grid(row=0,column=2)


#btnExit=Button(f1b,text="Exit-System",padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),
 #               width=14,height=1,command=iExit).grid(row=0,column=3)


btnExit=Button(f1b,text="Upload-Data",padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),
                width=14,height=1,command=database ).grid(row=0,column=3)


            
root.mainloop()


