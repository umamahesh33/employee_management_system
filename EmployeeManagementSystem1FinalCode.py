#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#---------------------------------------->  EMPLOYEE MANAGEMENT SYSTEM   <-----------------------------------------------------#

########################################    DEFINING ADDEMPLOYEE   #############################################
def addemployee():
    
    #<<<------------- defining the submit button in addemployee form ------------->>>#
    def submitadd():
        id = idval.get()                      #getting data from entries...or entry lables
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        salary = salaryval.get()
        addedtime = time.strftime("%H:%M:%S") #to get time
        addeddate = time.strftime("%d/%m/%Y") #to get date
        try:
            strr = 'insert into employeedata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, salary, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),
                                            parent=addroot)
            
            # clearing the entry form after adding details to database only if res==true
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                salaryval.set('')
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addroot)
        strr = 'select * from employeedata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]] #making data as list to print on treeview
            employeetable.insert('', END, values=vv)                    #to show data,employeetable treeview ,prints from starting to end of (vv) values
            
        #<<<--------------- end of defining sumbitbutton of addemployee --------------->>>#
        
    #<<<------------------- creating window for employeedata entry --------------------->>>#    
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Enter details')
    addroot.config(bg='light blue')
    addroot.resizable(False, False) #making window nonresizable
    
    # ------------------------- Addemployee Labels
    
    idlabel = Label(addroot, text='Enter Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address: ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)  # DCAE96

    genderlabel = Label(addroot, text='Enter Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    salarylabel = Label(addroot, text='Enter Salary : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    salarylabel.place(x=10, y=370)

    #------------------- Addemployee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    salaryval = StringVar()

    #------------------- Addemployee entry lables
    identry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=idval, width=18)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=nameval, width=18)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=mobileval, width=18)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=emailval, width=18)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=addressval, width=18)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=genderval, width=18)
    genderentry.place(x=250, y=310)

    salaryentry = Entry(addroot, font=('Helvetica', 15, 'bold'), bd=3, textvariable=salaryval, width=18)
    salaryentry.place(x=250, y=370)
    
    #------------------------- addemployee submit button
    submitbtn = Button(addroot, text="Submit", bd=3, font=("Bodoni", 16, "bold"), width=10)
    submitbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue", command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()
########################################    END OF ADDEMPLOYEE   #############################################

