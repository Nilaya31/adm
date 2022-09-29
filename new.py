from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
import sqlite3

headlabelfont = ("BankGothic Md BT", 15, 'bold')
labelfont = ('Century Gothic', 12)
entryfont = ('Century Gothic', 12)

connector = sqlite3.connect('Studentdetails.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS STUDENT_DETAILS (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, PARENT_NAME TEXT , AADHAR_NO TEXT , PHONE_NO TEXT , CLASS TEXT , SECTION TEXT, FEE TEXT )"
)

def reset_fields():
   global name_strvar, pname_strvar, studentid_strvar, aadhar_strvar, phoneno_strvar, Class_strvar, section_strvar,fee_strvar
   for i in ['name_strvar', 'pname_strvar', 'studentid_strvar', 'aadhar_strvar', 'phoneno_strvar', 'Class_strvar', 'section_strvar','fee_strvar']:
    exec(f'{i}.set(\'\')')

def reset_form():
   global tree
   tree.delete(*tree.get_children())
   reset_fields()

def display_records():
   tree.delete(*tree.get_children())
   curr = connector.execute('SELECT * FROM STUDENT_DETAILS')
   data = curr.fetchall()
   for records in data:
    tree.insert('', END, values=records)

def add_record():
   global name_strvar, pname_strvar, studentid_strvar, aadhar_strvar, phoneno_strvar, Class_strvar, section_strvar,fee_strvar
   name = name_strvar.get()
   parentname = pname_strvar.get()
   studentid = studentid_strvar.get()
   aadhar = aadhar_strvar.get()
   phoneno = phoneno_strvar.get()
   Class = Class_strvar.get()
   section = section_strvar.get()
   fee = fee_strvar.get()
   if not name or not parentname or not studentid or not aadhar or not phoneno or not Class or not section or not fee :
       mb.showerror('Error!', "Please fill all the missing fields!!")
   else:
       try:
           connector.execute(
           'INSERT INTO STUDENT_DETAILS (NAME, PARENT_NAME, STUDENT_ID, AADHAR_NO, PHONE_NO, CLASS, SECTION, FEE) VALUES (?,?,?,?,?,?,?,?)', (name, parentname, studentid, aadhar, phoneno, Class,  section, fee)
           )
           connector.commit()
           mb.showinfo('Record added', f"Record of {name} was successfully added")
           reset_fields()
           display_records()
       except:
           mb.showerror('Wrong type', 'The type of the values entered is not accurate.')

def remove_record():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       connector.execute('DELETE FROM STUDENT_DETAILS WHERE STUDENT_ID=%d' % selection[0])
       connector.commit()
       mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
       display_records()

def view_record():
   global name_strvar, pname_strvar, studentid_strvar, aadhar_strvar, phoneno_strvar, Class_strvar, section_strvar, fee_strvar
   if not tree.selection():
       mb.showerror('Error!', 'Please select a record to view')
   else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        name_strvar.set(selection[1]);pname_strvar.set(selection[2])
        studentid_strvar.set(selection[3]); aadhar_strvar.set(selection[4])
        phoneno_strvar.set(selection[5]); Class_strvar.set(selection[6])
        section_strvar.set(selection[7]);fee_strvar.set(selection[8])



main = Tk()
main.title('DataFlair Student Details')
main.geometry('1000x600')
main.resizable(0, 0)

lf_bg = 'thistle'
cf_bg = 'lavender'

name_strvar = StringVar()
pname_strvar = StringVar()
studentid_strvar = StringVar()
aadhar_strvar  = StringVar()
phoneno_strvar  = StringVar()
Class_strvar = StringVar()
section_strvar = StringVar()
fee_strvar = StringVar()


Label(main, text="SCHOOL DATABASE", font=headlabelfont, bg='lightsteelblue').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
right_frame = Frame(main, bg="Gray")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.36, rely=0.01)
Label(left_frame, text="Parent Name", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.10)
Label(left_frame, text="Student ID", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.20)
Label(left_frame, text="Aadhar No", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.29)
Label(left_frame, text="Phone No", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.39)
Label(left_frame, text="Class", font=labelfont, bg=lf_bg).place(relx=0.35, rely=0.49)
Label(left_frame, text="Section", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.58)
Label(left_frame, text="Fee", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.67)

Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=12, rely=0.048)
Entry(left_frame, width=19, textvariable=pname_strvar, font=entryfont).place(x=12, rely=0.14)
Entry(left_frame, width=19, textvariable=studentid_strvar, font=entryfont).place(x=12, rely=0.24)
Entry(left_frame, width=19, textvariable=aadhar_strvar, font=entryfont).place(x=12, rely=0.33)
Entry(left_frame, width=19, textvariable=phoneno_strvar, font=entryfont).place(x=12, rely=0.43)
Entry(left_frame, width=19, textvariable=Class_strvar, font=entryfont).place(x=12, rely=0.53)
Entry(left_frame, width=19, textvariable=section_strvar, font=entryfont).place(x=12, rely=0.62)
Entry(left_frame, width=19, textvariable=fee_strvar, font=entryfont).place(x=12, rely=0.71)
Button(left_frame, text='Submit', font=labelfont, command=add_record, width=18).place(relx=0.025, rely=0.85)

Button(center_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.1, rely=0.25)
Button(center_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.1, rely=0.35)
Button(center_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.1, rely=0.45)
Button(center_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.1, rely=0.55)

Label(right_frame, text='Students Details', font=headlabelfont, bg='slategrey', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=("Student ID","Name","Parent Name","Aadhar No","Phone No","Class","Section","Fee"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Parent Name', text='Parent Name', anchor=CENTER)
tree.heading('Aadhar No', text='Aadhar No', anchor=CENTER)
tree.heading('Phone No', text='Phone No', anchor=CENTER)
tree.heading('Class', text='Class', anchor=CENTER)
tree.heading('Section', text='Section', anchor=CENTER)
tree.heading('Fee', text='Fee', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=80, stretch=NO)
tree.column('#3', width=90, stretch=NO)
tree.column('#4', width=100, stretch=NO)
tree.column('#5', width=100, stretch=NO)
tree.column('#6', width=60, stretch=NO)
tree.column('#7', width=90, stretch=NO)
tree.column('#8', width=60, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()

main.update()
main.mainloop()