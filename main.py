from tkinter import *
from tkinter import ttk


class Student:
    def __init__(self, r):
        self.root = r
        self.root.title("Student Management System")
        self.root.geometry("1366x768+0+0")

        # --------- All Variables -----------
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="#d8e87f",
                      fg="#3fc10b")
        title.pack(side=TOP, fill=X)

        # Left Section of Student Management System Starts from here
        # --------- Manage Frame -----------
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#e1655d")
        Manage_Frame.place(x=20, y=100, width=450, height=590)

        m_title = Label(Manage_Frame, text="Manage Students", bg="#e1655d", fg="white",
                        font=("new times roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        # For Name
        lbl_Name = Label(Manage_Frame, text="Name", bg="#e1655d", fg="white", font=("new times roman", 20, "bold"))
        lbl_Name.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        txt_Name.focus()

        # For Roll_No.
        lbl_Roll = Label(Manage_Frame, text="Roll No.", bg="#e1655d", fg="white", font=("new times roman", 20, "bold"))
        lbl_Roll.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        txt_Roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # For Email
        lbl_Email = Label(Manage_Frame, text="E-mail", bg="#e1655d", fg="white", font=("new times roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # For Gender
        lbl_Gender = Label(Manage_Frame, text="Gender", bg="#e1655d", fg="white", font=("new times roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_Gender['values'] = ("Male", "Female", "Others")
        combo_Gender.grid(row=4, column=1, padx=20, pady=10)

        # For Contact
        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#e1655d", fg="white",
                            font=("new times roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # For D.O.B
        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="#e1655d", fg="white", font=("new times roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dob.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        # For Address
        lbl_Address = Label(Manage_Frame, text="Address", bg="#e1655d", fg="white",
                            font=("new times roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=30, height=4, font=("times new roman", 10, "bold"))
        self.txt_Address.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # ---------- Button Frame ----------
        Button_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="#e1655d")
        Button_Frame.place(x=10, y=520, width=430)

        # For Add Button
        add_Button = Button(Button_Frame, text="Add", width=10)
        add_Button.grid(row=0, column=0, padx=10, pady=10)

        # For Update Button
        update_Button = Button(Button_Frame, text="Update", width=10)
        update_Button.grid(row=0, column=1, padx=10, pady=10)

        # For Delete Button
        delete_Button = Button(Button_Frame, text="Delete", width=10)
        delete_Button.grid(row=0, column=2, padx=10, pady=10)

        # For Clear Button
        clear_Button = Button(Button_Frame, text="Clear", width=10)
        clear_Button.grid(row=0, column=3, padx=10, pady=10)

        # Left Section of Student Management System Ends here.....

        # Right Section of Student Management System Starts from here..
        # ---------- Detail Frame -----------
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#e1655d")
        Detail_Frame.place(x=510, y=100, width=810, height=590)

        lbl_search = Label(Detail_Frame, text="Search By", bg="#e1655d", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, font=("times new roman", 13, "italic"), state="readonly")
        combo_search['values'] = ("Roll No.", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame, width=20, font=("times new roman", 10, "bold"), bd=6, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        # For Search Button
        search_btn = Button(Detail_Frame, text="Search", width=10, pady=5)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        show_all_btn = Button(Detail_Frame, text="Show All", width=10, pady=5)
        show_all_btn.grid(row=0, column=4, padx=10, pady=10)

        # ---------- Table Frame ---------
        Tabel_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#e1655d")
        Tabel_Frame.place(x=10, y=70, width=780, height=500)

        scroll_x = Scrollbar(Tabel_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Tabel_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(Tabel_Frame,
                                          columns=("name", "roll", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("email", text="E-mail")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column('name', width=100)
        self.student_table.column('roll', width=100)
        self.student_table.column('email', width=100)
        self.student_table.column('gender', width=100)
        self.student_table.column('contact', width=100)
        self.student_table.column('dob', width=100)
        self.student_table.column('address', width=100)
        self.student_table.pack(fill=BOTH, expand=1)

        # Right Section of Student Management System End here....

root = Tk()
obj = Student(root)
root.mainloop()
