

from tkinter import *
import sqlite3
root = Tk()
root.title("Library Book Management System")
root.geometry("920x450")


import tkinter.ttk as ttk
## defining functions
# i need to create CRUD 
# lets create a database first


## Adding the login credentials 

# mydb = input("Enter the Database Name (library.db): ")
mydb = "library.db"



def Database():
    global cursor,conn
    conn = sqlite3.connect(mydb)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (Book_name TEXT,Author TEXT,Year INT ,ISBN INT PRIMARY KEY) ")
    

# Created the database

def add(): 
    Database()
    conn = sqlite3.connect(mydb)
    cursor = conn.cursor()
    if title_var.get() =="" or author_var.get()=="" or isbn_var.get() ==""or year_var.get() =="":
        label_status.config(text = "Please fill all the fields",fg = "red")
    else:
        msg = "added the book "+title_var.get()+ ", please click Display to see the changes"
        label_status.config(text = msg,fg = "green")
        cursor.execute("INSERT INTO books(Book_name ,Author ,Year,ISBN) VALUES (?,?,?,?)",(str(title_var.get()),str(author_var.get()),str(year_var.get()),str(isbn_var.get()))) 
        title_var.set("")
        author_var.set("")
        isbn_var.set("")
        year_var.set("")
        conn.commit()
        conn.close()

  
    

def display():
    book_rack.delete(*book_rack.get_children())
    Database()
    cursor.execute("SELECT * FROM books order by Book_name asc")
    rows=cursor.fetchall()
    for i in rows:
        book_rack.insert('','end',values=(i[0],i[1],i[2],i[3]))
    conn.commit()
    conn.close()
    
def exit():
    root.destroy()
    
def delete():
    # book_rack.delete(*book_rack.get_children())
    Database()
    cursor.execute("DELETE FROM books WHERE ISBN= ?",(isbn_var.get() ,))
    conn.commit()
    conn.close()
    msg = "Use ISBN no to Delete a book from the record"
    label_status.config(text = msg,fg = "red")
    title_var.set("")
    author_var.set("")
    isbn_var.set("")
    year_var.set("")   
  

def SearchData():
    Database()
    cursor.execute("SELECT * FROM books where Book_name = ? OR Author=? OR Year=? OR ISBN=?",(str(title_var.get()),str(author_var.get()),str(year_var.get()),str(isbn_var.get())))
    rows=cursor.fetchall()
    title_var.set("")
    author_var.set("")
    isbn_var.set("")
    year_var.set("")
    for i in rows:
        book_rack.insert('','end',values=(i[0],i[1],i[2],i[3]))
    conn.commit()
    conn.close()
        


def issue():
    label_status.config(text = "use isbn no to delete a record ")


# lets create the top frame along with the label
frm1 = Frame(root ,width = 900 ,height = 50 ,relief = "groove",bd = 5,padx=15)
frm1.grid(column=0,row = 0,columnspan = 2)

gap =Frame(root ,width = 900 ,height = 10 )
gap.grid(column=0,row = 1,columnspan = 2)

left_frm2 = Frame(root ,width = 350 ,height = 300 ,padx=5,relief = "groove",bd = 2)
left_frm2.grid(row = 2,column=0)


right_frm2 = Frame(root ,width = 500 ,height = 320,relief = "groove",bd = 5
                   ,padx=5)
right_frm2.grid(row = 2,column=1 , rowspan= 2)

button_frm = Frame(root ,width = 390 ,height = 100 ,relief = "groove",bd = 0)
button_frm.grid(row = 3 ,column=0 )



# Lets create the label Library book management system

label_heading = Label(frm1,text = "Library Book Management System",
                      font = ('Raleway',19 ), padx = 15,pady = 15 ,justify=CENTER
                      ).grid(row = 0, column = 0)
label_title = Label(left_frm2 ,text  = "name of the title "
                     ,pady = 15,font = ('Raleway',12 ),justify=LEFT
                     )
label_title.grid(row = 0,column = 0)

label_author = Label(left_frm2 ,text  = "name of the author "
                     ,pady = 15,font = ('Raleway',12 ),justify=LEFT
                     )
label_author.grid(row = 1,column = 0)



label_year = Label(left_frm2 ,text  = "Year"
                     ,pady = 15,font = ('Raleway',12 ),justify=LEFT
                     )
label_year.grid(row = 2,column = 0)
label_isbn = Label(left_frm2 ,text  = "ISBN no. "
                     ,pady = 15,font = ('Raleway',12 ),justify=LEFT
                     )