########################################   DEFINING SEARCHEMPLOYEE   #########################################
def searchemployee():
    
    #<<<------------- defining the search button in searchemployee form ------------->>>#
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        salary = salaryval.get()
        addeddate = time.strftime("%d/%m/%Y")
        
        #<<<--------------- code for searching records ------------->>>#
        if (id != ''):                                       
            strr = 'select *from employeedata1 where id=%s'    #it will select all records with the entered value
            mycursor.execute(strr, (id))                       #executing that statement
            datas = mycursor.fetchall()                        #it will fetch all records and stores in datas
            employeetable.delete(*employeetable.get_children())# it will clear the console(showdataframe)
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]#it will print the fetched data of the searched record on the console
                employeetable.insert('', END, values=vv)  # it will print fetched record from starting to end of that value
        elif (name != ''):
            strr = 'select *from employeedata1 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select *from employeedata1 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select *from employeedata1 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select *from employeedata1 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select *from employeedata1 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
        elif (salary != ''):
            strr = 'select *from employeedata1 where salary=%s'
            mycursor.execute(strr, (salary))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)

        elif (addeddate != ''):
            strr = 'select *from employeedata1 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            employeetable.delete(*employeetable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                employeetable.insert('', END, values=vv)
                
    #<<<--------- end of searching records code ---------->>>#
    
    #<<<--------- creating a window of searching from ----------->>>#
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('search records')
    searchroot.config(bg='light blue')
    searchroot.resizable(False, False)
    
    # --------------------------------search employee Labels
    idlabel = Label(searchroot, text='Enter Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address: ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)  # DCAE96

    genderlabel = Label(searchroot, text='Enter Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    salarylabel = Label(searchroot, text='Enter Salary : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    salarylabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    #----------------------------------search employee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    salaryval = StringVar()
    dateval = StringVar()

    #-----------------------------------saerch employee entrylables
    identry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    salaryentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=salaryval)
    salaryentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('arial', 13, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
    
    #------------------------- search button
    searchbtn = Button(searchroot, text='Search', bd=3, font=("Bodoni", 16, "bold"), width=10, command=search)
    searchbtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue")
    searchbtn.place(x=150, y=480)

    searchroot.mainloop()

########################################   END OF DEFINING SEARCHEMPLOYEE   #########################################

########################################  DEFINING DELETE EMPLOYEE   ################################################
def deleteemployee():
    cc = employeetable.focus()         #focus on the record which we click and gets data of that record
    content = employeetable.item(cc)
    pp = content['values'][0]          #it gives the id of the particular record to delete 
    strr = 'delete from employeedata1 where id=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from employeedata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        employeetable.insert('', END, values=vv)

#######################################  END OF DELETEEMPLOYEE   ####################################################

######################################   DEFINING UPDATEEMPLOYEE  ###################################################
def updateemployee():
    
    #<<<--------------- defining updatebutton in update entry form -------------->>>#
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        salary = salaryval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update employeedata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,salary=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr, (name, mobile, email, address, gender, salary, date, time, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
        strr = 'select *from employeedata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        employeetable.delete(*employeetable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            employeetable.insert('', END, values=vv)
    
    #<<<--------------- creating a window for updateentry form --------------->>>#
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Update Record')
    updateroot.config(bg='light blue')
    updateroot.resizable(False, False)
    
    #---------------------------------- Updateemployee Labels
    idlabel = Label(updateroot, text='Enter Id : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address: ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)  # DCAE96

    genderlabel = Label(updateroot, text='Enter Gender : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    salarylabel = Label(updateroot, text='Enter Salary : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    salarylabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', bg='#DCAE96', font=('verdana', 17, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    #-------------------- Updateemployee Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    salaryval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    #---------------------------updateemployee entry labels
    
    identry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    salaryentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=salaryval)
    salaryentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('arial', 12, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
    
    #------------------------- update button
    updatebtn = Button(updateroot, text="Update", bd=3, font=("Bodoni", 16, "bold"), width=10,command=update)
    updatebtn.config(relief="raised", bg="#f7e7ce", activebackground="sky blue")
    updatebtn.place(x=150, y=540)

    cc = employeetable.focus()      #this will get all details of existing record when clicked on it and fills in update entryform
    content = employeetable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        salaryval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

########################################  END OF DEFINING UPDATEEMPLOYEE  ###############################################

########################################  DEFINING SHOW ALL RECORDS    ##################################################
def showallrecords():
    strr = 'select *from employeedata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    employeetable.delete(*employeetable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        employeetable.insert('', END, values=vv)

########################################  END OF SHOWALLRECORDS  ########################################################

########################################  DEFINING EXITBUTTON    ########################################################
def exit_window():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()

########################################  END OF EXITBUTTON     ########################################################

##******************************************  DEFINING LOGINDATABASE  ************************************************##
def Connectdb():
    
    #--------------------> defining login button & making connection to database <-------------------#
    def submitdb():
        global con, mycursor
        host = "localhost"
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database employeemanagementsystem1'
            mycursor.execute(strr)
            strr = 'use employeemanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table employeedata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),salary varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table employeedata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table employeedata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',
                                'database created and now you are connected connected to the database ....',
                                parent=dbroot)

        except:
            strr = 'use employeemanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()
    
    #--------------------> creating window for login database button <-----------------------#
    messagebox.showinfo('Information..!','Please login with MySQL user id and password to create a database as localhost...!')
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("500x300+500+250")
    dbroot.resizable(False, False)
    dbroot.config(bg='light blue')
    dbroot.title("LogIn To Database")
    
    # ----------------------Connectdb Labels
    label1 = Label(dbroot, text="LogIn to database with MySQL credentials", bd=4, bg="lavender", fg="red",
                   relief=SOLID, font=("Courier", 14, "bold"))
    label1.pack(side="top", fill=BOTH)

    userlabel = Label(dbroot, text="MySQL Id :", font=("verdana", 12, "bold"),bg="lavender")
    userlabel.place(x=75, y=75)

    passwordlabel = Label(dbroot, text="MySQL Password :", font=("verdana", 12, "bold"),bg="lavender")
    passwordlabel.place(x=75, y=150)

    # -----------------------Connectdb Entry
    userval = StringVar()
    passwordval = StringVar()

    #------------------------Connectdb entrylabels
    userentry = Entry(dbroot, textvariable=userval, bd=4, bg="white", relief="raised", width=57)
    userentry.place(x=75, y=110)

    passwordentry = Entry(dbroot, textvariable=passwordval, bd=4, bg="white", relief="raised", width=57, show="*")
    passwordentry.place(x=75, y=185)

    # -----------------------login button & exit button
    login_button = Button(dbroot, text="LogIn", bd="4", bg="#DCAE96", relief="raised", font=("arial", 11, "bold"),
                          command=submitdb)
    login_button.config(activebackground="red", activeforeground="white")
    login_button.place(x=75, y=235)

    exit_button = Button(dbroot, text="Exit", bd="4", bg="#DCAE96", relief="raised", font=("arial", 11, "bold"),
                         command=dbroot.destroy)
    exit_button.config(activebackground="red", activeforeground="white")
    exit_button.place(x=165, y=235)

    dbroot.mainloop()

##****************************************** END OF LOGINDATABASE BUTTON  ************************************************##

##*****************************************  DEFINING TIME&DATE METHODS    ***********************************************##
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" + "Time : " + time_string)
    clock.after(200, tick)

##*****************************************  END OF TIME&DATE METHODS    ************************************************##

##############################################  IMPORTING & CREATING MAINWINDOW  ###############################################
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time

#---------------CREATING MAINWINDOW
root = Tk()
root.title("Employee Management System")
root.config(bg="light blue")
root.geometry("1100x700+200+50")
root.resizable(False, False)

####################################  CREATING TWO FRAMES IN MAIN WINDOW   ############################################

#--------------------------------------------------- CREATING & DEVELOPING DATA ENRTY FRAME 
DataEntryFrame = Frame(root, bg="#DCAE96", bd=1, relief="groove")
DataEntryFrame.place(x=20, y=80, width=500, height=600)

#--------------------data entry frame labels
frontlabel = Label(DataEntryFrame, text="Data Management Functions", relief="groove", bg="#f7e7ce", fg="navy blue",
                   font=("arial", 20, "bold"))
frontlabel.pack(side="top", fill=BOTH)

addbtn = Button(DataEntryFrame, text="Add Employee", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                width=20, command=addemployee)
addbtn.place(x=118, y=100)

updatebtn = Button(DataEntryFrame, text="Update Record", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                   width=20, command=updateemployee)
updatebtn.place(x=118, y=180)

searchbtn = Button(DataEntryFrame, text="Search Record", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                   width=20, command=searchemployee)
searchbtn.place(x=118, y=260)

delete_button = Button(DataEntryFrame, text="Delete Record", relief="raised", bg="light blue",
                       font=("verdana", 14, "bold"), width=20, command=deleteemployee)
delete_button.place(x=118, y=340)

showall_button = Button(DataEntryFrame, text="Show All Records", relief="raised", bg="light blue",
                        font=("verdana", 14, "bold"), width=20, command=showallrecords)
showall_button.place(x=118, y=420)

exit_button = Button(DataEntryFrame, text="Exit", relief="raised", bg="light blue", font=("verdana", 14, "bold"),
                     width=20, command=exit_window)
exit_button.place(x=118, y=500)

#--------------------------------------------------------------------END OF DATA ENTRY FRAME


#----------------------------------------------------CRAETING AND DEVELOPING SHOW DATA FRAME
ShowDataFrame = Frame(root, bg='Lavender', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=580, y=80, width=500, height=600)

#-------------------making a table in showdataframe to get tree view of data
#-------------------making/creating treeview
style = ttk.Style()
style.configure('Treeview.Heading', font=('verdana', 12, 'bold'), foreground='navy blue')
style.configure('Treeview', font=('Helvetica', 11, 'bold'), foreground='black', background='lavender')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
employeetable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Salary', 'Added Date', 'Added Time'),
                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=employeetable.xview)
scroll_y.config(command=employeetable.yview)
employeetable.heading('Id', text='Id')
employeetable.heading('Name', text='Name')
employeetable.heading('Mobile No', text='Mobile No')
employeetable.heading('Email', text='Email')
employeetable.heading('Address', text='Address')
employeetable.heading('Gender', text='Gender')
employeetable.heading('Salary', text='Salary')
employeetable.heading('Added Date', text='Added Date')
employeetable.heading('Added Time', text='Added Time')
employeetable['show'] = 'headings'
employeetable.column('Id', width=100)
employeetable.column('Name', width=200)
employeetable.column('Mobile No', width=200)
employeetable.column('Email', width=300)
employeetable.column('Address', width=200)
employeetable.column('Gender', width=100)
employeetable.column('Salary', width=150)
employeetable.column('Added Date', width=150)
employeetable.column('Added Time', width=150)
employeetable.pack(fill=BOTH, expand=1)

#----------------------------------------------------------------------END OF SHOW DATA FRAME

#############################################  END OF TWO FRAME DEVELOPMENTS  ###############################################

##################################### FOOTER / TOP SIDE OF MAIN WINDOW(ROOT)  ###############################################

#------------------------------------ MAIN LABEL/HEADING
main_label = Label(root, text="Employee Management System", relief="groove", bg="#FFFDD0", fg="navy blue",
                   font=("arial", 22, "bold"))
main_label.pack(side="top")

#------------------------------------ DATE&TIME
clock = Label(root, font=('verdana', 10, 'bold'), relief=RAISED, borderwidth=3, bg='Lavender', fg="black")
clock.place(x=930, y=5)
tick()
#------------------------------------ LOGIN DATABASE BUTTON
connectbutton = Button(root, text='LogIn Database', width=16, font=("verdana", 14, "bold"), command=Connectdb)
connectbutton.config(bg="#DCAE96", fg="black", activebackground="sky blue", activeforeground="black")
connectbutton.place(x=5, y=5)


root.mainloop()

#--------------------------------------------------->  END OF CODE <-----------------------------------------------------------#

#ALL CODE WAS EXPLAINED IN DETAIL IN THE REPORT 
#DONE BY:-
# K.Uma maheshwar Rao   rollno:-66
# G.Sai Rohith          rollno:-65
# M.Dheeraj             rollno:-59


# In[ ]:





# In[ ]:




