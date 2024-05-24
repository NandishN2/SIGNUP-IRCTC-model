from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
new2=Tk()
new2.title('Welcome to IRCTC')
l1=Label(new2,text="INDIAN RAILWAYS",bg='orange',fg='white',font=('calibri',14),width=30,height=2)
l1.pack()
l2=Label(new2,text="Welcome to IRCTC",bg='orange',fg='white',font=('calibri',13),width=32,height=1)
l2.place(x=620,y=70)
l3=Label(new2,text="Sign up",font=('calibri',14),width=20)
l3.place(x=660,y=105)
d='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_'
l1=list(d)
m=StringVar()
v=StringVar()
u=StringVar()
def signup():
    flag=0
    a = v.get()
    b = u.get()
    c = m.get()
    l = list(c)
    file = open("user.text", "w")
    file.writelines( str(c))
    file.writelines("\n"+str(b))
    file.close()
    l=list(c)
    for i in range(len(l)):
        if l[i] not in l1:
            flag=1
    if (flag==1):
        messagebox.showinfo('warning', 'only alphabets,numbers and underscores are allowed in username')
    elif(a==''or b==''or c==''):
        messagebox.showinfo('empty spaces', 'empty spaces are not allowed')
    elif (a==b):
        messagebox.showinfo('signup successfull','signup is successful')
    else:
        messagebox.showwarning('caution','please re-enter the password correctly to confirm ')

l4=Label(new2,text="UserName :",font=('calibri',11))
l4.place(x=660,y=150)
E1=Entry(new2,bg='blue',fg='white',width=20,textvariable=m)
E1.place(x=740,y=150)
l5=Label(new2,text="Password :",font=('calibri',11))
l5.place(x=660,y=190)
B1=Button(new2,text="SIGN UP",bg='orange',fg='white',bd=2,width=32,command=signup)
B1.place(x=650,y=300)
E2=Entry(new2,bg='blue',fg='white',width=20,textvariable=v,show='*')
E2.place(x=740,y=190)
l6=Label(new2,text="Confirm\npassword :",font=('calibri',11))
l6.place(x=660,y=212)
E3=Entry(new2,bg='blue',fg='white',width=20,textvariable=u,show='*')
E3.place(x=740,y=230)
l7=Label(new2,text='Already have an account ?')
l7.place(x=650,y=330)
B2=Button(new2,text="Sign in",fg='Blue',bd=0)
B2.place(x=800,y=330)
i1=PhotoImage(file="C:/Users/nandi/OneDrive/Desktop/images.png")
l8=Label(new2,image=i1)
l8.place(x=615,y=370)

i2=Image.open("C:/Users/nandi/OneDrive/Desktop/777497-200.png")
i3=Image.open("C:/Users/nandi/OneDrive/Desktop/show-password-icon-18.jpg")
r1=i2.resize((20,20))
r2=i3.resize((20,20))
N1=ImageTk.PhotoImage(r1)
N2=ImageTk.PhotoImage(r2)
def show():
    hide_button=Button(new2,image=N1,bd=0,relief=FLAT,command=hide)
    hide_button.place(x=880,y=190)
    E2.config(show='')
def hide():
    B3 = Button(new2, image=N2, bd=0, relief=FLAT, command=show)
    B3.place(x=880, y=190)
    E2.config(show='*')

B3=Button(new2,image=N2,bd=0,relief=FLAT,command=show)
B3.place(x=880,y=190)
def show1():
    hide_button1=Button(new2,image=N1,bd=0,relief=FLAT,command=hide1)
    hide_button1.place(x=880,y=230)
    E3.config(show='')
def hide1():
    B4 = Button(new2, image=N2, bd=0, relief=FLAT, command=show1)
    B4.place(x=880, y=230)
    E3.config(show='*')


B4=Button(new2,image=N2,bd=0,relief=FLAT,command=show1)
B4.place(x=880,y=230)

new2.mainloop()