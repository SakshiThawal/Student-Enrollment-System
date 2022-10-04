from tkinter import*
from tkinter import ttk 
import tkinter.messagebox
import pymysql

class memberConnect :

    def __init__(self,root) :

        self.root = root
        blankSpace = " "
        self.root.title((202*blankSpace + "Student Management System"))
        self.root.resizable(width=False,height=False)
        self.root.geometry("1529x780+0+0")

        #===========================================================================================================

        AadharNo = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        MobNo = StringVar()
        Email = StringVar()
        Gender = StringVar()
        Percentage = StringVar()
        Stream = StringVar()
        Address = StringVar()
        Search = StringVar()        

        #======================================================EXIT==================================================

        def iexit() :

             ex = tkinter.messagebox.askyesno("Exit","Confirm if you want to exit")
             if ex > 0 :
                 root.destroy()
                 return

        #======================================================RESET==================================================
        
        def reset() :

            AadharNo.set("")
            FirstName.set("")
            LastName.set("")
            MobNo.set("")
            Email.set("")
            Gender.set("")
            Percentage.set("")
            Stream.set("")
            Address.set("")
            Search.set("")

        #==========================================================================================================

        mainFrame = Frame(self.root,bd=10,width=1529,height=780,relief=RIDGE,bg="PeachPuff")
        mainFrame.grid()

        titleFrames = Frame(mainFrame,bd=7,width=1529,height=100,relief=RIDGE)
        titleFrames.grid(row=0,column=0)

        titleFrame = Frame(titleFrames,bd=7,width=1510,height=100,relief=RIDGE,bg="PeachPuff")
        titleFrame.grid(row=0,column=0)

        searchFrame = Frame(mainFrame,bd=5,width=1500,height=50,relief=RIDGE)
        searchFrame.grid(row=1,column=0)

        midFrame = Frame(mainFrame,bd=5,width=1500,height=630,relief=RIDGE,bg="PeachPuff")
        midFrame.grid(row=3,column=0)

        innerFrame = Frame(midFrame,bd=5,width=1500,height=180,padx=24,pady=4,relief=RIDGE)
        innerFrame.grid(row=0,column=0)  

        buttonFrame = Frame(midFrame,bd=7,width=1500,height=50,relief=RIDGE,bg="PeachPuff")
        buttonFrame.grid(row=1,column=0)

        treeViewFrame = Frame(midFrame,bd=5,width=1500,height=358,padx=4,relief=RIDGE)
        treeViewFrame.grid(row=2,column=0,padx=5,pady=0)

        # For title of window
        self.lblTitle = Label(titleFrames,font=('arial',40,'bold'),bd=4,text="Student Enrollment System",bg="PeachPuff",fg="black")
        self.lblTitle.grid(row=0,column=0,padx=90) 
        
        # For Aadhar No. attribute lable and it's entry
        self.lblAadharNo = Label(innerFrame,font=('arial',12,'bold'),text="Aadhar No",bd=7)
        self.lblAadharNo.grid(row=0,column=0,padx=5,sticky=W)
        self.txtAadharNo = Entry(innerFrame,font=('arial',12,'bold'),bd=4,width=35,textvariable=AadharNo,justify='center')
        self.txtAadharNo.grid(row=0,column=1,padx=39) 

        # For FirstName attribute lable and it's entry
        self.lblFirstName = Label(innerFrame,font=('arial',12,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=1,column=0,padx=5,sticky=W)
        self.txtFirstName = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=FirstName,justify='center',bd=4)
        self.txtFirstName.grid(row=1,column=1,padx=39) 

        # For LastName attribute lable and it's entry
        self.lblSurname = Label(innerFrame,font=('arial',12,'bold'),text="Last Name",bd=7)
        self.lblSurname.grid(row=2,column=0,padx=5,sticky=W)
        self.txtSurname = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=LastName,justify='center',bd=4)
        self.txtSurname.grid(row=2,column=1,padx=39) 

        # For MobNo attribute lable and it's entry
        self.lblmobNo = Label(innerFrame,font=('arial',12,'bold'),text="Mobile No",bd=7)
        self.lblmobNo.grid(row=2,column=2,padx=5,sticky=W)
        self.txtmobNo = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=MobNo,justify='left',bd=4)
        self.txtmobNo.grid(row=2,column=3,padx=39)

        # For Email attribute lable and it's entry
        self.lblEmail = Label(innerFrame,font=('arial',12,'bold'),text="Email",bd=7)
        self.lblEmail.grid(row=1,column=2,padx=5,sticky=W)
        self.txtEmail = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=Email,justify='left',bd=4)
        self.txtEmail.grid(row=1,column=3,padx=39)

        # For Gender attribute lable and it's entry
        self.lblGender = Label(innerFrame,font=('arial',12,'bold'),text='Gender',bd=5)
        self.lblGender.grid(row=0,column=5,sticky=W,padx=5)
        self.cbogender = ttk.Combobox(innerFrame,width=35,font=('arail',12,'bold'),state='readonly',textvariable=Gender)
        self.cbogender['values'] = ('','Female','Male')
        self.cbogender.current(0)
        self.cbogender.grid(row=0,column=6)

        # For Percentage attribute lable and it's entry
        self.lblPercentage = Label(innerFrame,font=('arial',12,'bold'),text='Percentage',bd=5)
        self.lblPercentage.grid(row=2,column=5,sticky=W,padx=5)
        self.txtPercentage = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=Percentage,justify='left',bd=4)
        self.txtPercentage.grid(row=2,column=6)

        # For Stream attribute lable and it's entry
        self.lblStream = Label(innerFrame,font=('arial',12,'bold'),text='Stream',bd=5)
        self.lblStream.grid(row=1,column=5,sticky=W,padx=5)
        self.stream= ttk.Combobox(innerFrame,width=35,font=('arail',12,'bold'),state='readonly',textvariable=Stream)
        self.stream['values'] = ('','Science','Commerce','Arts')
        self.stream.current(0)
        self.stream.grid(row=1,column=6)

        # For Address attribute lable and it's entry
        self.lblAddress = Label(innerFrame,font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=0,column=2,padx=5,sticky=W)
        self.txtAddress = Entry(innerFrame,font=('arial',12,'bold'),width=35,textvariable=Address,justify='left',bd=4)
        self.txtAddress.grid(row=0,column=3,padx=39)

        #==========================================================================================================

        # Inserting new record in student database
        def addNew() :

            if AadharNo.get() == "" or FirstName.get()=="" or LastName.get()=="" :
                tkinter.messagebox.showerror("Error check input","Enter valid details")
            else :

                try :
                    sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001" ,database="Student_enrollment_system")
                    cur = sqlCon.cursor()
                    # MySQL query for inserting new record
                    cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        AadharNo.get(),
                        FirstName.get(),
                        LastName.get(),
                        MobNo.get(),
                        Email.get(),
                        Gender.get(),
                        Percentage.get(),
                        Stream.get(),
                        Address.get()
                    ))
                    sqlCon.commit()
                    show_records()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Data Entry from","Record succesfully inserted")

                except :
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Data Entry from","Record already present.")

        # Searching record in student database using aadhar number
        def searchDB() :

            try :

                sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
                cur = sqlCon.cursor()
                # MySQL query for searching record using Aadhar no.
                cur.execute("select * from student where aadharNo=%s"%Search.get()) 
                
                row = cur.fetchone()

                AadharNo.set(row[0])
                FirstName.set(row[1])
                LastName.set(row[2])
                MobNo.set(row[3])
                Email.set(row[4])
                Gender.set(row[5])
                Percentage.set(row[6])
                Stream.set(row[7])
                Address.set(row[8])

                sqlCon.commit()
            except :
                tkinter.messagebox.showinfo("Data Entry from","No such record found")
                Search.set("")

            sqlCon.close()            

        def show_records() :

            sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
            cur = sqlCon.cursor()
            cur.execute("select * from student")
            result = cur.fetchall()
            if len(result) != 0 :
                self.member_records.delete(*self.member_records.get_children())
                for row in result :
                    self.member_records.insert('',END,values=row)
                sqlCon.commit()
            sqlCon.close()

        def memberInfo() :

            viewInfo = self.member_records.focus()
            learnerdata = self.member_records.item(viewInfo)
            row = learnerdata['values']

            AadharNo.set(row[0])
            FirstName.set(row[1])
            LastName.set(row[2])
            MobNo.set(row[3])
            Email.set(row[4])
            Gender.set(row[5])
            Percentage.set(row[6])
            Stream.set(row[7])
            Address.set(row[8])

        def update() :

            sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
            cur = sqlCon.cursor()
            cur.execute("update student set FirstName=%s,LastName=%s,MobNo=%s,Email=%s,Gender=%s,Percentage=%s,Stream=%s,Address=%s where AadharNo = %s",
            (
                FirstName.get(),
                LastName.get(),
                MobNo.get(),
                Email.get(),
                Gender.get(),
                Percentage.get(),
                Stream.get(),
                Address.get(),
                AadharNo.get()
            ))  

            if  AadharNo.get() == "":
                tkinter.messagebox.showerror("Error check input","Enter valid details")
            else :
                tkinter.messagebox.showinfo("Data Entry from","Record Succesfully updated")

            sqlCon.commit()
            show_records()
            sqlCon.close()            

        def deleteDB() :

            sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
            cur = sqlCon.cursor()

            cur.execute("delete from student where aadharNo = %s",AadharNo.get())
            sqlCon.commit()
            sqlCon.close()         
            tkinter.messagebox.showinfo("Data Entry from","Record Succesfully deleted")
            show_records()
            reset() 


        # #===========================================================================================================

        self.txtSearch = Entry(searchFrame,font=('arial',13,'bold'),width=154,textvariable=Search,justify='center')
        self.txtSearch.grid(row=0,column=0)
        self.btSearch = Button(searchFrame,pady=1,bd=4,font=('arial',12,'bold'),text="Search",width=10,height=1,bg="PeachPuff",command=searchDB).grid(row=0,column=3,padx=1)

        self.btAdd = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Add",width=20,height=1,bg="PeachPuff",command=addNew).grid(row=0,column=0,padx=2)
        self.btRecords = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Show Records",width=20,height=1,bg="PeachPuff",command=show_records).grid(row=0,column=1,padx=2)
        self.btUpdate = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Update",width=20,height=1,bg="PeachPuff",command=update).grid(row=0,column=2,padx=2)
        self.btDelete = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Delete",width=20,height=1,bg="PeachPuff",command=deleteDB).grid(row=0,column=3,padx=2)
        self.btReset = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Reset",width=20,height=1,bg="PeachPuff",command=reset).grid(row=0,column=4,padx=2)
        self.btExit = Button(buttonFrame,pady=1,fg='black',bd=4,font=('arial',12,'bold'),text="Exit",width=20,height=1,bg="PeachPuff",command=iexit).grid(row=0,column=5,padx=2)

        scroll_y = Scrollbar(treeViewFrame,orient=VERTICAL)
        self.member_records = ttk.Treeview(treeViewFrame,height=12,columns=("aadharNo","firstName","lastName","mobNo","email","gender","percentage","stream","address"),yscrollcommand = scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.member_records.heading("aadharNo",text="Aadhar No")
        self.member_records.heading("firstName",text="First name")
        self.member_records.heading("lastName",text="Surname")
        self.member_records.heading("mobNo",text="Mobile No")
        self.member_records.heading("email",text="Email")
        self.member_records.heading("gender",text="Gender")
        self.member_records.heading("percentage",text="Percentage")
        self.member_records.heading("stream",text="Stream")
        self.member_records.heading("address",text="Address")

        self.member_records['show'] = 'headings'

        self.member_records.column('aadharNo',width=150)
        self.member_records.column('firstName',width=150)
        self.member_records.column('lastName',width=150)
        self.member_records.column('mobNo',width=160)
        self.member_records.column('email',width=200)
        self.member_records.column('gender',width=150)
        self.member_records.column('percentage',width=150)
        self.member_records.column('stream',width=150)
        self.member_records.column('address',width=200)

        self.member_records.pack(fill=BOTH,expand=1)
        self.member_records.bind("<ButtonRelease - 1>",memberInfo)
        show_records()

class Login() :

    def __init__(self,root) :
    
        self.root = root
        self.root.title("Login and Registration System")
        self.root.resizable(width=False,height=False)
        self.root.geometry("1529x780+0+0")
        self.loginform()

    def loginform(self) :

        LoginFrame = Frame(self.root,bg="lightgray")
        LoginFrame.place(x=0,y=0,width=1529,height=780)

        InputFrame = Frame(self.root,bg="white")
        InputFrame.place(x=400,y=200,height=450,width=400)

        self.lblLogin = Label(InputFrame,font=('impact',45,'bold'),text='Login Here',fg="black",bg="white")
        self.lblLogin.place(x=75,y=20)

        self.lblLoginUser = Label(InputFrame,font=('impact',20,'bold'),text='Username',fg="black",bg="white")
        self.lblLoginUser.place(x=30,y=95)
        self.txtLoginUser = Entry(InputFrame,font=('impact',15),justify='left',bg='lightgray')
        self.txtLoginUser.place(x=30,y=145,height=35,width=270)

        self.lblLoginPass = Label(InputFrame,font=('impact',20,'bold'),text='Password',fg="black",bg="white")
        self.lblLoginPass.place(x=30,y=195)
        self.txtLoginPass = Entry(InputFrame,font=('impact',15),justify='left',bg='lightgray')
        self.txtLoginPass.place(x=30,y=245,width=270,height=35)

        self.btnlogin = Button(InputFrame,font=('arial',10),text="Login",bd=0,command=self.login,bg='gray',cursor='hand2',width=15,height=1)
        self.btnlogin.place(x=200,y=290)

        self.btnreg = Button(InputFrame,font=('arial',10),text="Not Registered? Register",bd=0,command=self.register,cursor='hand2',bg='white',fg='black')
        self.btnreg.place(x=20,y=290)

    def login(self) :

        if(self.txtLoginPass.get() == "" or self.txtLoginUser.get() == "") :
            tkinter.messagebox.showerror("Error","All fields are required")
        else :
            try :
                sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
                cur = sqlCon.cursor()
                cur.execute('select * from register where Username=%s and Password=%s',(self.txtLoginUser.get(),self.txtLoginPass.get()))
                row = cur.fetchone()

                if row == None:
                    tkinter.messagebox.showerror("Error","Invalid Username or Password")
                    self.loginClear()
                    self.txtLoginUser.focus()
                else :
                    memberConnect(root)
                    sqlCon.close() 
            except Exception as es :
                tkinter.messagebox.showerror("Error",f'Error due to : {str(es)}',parent=self.root)

    def register(self) :

        LoginFrame1 = Frame(self.root,bg="white")
        LoginFrame1.place(x=0,y=0,width=1529,height=780)

        InputFrame2 = Frame(self.root,bg="white")
        InputFrame2.place(x=320,y=130,height=450,width=650)

        self.lblRegister = Label(InputFrame2,text="Register Here",bg="White",font=('impact',45,'bold'))
        self.lblRegister.place(x=45,y=20)

        self.lblUser = Label(InputFrame2,font=('impact',15),text='Username',fg="black",bg="white")
        self.lblUser.place(x=10,y=95)
        self.txtUser = Entry(InputFrame2,font=('arial',15),width=30,justify='left')
        self.txtUser.place(x=150,y=95)

        self.lblPass = Label(InputFrame2,font=('impact',15),text='Password',fg="black",bg="white")
        self.lblPass.place(x=10,y=150)
        self.txtPass = Entry(InputFrame2,font=('arial',15),width=30,justify='left')
        self.txtPass.place(x=150,y=150)

        self.lblEmail = Label(InputFrame2,font=('impact',15),text='Email ID',fg="black",bg="white")
        self.lblEmail.place(x=10,y=205)
        self.txtEmail = Entry(InputFrame2,font=('arial',15),width=30,justify='left',bd=1)
        self.txtEmail.place(x=150,y=205)

        self.lblConPass = Label(InputFrame2,font=('impact',15),text='Confirm Password',fg="black",bg="white")
        self.lblConPass.place(x=10,y=260)
        self.txtConPass = Entry(InputFrame2,font=('arial',15),width=30,justify='left')
        self.txtConPass.place(x=200,y=260)

        self.btnregister = Button(InputFrame2,command=self.registered,bd=0,text="Register",cursor='hand2',font=('impact',15),fg='black',bg='white',width=15,height=1)
        self.btnregister.place(x=100,y=350)

        self.btn = Button(InputFrame2,text="Already Register? Login",bd=0,cursor='hand2',command=self.loginform,font=('impact',15),fg='black',bg='white',width=25,height=1)
        self.btn.place(x=300,y=350)

    def registered(self) :

        if (self.txtUser.get()=="" or self.txtPass.get()=="" or self.txtEmail.get()=="" or self.txtConPass.get()=="") :
            tkinter.messagebox.showerror("Error","All fields are required")
        elif(self.txtPass.get() != self.txtConPass.get()) :
            tkinter.messagebox.showerror("Error","Password are not same")
        else :
            try :
                sqlCon = pymysql.connect(host="localhost",user="root",passwd="Sakshi$2001",database="Student_enrollment_system")
                cur = sqlCon.cursor()
                cur.execute('select * from register where Username=%s',self.txtUser.get())

                row = cur.fetchone()

                if row != None:
                    tkinter.messagebox.showerror("Error","User already exist. Please try with another username.")
                    self.regClear()
                    self.txtUser.focus()
                else :
                    cur.execute('insert into register values(%s,%s, %s, %s)',(self.txtUser.get(),self.txtPass.get(),self.txtEmail.get(),self.txtConPass.get()))
                    sqlCon.commit()
                    tkinter.messagebox.showinfo("Success","Register Successful")
                    self.regClear()
                    sqlCon.close()
            except Exception as es :
                tkinter.messagebox.showerror("Error",f'Error due to : {str(es)}',parent=self.root)  

    def regClear(self) :

        self.txtUser.delete(0,END)
        self.txtEmail.delete(0,END)
        self.txtPass.delete(0,END)
        self.txtConPass.delete(0,END)

    def loginClear(self) :

        self.txtLoginUser.delete(0,END)
        self.txtLoginPass.delete(0,END)


if __name__ == '__main__' :
    root = Tk()
    Login(root)
    root.mainloop()