label_isbn.grid(row = 3,column = 0)


label_status = Label(root,text = "you can search and delete a record by just isbn no",relief="groove",bd = -5)
label_status.grid(row = 5 ,column = 0,columnspan=2,pady=15)


# lets create the entries

title_var = StringVar()
author_var = StringVar()
year_var = StringVar()
isbn_var = StringVar()


ent_title = Entry(left_frm2 ,textvariable=title_var ,width = 30
                  )
ent_title.grid(row= 0,column = 1)

ent_author = Entry(left_frm2 ,textvariable=author_var ,width = 30
                   )
ent_author.grid(row= 1,column = 1)

ent_year = Entry(left_frm2 ,textvariable=year_var ,width = 30
                 )
ent_year.grid(row= 2,column = 1)

ent_isbn = Entry(left_frm2 ,textvariable=isbn_var ,width = 30
                 )
ent_isbn.grid(row= 3,column = 1)


## Lets use the button_frm to insert buttons 390x 100
button_add = Button(button_frm ,width  = 7 ,command = add ,padx = 15,relief= "ridge"
                    ,text  = "Add",bd = 3).grid(row = 0 ,column = 0,padx = 10 ,pady  = 10)

button_delete = Button(button_frm ,width  = 7 ,command = delete,padx = 15,relief= "ridge"
                    ,text = "Delete",bd = 3).grid(row = 1 ,column = 0,padx = 10 ,pady  = 10)

button_display = Button(button_frm ,width  = 7 ,command = display,padx = 15,relief= "ridge"
                    ,text  = "Display",bd = 3).grid(row = 0 ,column = 1,padx = 10 ,pady  = 10)

button_issue = Button(button_frm ,width  = 7 ,command = issue,padx = 15,relief= "ridge",bg = "cyan"
                    ,text = "help",bd = 3).grid(row = 1 ,column = 1,padx = 10 ,pady  = 10)

button_search = Button(button_frm ,width  = 7 ,command = SearchData,padx = 15,relief= "ridge"
                    ,text  = "Search",bd = 3).grid(row = 0 ,column = 2,padx = 10 ,pady  = 10)

button_exit = Button(button_frm ,width  = 7 ,command = exit,padx = 15,relief= "ridge"
                    ,text  = "Exit",bd = 3).grid(row = 1 ,column = 2,padx = 10 ,pady  = 10)


## Lets show the data on the right frame
book_rack = ttk.Treeview(right_frm2,height= 14)
book_rack["column"] = ("Book_name","Author","Year","ISBN")
book_rack.column('#0',width=0,stretch=NO)
book_rack.column("Book_name",anchor = CENTER ,width = 125)
book_rack.column("Author",anchor = CENTER ,width = 125)
book_rack.column("Year",anchor = CENTER ,width = 125)
book_rack.column("ISBN",anchor = CENTER ,width = 125)


book_rack.heading('#0',text="",anchor=CENTER)
book_rack.heading('Book_name',text="Book_name",anchor=CENTER)
book_rack.heading('Author',text="Author",anchor=CENTER)
book_rack.heading('Year',text="Year",anchor=CENTER)
book_rack.heading('ISBN',text="ISBM(Unique)",anchor=CENTER)

book_rack.pack()


# #############################################################################
# #lets add some books to the records (Uncomment)

Database()
cursor.execute("INSERT INTO books values('Believe-What Life and Cricket Taught Me','Suresh Raina',1586,1224)")
cursor.execute("INSERT INTO books values('The Christmas Pig','JK Rowling',2015,1124)")
cursor.execute("INSERT INTO books values('The India Story','Bimal Jalal',2015,1225)")
cursor.execute("INSERT INTO books values('Business of Sports: The Winning Formula for Success','Vinit Karnik',2016,1226)")
cursor.execute("INSERT INTO books values('A Place Called Home','Preeti Shenoy',2017,1227)")
cursor.execute("INSERT INTO books values('Modi @20: Dreams Meeting Delivery','VP Venkaiah Naidu',2023,1229)")
cursor.execute("INSERT INTO books values('The Struggle for Police Reforms in India','Ex-IPS Prakash Singh',2021,1228)")
cursor.execute("INSERT INTO books values('INDO-PAK WAR 1971- Reminiscences of Air Warriors','Rajnath Singh',2020,1230)")
cursor.execute("INSERT INTO books values('Leaders, Politicians, Citizens','Rasheed Kidwai ',2001,1220)")
conn.commit()
conn.close()

# #############################################################################


root.mainloop()
