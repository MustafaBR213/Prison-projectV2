from tkinter import *
from tkinter import ttk
from turtle import clear
from db import DataBase
from pages import Pages
from tkinter import messagebox
from tkinter import Toplevel, Button, Tk, Menu  
  
from visitings import Visiting #هي الملف التاني فيه دالة بس كبسنا على زر فيسيتنغ بينتقل عليه

db=DataBase("Persons.db")
pg=Pages()
#ساوينا القياس واحد 
pr=Tk()
pr.title('Prison')
pr.geometry('1310x515')
pr.resizable(False,False)
pr.configure(bg='#1f2e2e')##1f2e2e


firstName=StringVar()
father=StringVar()
lastName=StringVar()
gender=StringVar()
birthYear=StringVar()


# logo=PhotoImage(file='logo.png')
# lbl_logo=Label(pr,image=logo)
# lbl_logo.place(x=80,y=520)



#label frames قسم جزء منشان الازرار و الانبوت
entries_frame=Frame(pr,bg='#1f2e2e')
entries_frame.place(x=1,y=1,width=360,height=510)
title=Label(entries_frame,text='Prison BR',font=('Calibri',20,'bold'),bg='#1f2e2e',fg='white')
title.place(x=120,y=15)

# def hide():
#     pr.geometry("360x515+0+0")

# def show():
#     pr.geometry('1310x515+0+0')
#هدول كانوا لاخفاء الجدول و اظهارو

#هدول الزرار واحد بس شغال منشان التنقل بين الصفحات 


# btnhidee=Button(entries_frame,text='Visit',bg='white',bd=1,relief=SOLID,cursor='hand2',command=pg.VisitPage)
# btnhidee.place(x=160,y=10)

# btnhidee=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
# btnhidee.place(x=210,y=10)


# btnhide=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
# btnhide.place(x=260,y=10)
 
# btnshow=Button(entries_frame,text='Visiting',bg='white',bd=1,relief=SOLID,cursor='hand2',command=Visiting)
# btnshow.place(x=310,y=10)
#نهاية الزرار

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row 
    row=data["values"]
    firstName.set(row[1])
    father.set(row[2])
    lastName.set(row[3])
    gender.set(row[4])
    birthYear.set(row[5])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END,row[6])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def delete():
    db.remove(row[0])
    Clear()
    displayAll()

def Clear():
    firstName.set("")
    father.set("")
    lastName.set("")
    gender.set("")
    birthYear.set("")
    txtAddress.delete(1.0,END)

def add_Prisoner():
    if txtFName.get()=="" or txtLName.get()=="" or txtFather.get()=="" or txtBirth.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","Pleace Fill all the Entry")
        return 
    db.insert(
        txtFName.get(),
        txtFather.get(),
        txtLName.get(),
        comboGender.get(),
        txtBirth.get(),
        txtAddress.get(1.0,END))
    messagebox.showinfo("Success","Added new Prisoner")
    Clear()
    displayAll()
def Update():
    if txtFName.get()=="" or txtLName.get()=="" or txtFather.get()=="" or txtBirth.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error","Pleace Fill all the Entry")
        return 
    db.update(
        row[0],
        txtFName.get(),
        txtFather.get(),
        txtLName.get(),
        comboGender.get(),
        txtBirth.get(),
        txtAddress.get(1.0,END))
    messagebox.showinfo("Success","The Prisoner Data is Updated")
    Clear()
    displayAll()
def printIt():
    db.printToExcel()

menubar = Menu(pr)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
  
file.add_separator()  
  
file.add_command(label="Exit", command=pr.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="Visiting", command=pg.VisitPage)
help.add_command(label="Convicts", command=pg.ConvictsPage)
help.add_command(label="Offence", command=pg.OffencePage)
help.add_command(label="Dungeon", command=pg.DungeonPage)
help.add_command(label="DungeonMoves", command=pg.DungeonMovesPage)

