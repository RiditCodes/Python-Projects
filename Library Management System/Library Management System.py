import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.daysoverdue_var = StringVar()
        self.actualprice_var = StringVar()

        Lbltitle = Label(self.root, text = "Library Management System",
        bg = "powder blue", fg = "yellow" ,bd = 20,
        relief = RIDGE, font = ("Times New Roman", 40, "bold"))
        Lbltitle.pack(side = TOP, fill = X)

        frame = Frame(self.root, bg = "powder blue", bd = 12, relief = RIDGE)
        frame.place(x = 0, y = 104, width = 1365, height = 390)

        DataFrameLeft = LabelFrame(frame, text = "Library Membership Information", bg = "powder blue", fg = "yellow", bd = 10, relief = RIDGE, font = ("Times New Roman", 15, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 680, height = 360)

        LblMember = Label(DataFrameLeft, text = "Member Type", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblMember.grid(row = 0, column = 0)

        ComMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var,font = ("Times New Roman", 15, "bold"))
        ComMember["value"] = ("Admin Staff", "Students", "Teachers/Professors", "Other")
        ComMember.grid(row = 0, column = 1)

        LblPRN_NO = Label(DataFrameLeft, text = "PRN No.", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblPRN_NO.grid(row = 1, column = 0)
        txtPRN_NO = Entry(DataFrameLeft, textvariable=self.prn_var,font = ("Times New Roman", 15, "bold"))
        txtPRN_NO.grid(row = 1, column = 1)

        Lbltitle2 = Label(DataFrameLeft, text = "ID No.", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        Lbltitle2.grid(row = 2, column = 0)
        txtTitle = Entry(DataFrameLeft, textvariable=self.id_var,font = ("Times New Roman", 15, "bold"))
        txtTitle.grid(row = 2, column = 1)

        LblFirstName = Label(DataFrameLeft, text = "First Name: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblFirstName.grid(row = 3, column = 0)
        txtFirstName = Entry(DataFrameLeft, textvariable=self.firstname_var,font = ("Times New Roman", 15, "bold"))
        txtFirstName.grid(row = 3, column = 1)

        LblLastName = Label(DataFrameLeft, text = "Last Name: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblLastName.grid(row = 4, column = 0)
        txtLastName = Entry(DataFrameLeft, textvariable=self.lastname_var,font = ("Times New Roman", 15, "bold"))
        txtLastName.grid(row = 4, column = 1)

        LblAddress1 = Label(DataFrameLeft, text = "Address 1: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblAddress1.grid(row = 5, column = 0)
        txtAddress1 = Entry(DataFrameLeft, textvariable=self.address1_var,font = ("Times New Roman", 15, "bold"))
        txtAddress1.grid(row = 5, column = 1)

        LblAddress2 = Label(DataFrameLeft, text = "Address 2: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblAddress2.grid(row = 6, column = 0)
        txtAddress2 = Entry(DataFrameLeft, textvariable=self.address2_var,font = ("Times New Roman", 15, "bold"))
        txtAddress2.grid(row = 6, column = 1)

        LblPostCode = Label(DataFrameLeft, text = "Postal Code: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblPostCode.grid(row = 7, column = 0)
        txtPostCode = Entry(DataFrameLeft, textvariable=self.postcode_var,font = ("Times New Roman", 15, "bold"))
        txtPostCode.grid(row = 7, column = 1)

        LblMobile = Label(DataFrameLeft, text = "Mobile No.: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblMobile.grid(row = 8, column = 0)
        txtMobile = Entry(DataFrameLeft, textvariable=self.mobile_var,font = ("Times New Roman", 15, "bold"))
        txtMobile.grid(row = 8, column = 1)

        LblBookID = Label(DataFrameLeft, text = "Book ID: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblBookID.grid(row = 9, column = 0)
        txtBookID = Entry(DataFrameLeft, textvariable=self.bookid_var,font = ("Times New Roman", 15, "bold"))
        txtBookID.grid(row = 9, column = 1)

        LblBookTitle = Label(DataFrameLeft, text = "Book Title: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblBookTitle.grid(row = 10, column = 0)
        txtBookTitle = Entry(DataFrameLeft, textvariable=self.booktitle_var,font = ("Times New Roman", 15, "bold"))
        txtBookTitle.grid(row = 10, column = 1)

        LblAuthor = Label(DataFrameLeft,text = "Author: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblAuthor.grid(row = 0, column = 2)
        txtAuthor = Entry(DataFrameLeft, textvariable=self.author_var,font = ("Times New Roman", 15, "bold"))
        txtAuthor.grid(row = 0, column = 3)

        LblDateBorrowed = Label(DataFrameLeft, text = "Taken on: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblDateBorrowed.grid(row = 1, column = 2)
        txtDateBorrowed = Entry(DataFrameLeft, textvariable=self.dateborrowed_var,font = ("Times New Roman", 15, "bold"))
        txtDateBorrowed.grid(row = 1, column = 3)

        LblDue = Label(DataFrameLeft, text = "Due On: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblDue.grid(row = 2, column = 2)
        txtDue = Entry(DataFrameLeft, textvariable=self.datedue_var,font = ("Times New Roman", 15, "bold"))
        txtDue.grid(row = 2, column = 3)

        LblDays = Label(DataFrameLeft, text = "For days: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblDays.grid(row = 3, column = 2)
        txtDays = Entry(DataFrameLeft, textvariable=self.daysonbook_var,font = ("Times New Roman", 15, "bold"))
        txtDays.grid(row = 3, column = 3)

        Lbllatereturn = Label(DataFrameLeft, text = "Late fine: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        Lbllatereturn.grid(row = 4, column = 2)
        txtlatereturn = Entry(DataFrameLeft, textvariable=self.latereturnfine_var,font = ("Times New Roman", 15, "bold"))
        txtlatereturn.grid(row = 4, column = 3)

        LblDaysoverdue = Label(DataFrameLeft, text = "Over due: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblDaysoverdue.grid(row = 5, column = 2)
        txtDaysoverdue = Entry(DataFrameLeft, textvariable=self.daysoverdue_var,font = ("Times New Roman", 15, "bold"))
        txtDaysoverdue.grid(row = 5, column = 3)

        LblActualPrice = Label(DataFrameLeft, text = "Price: ", bg = "powder blue", font = ("Times New Roman", 15, "bold"))
        LblActualPrice.grid(row = 6, column = 2)
        txtActualPrice = Entry(DataFrameLeft, textvariable=self.actualprice_var,font = ("Times New Roman", 15, "bold"))
        txtActualPrice.grid(row = 6, column = 3)

        DataFrameRight = LabelFrame(frame, text = "Book Details", bg = "powder blue", fg = "yellow", bd = 10, relief = RIDGE, font = ("Times New Roman", 15, "bold"))
        DataFrameRight.place(x = 680, y = 5, width = 660, height = 360)

        self.txtBox  = Text(DataFrameRight, font = ("Times New Roman", 15, "bold"), width = 20, height = 14)
        self.txtBox.grid(row = 0, column = 2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row = 0, column = 1, stick = "ns")

        listBooks = ["Python Crash Course", "Geronimo Stilton",
         "Fun micro:bit project ideas", "Head-first Python",
         "BBC microbit introduction"]

        def SelectBook(event = ""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Python Crash Course":
                self.bookid_var.set("P1111")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("Paul Pyger")
                Date1 = datetime.datetime.today()
                Date2 = datetime.timedelta(days = 15)
                Date3 = Date1 + Date2
                self.dateborrowed_var.set(Date1)
                self.datedue_var.set(Date3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs. 50")
                self.daysoverdue_var.set("No")
                self.actualprice_var.set("Rs. 500")

            elif x == "Geronimo Stilton":
                self.bookid_var.set("G1111")
                self.booktitle_var.set("Geronimo Stilton")
                self.author_var.set("Geronimo Stilton")
                Date1 = datetime.datetime.today()
                Date2 = datetime.timedelta(days = 15)
                Date3 = Date1 + Date2
                self.dateborrowed_var.set(Date1)
                self.datedue_var.set(Date3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs. 100")
                self.daysoverdue_var.set("No")
                self.actualprice_var.set("Rs. 1000")

            elif x == "Fun micro:bit project ideas":
                self.bookid_var.set("F1111")
                self.booktitle_var.set("Fun micro:bit project ideas")
                self.author_var.set("Kirti Chaurasia")
                Date1 = datetime.datetime.today()
                Date2 = datetime.timedelta(days = 15)
                Date3 = Date1 + Date2
                self.dateborrowed_var.set(Date1)
                self.datedue_var.set(Date3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs. 100")
                self.daysoverdue_var.set("No")
                self.actualprice_var.set("Rs. 500")

            
            elif x == "Head-first Python":
                self.bookid_var.set("H1111")
                self.booktitle_var.set("Head-first Python")
                self.author_var.set("Santosh Chaudhari")
                Date1 = datetime.datetime.today()
                Date2 = datetime.timedelta(days = 15)
                Date3 = Date1 + Date2
                self.dateborrowed_var.set(Date1)
                self.datedue_var.set(Date3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs. 150")
                self.daysoverdue_var.set("No")
                self.actualprice_var.set("Rs. 1000")

            elif x == "BBC microbit introduction":
                self.bookid_var.set("B1111")
                self.booktitle_var.set("BBC microbit introduction")
                self.author_var.set("Joe Ranger")
                Date1 = datetime.datetime.today()
                Date2 = datetime.timedelta(days = 15)
                Date3 = Date1 + Date2
                self.dateborrowed_var.set(Date1)
                self.datedue_var.set(Date3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs. 200")
                self.daysoverdue_var.set("No")
                self.actualprice_var.set("Rs. 1500")


        listBox = Listbox(DataFrameRight, font = ("Times New Roman", 15, "bold"), width = 15, height = 15)
        listBox.grid(row = 0, column = 0)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listScrollbar.config(command = listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)

        Framebutton =   Frame(self.root, bg = "powder blue", bd = 12, relief = RIDGE)
        Framebutton.place(x = 0, y = 500, width = 1360, height = 200)

        btnAddData = Button(Framebutton,command = self.AddData, text = "Add Data")
        btnAddData.grid(row = 0, column = 0)

        btnShowData = Button(Framebutton,command = self.FetchData, text = "Show Data")
        btnShowData.grid(row = 0, column = 1)

        btnUpdateData = Button(Framebutton, command = self.UpdateData,text = "Update Data")
        btnUpdateData.grid(row = 0, column = 2)

        btnDeleteData = Button(Framebutton, command = self.DeleteData,text = "Delete Data")
        btnDeleteData.grid(row = 0, column = 3)

        btnResetText = Button(Framebutton,command = self.ResetText ,text = "Reset Text")
        btnResetText.grid(row = 0, column = 4)

        btnExit = Button(Framebutton,command = self.Exit ,text = "Exit")
        btnExit.grid(row = 0, column = 5)

        FrameDetails = Frame(self.root, bg = "powder blue", bd = 12, relief = RIDGE)
        FrameDetails.place(x = 0, y = 580, width = 1020, height = 120)

        Table_Frame = Frame(FrameDetails, bg = "powder blue", bd = 12, relief = RIDGE)
        Table_Frame.place(x = 3, y = 2, width = 990, height = 92)

        xscroll = ttk.Scrollbar(Table_Frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_Frame, orient = VERTICAL)

        self.library_table = ttk.Treeview(Table_Frame, column = ("Member Type",
        "PRN No.", "ID No.", "First Name", "Last Name", "Address1",
        "Address 2", "Post Code", "Mobile No.", "Book ID", "Book Title",
        "Author", "Date Borrowed", "Date Due", "Days on Book",
        "Late Return Fine", "Days over due", "Actual Price"),
        xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

        xscroll.pack(side = BOTTOM, fill = X)
        yscroll.pack(side = RIGHT, fill = Y)

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)

        self.library_table.heading("Member Type", text = "Member Type")
        self.library_table.heading("PRN No.", text = "PRN No.")
        self.library_table.heading("ID No.", text = "ID No.")
        self.library_table.heading("First Name", text = "First Name")
        self.library_table.heading("Last Name", text = "Last Name")
        self.library_table.heading("Address1", text = "Address 1")
        self.library_table.heading("Address 2", text = "Address 2")
        self.library_table.heading("Post Code", text = "Post Code")
        self.library_table.heading("Mobile No.", text = "Mobile No.")
        self.library_table.heading("Book ID", text = "Book ID")
        self.library_table.heading("Book Title", text = "Book Title")
        self.library_table.heading("Author", text = "Author")
        self.library_table.heading("Date Borrowed", text = "Date Borrowed")
        self.library_table.heading("Date Due", text = "Date Due")
        self.library_table.heading("Days on Book", text = "Days On Book")
        self.library_table.heading("Late Return Fine", text = "Late Return Fine")
        self.library_table.heading("Days over due", text = "Days Over Due")
        self.library_table.heading("Actual Price", text = " Actual Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand = 1)

        def get_row(events=""):
            row_num = self.library_table.focus()
            row = self.library_table.item(row_num)
            column = row["values"]

            self.member_var.set(column[0]) 
            self.prn_var.set(column[1]) 
            self.id_var.set(column[2]) 
            self.firstname_var.set(column[3])
            self.lastname_var.set(column[4]) 
            self.address1_var.set(column[5]) 
            self.address2_var.set(column[6]) 
            self.postcode_var.set(column[7])
            self.mobile_var.set(column[8]) 
            self.bookid_var.set(column[9]) 
            self.booktitle_var.set(column[10]) 
            self.author_var.set(column[11])
            self.dateborrowed_var.set(column[12]) 
            self.datedue_var.set(column[13]) 
            self.daysonbook_var.set(column[14])
            self.latereturnfine_var.set(column[15]) 
            self.daysoverdue_var.set(column[16]) 
            self.actualprice_var.set(column[17])
        
        self.library_table.bind("<ButtonRelease>", get_row) 

    def AddData(self):
        con = mysql.connector.connect(host = "localhost", username = "root", password = "Eluck509@509", database = "librarydata")
        cursor_add = con.cursor()
        cursor_add.execute("INSERT INTO information VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
            (self.member_var.get(), self.prn_var.get(), self.id_var.get(), self.firstname_var.get(),
            self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
            self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(),
            self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook_var.get(),
            self.latereturnfine_var.get(), self.daysoverdue_var.get(), self.actualprice_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Library Managment System", "Data has been successfully added")

    def FetchData(self):

        for record in self.library_table.get_children():
            self.library_table.delete(record)
            
        con = mysql.connector.connect(host = "localhost", username = "root", password = "Eluck509@509", database = "librarydata")
        cursor_fetch = con.cursor()
        cursor_fetch.execute("SELECT * FROM information")
        rows = cursor_fetch.fetchall()
        con.commit()
        con.close()
        if len(rows) != 0:
            for i in rows:
                self.library_table.insert("",END,values = i)

    def UpdateData(self):
        con = mysql.connector.connect(host = "localhost", username = "root", password = "Eluck509@509", database = "librarydata")
        cursor_update = con.cursor()
        cursor_update.execute("UPDATE information SET Member=%s, ID_No=%s, First_Name=%s, Last_Name=%s, Address1=%s, Address2=%s, Postal_Code=%s, Mobile_No=%s, Book_ID=%s, Book_Title=%s, Author=%s, Date_Borrowed=%s, Due_On=%s, Borrowed_For=%s, Late_Return_Fine=%s, Days_Overdue=%s, Actual_Price=%s where PRN_No=%s", 
            (self.member_var.get(), self.id_var.get(), self.firstname_var.get(),
            self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(),
            self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(),
            self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook_var.get(),
            self.latereturnfine_var.get(), self.daysoverdue_var.get(), self.actualprice_var.get(),
            self.prn_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Library Managment System", "Data has been successfully updated")
    
    def DeleteData(self):
        con = mysql.connector.connect(host = "localhost", username = "root", password = "Eluck509@509", database = "librarydata")
        cursor_delete = con.cursor()
        query = "DELETE FROM information WHERE PRN_No=%s"
        value = (self.prn_var.get(),)
        cursor_delete.execute(query, value)
        con.commit()
        con.close()
        messagebox.showinfo("Library Managment System", "Data has been successfully deleted")

    def ResetText(self):
            self.member_var.set("") 
            self.prn_var.set("") 
            self.id_var.set("") 
            self.firstname_var.set("")
            self.lastname_var.set("") 
            self.address1_var.set("") 
            self.address2_var.set("") 
            self.postcode_var.set("")
            self.mobile_var.set("") 
            self.bookid_var.set("") 
            self.booktitle_var.set("") 
            self.author_var.set("")
            self.dateborrowed_var.set("") 
            self.datedue_var.set("") 
            self.daysonbook_var.set("")
            self.latereturnfine_var.set("") 
            self.daysoverdue_var.set("") 
            self.actualprice_var.set("")

    def Exit(self):
        answer = messagebox.askyesno("Library Management System", "Do you really want to exit?")
        if answer > 0:
            exit()
        else:
            pass

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagement(root)
    root.mainloop()