menubar.add_cascade(label="Sections", menu=help)  
  
pr.config(menu=menubar)  

# btnhidee=Button(entries_frame,text='Export',bg='white',bd=1,relief=SOLID,cursor='hand2',command=printIt)
# btnhidee.place(x=110,y=10)
#عنوان الانبوات
lblFName=Label(entries_frame,text="FirstName",font=('Calibri',16),bg='#1f2e2e',fg='white')##1f2e2e
lblFName.place(x=10,y=80)
#الانبوت من نوع انتري يعني ادخال يدوي 😁
txtFName=Entry(entries_frame,textvariable=firstName,width=20,font=('Calibari',16))
txtFName.place(x=120,y=80)

lblFather=Label(entries_frame,text="Father",font=('Calibri',16),bg='#1f2e2e',fg='white')
lblFather.place(x=10,y=130)
txtFather=Entry(entries_frame,textvariable=father,width=20,font=('Calibari',16))
txtFather.place(x=120,y=130)


lblLName=Label(entries_frame,text="LastName",font=('Calibri',16),bg='#1f2e2e',fg='white')
lblLName.place(x=10,y=180)
txtLName=Entry(entries_frame,textvariable=lastName,width=20,font=('Calibari',16))
txtLName.place(x=120,y=180)

lblGender=Label(entries_frame,text="Gender",font=('Calibri',16),bg='#1f2e2e',fg='white')
lblGender.place(x=10,y=230)
comboGender=ttk.Combobox(entries_frame,textvariable=gender,state='readonly',width=20,font=('Calibri',16))
comboGender['values']=("Male","Female")
comboGender.place(x=120,y=230)

lblBirth=Label(entries_frame,text="BirthYear",font=('Calibri',16),bg='#1f2e2e',fg='white')
lblBirth.place(x=10,y=280)
txtBirth=Entry(entries_frame,textvariable=birthYear,width=20,font=('Calibari',16))
txtBirth.place(x=120,y=280)

lblAddress=Label(entries_frame,text="Address: ",font=('Calibri',16),bg='#1f2e2e',fg='white')
lblAddress.place(x=10,y=330)
txtAddress=Text(entries_frame,width=23,height=1,font=('Calibri',16))
txtAddress.place(x=120,y=330)

#buttons frame الازرار و تزبيط قياساتها 
btn_frame=Frame(entries_frame,bg='#1f2e2e',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)

btnAdd=Button(btn_frame,
              text='Insert Prisoner',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='#001a33',
              bd=0,
              command=add_Prisoner

              ).place(x=4,y=5)
btnEdit=Button(btn_frame,
              text='Update Prisoner',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='#001a33',
              bd=0,
              command=Update
              ).place(x=4,y=50)

btnDelete=Button(btn_frame,
              text='Delete Prisoner',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='#001a33',
              bd=0,
              command=delete
              ).place(x=170,y=5)
btnClear=Button(btn_frame,
              text='Clear Prisoners',
              width=14,
              height=1,
              font=('Calibri',16),
              fg='white',
              bg='#001a33',
              bd=0,
              command=Clear
              ).place(x=170,y=50)

# Table Frame عرض الجدول 

tree_frame=Frame(pr,bg='white')
tree_frame.place(x=365,y=1,width=940,height=510)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibari',13))

tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7),style="mystyle.Treeview" )
tv.heading("1",text="ID")
tv.column("1",width="60")

tv.heading("2",text="FirstName")
tv.column("2",width="140")

tv.heading("3",text="Father")
tv.column("3",width="140")

tv.heading("4",text="LastName")
tv.column("4",width="140")

tv.heading("5",text="Gender")
tv.column("5",width="120")

tv.heading("6",text="BarthYear")
tv.column("6",width="140")

tv.heading("7",text="Address")
tv.column("7",width="200")

tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=1,height=610,width=975)

displayAll()


pr.mainloop()