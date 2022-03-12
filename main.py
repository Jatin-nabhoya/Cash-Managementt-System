from cProfile import label
from connection import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ---------------------------------------------------------------Login Function --------------------------------------
def clear():
    userentry.delete(0, END)
    passentry.delete(0, END)


def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror(
            "Error", "Enter User Name And Password", parent=win)
    else:
        try:
            con = sqlite3.connect("data.db")
            cur = con.cursor()

            # cur.execute(f"select * from user where username={user_name.get()} and password = {password.get()}")#,(user_name.get(),password.get()))
            cur.execute("select * from user where username=? and password=?",
                        (user_name.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Invalid User Name And Password", parent=win)

            else:
                messagebox.showinfo(
                    "Success", "Successfully Login", parent=win)
                close()
                deshbord()
            con.close()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error Dui to : {str(es)}", parent=win)

# ---------------------------------------------------------------End Login Function ---------------------------------

# #---------------------------------------------------- DeshBoard Panel -----------------------------------------
# ======================================================================================================================


def deshbord():
    def cash_in():
        def switch():
            root.destroy()

        def action():
            if deposite_amount.get() == "" or description.get() == "" or payment_mode.get() == "":
                messagebox.showerror(
                    "Error", "All Fields Are Required", parent=cash_in)
            else:

                try:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    row = cur.fetchone()
                    cur.execute("insert into data(deposite_amount ,description ,payment_mode)values (:deposite_amount, :description, :payment_mode)",
                                {
                                    "deposite_amount": deposite_amount.get(),
                                    "description": description.get(),
                                    "payment_mode": payment_mode.get()
                                })
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Data Inserted", parent=cash_in)
                    clear()
                    switch()

                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error Dui to : {str(es)}", parent=cash_in)

            # close signup function
        def switch():
            cash_in.destroy()

        # clear data function
        def clear():
            deposite_amount.delete(0, END)
            description.delete(0, END)
            payment_mode.delete(0, END)

            # start Signup Window
        for row in data:
            label(f2,text=f"{row[0]}, {row[1]}, {row[2]},{row[3]} ,{row[4]},{row[5]},{row[6]},{row[7]}",fg="light blue").pack(anchor="w",padx=40)
        cash_in = Tk()
        cash_in.title("Case")
        cash_in.maxsize(width=500,  height=600)
        cash_in.minsize(width=500,  height=600)

        # heading label
        heading = Label(cash_in, text="Cash In", font='Verdana 15 bold')
        heading.place(x=80, y=60)

        # form data label
        deposite_amount = Label(
            cash_in, text="Amount :", font='Verdana 10 bold')
        deposite_amount.place(x=80, y=130)

        description = Label(cash_in, text="description :",
                            font='Verdana 10 bold')
        description.place(x=80, y=160)

        payment_mode = Label(cash_in, text="payment_mode:",
                             font='Verdana 10 bold')
        payment_mode.place(x=80, y=190)

        # payment = StringVar()
        # payment.set("Select any Payment_mode")

        # drop = OptionMenu(cash_out , payment, "cash","online" ,"paytm","google pay")
        # drop.pack()
        # Entry Box ------------------------------------------------------------------

        deposite_amount = IntVar()
        description = StringVar()
        payment_mode = StringVar()

        deposite_amount = Entry(
            cash_in, width=40, textvariable=deposite_amount)
        deposite_amount.place(x=200, y=133)

        description = Entry(cash_in, width=40, textvariable=description)
        description.place(x=200, y=163)

        payment_mode = Entry(cash_in, width=40, textvariable=payment_mode)
        payment_mode.place(x=200, y=193)
        # payment = tk.StringVar(cash_out)
        # payment.set("Select any Payment_mode")
        # drop = OptionMenu(cash_out , payment, "cash","online" ,"paytm","google pay")
        # drop.pack()

        # button login and clear

        btn_signup = Button(cash_in, text="save",
                            font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=413)

        btn_login = Button(cash_in, text="clear",
                           font='Verdana 10 bold', command=clear)
        btn_login.place(x=280, y=413)

        sign_up_btn = Button(cash_in, text="leave ", command=switch)
        sign_up_btn.place(x=350, y=20)

        cash_in.mainloop()


# ----------------------------------------   Case out   -----------------------------------------------------------------------------

    def cash_out():
        def switch():
            root.destroy()

        def action():
            if spent_amount.get() == "" or description.get() == "" or payment_mode.get() == "":
                messagebox.showerror(
                    "Error", "All Fields Are Required", parent=cash_out)
            else:

                try:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    row = cur.fetchone()
                    cur.execute("insert into data(spent_amount ,description ,payment_mode)values (:spent_amount, :description, :payment_mode)",
                                {
                                    "spent_amount": spent_amount.get(),
                                    "description": description.get(),
                                    "payment_mode": payment_mode.get()
                                })
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Data inserted", parent=case_out)
                    clear()
                    switch()

                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error Dui to : {str(es)}", parent=case_out)

            # close signup function
        def switch():
            case_out.destroy()

            # clear data function
        def clear():
            spent_amount.delete(0, END)
            description.delete(0, END)
            payment_mode.delete(0, END)

            # start Signup Window
        case_out = Tk()
        case_out.title("Case")
        case_out.maxsize(width=500,  height=600)
        case_out.minsize(width=500,  height=600)

        # heading label
        heading = Label(case_out, text="Cash Out", font='Verdana 15 bold')
        heading.place(x=80, y=60)

        # form data label
        spent_amount = Label(case_out, text="Spent Amount :",
                             font='Verdana 10 bold')
        spent_amount.place(x=80, y=130)

        description = Label(case_out, text="description :",
                            font='Verdana 10 bold')
        description.place(x=80, y=160)

        payment_mode = Label(case_out, text="payment_mode:",
                             font='Verdana 10 bold')
        payment_mode.place(x=80, y=190)

        # Entry Box ------------------------------------------------------------------

        spent_amount = IntVar(case_out, value='0')
        description = StringVar()
        payment_mode = StringVar()

        spent_amount = Entry(case_out, width=40, textvariable=spent_amount)
        spent_amount.place(x=200, y=133)

        description = Entry(case_out, width=40, textvariable=description)
        description.place(x=200, y=163)

        # payment_mode = Entry(case_out, width=40 , textvariable = payment_mode)
        # payment_mode.place(x=200 , y=193)

        payment_mode = Entry(case_out, width=40, textvariable=payment_mode)
        payment_mode.place(x=200, y=193)
        

        # button login and clear

        btn_signup = Button(case_out, text="save",
                            font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=413)

        btn_login = Button(case_out, text="clear",
                           font='Verdana 10 bold', command=clear)
        btn_login.place(x=280, y=413)

        sign_up_btn = Button(case_out, text="leave ", command=switch)
        sign_up_btn.place(x=350, y=20)

        case_out.mainloop()


# --------------------------------------  index page --------------------------------------------------------------------------------

    root = Tk()  # starting GUI.
    root.geometry("720x720")    # GUI window size.
    root.title("Cash Management System")   # window's title bar name.
    root.minsize(720, 720)   # minimum GUI window.
    data = con.execute("select * from data")
    # creating horizontal frame.
    f1 = Frame(root, borderwidth=6, relief=GROOVE)
    f1.pack(side=TOP, fill="x")    # packing horizontal frame.
    # creating Left vartical frame.
    f2 = Frame(root, borderwidth=6, relief=GROOVE)
    f2.pack(fill="both", expand=True)    # packing Left vartical frame.
     # packing right vartical frame.
    # # creating a label in top frame.
    
    # for row in data:
    #     label(f2,text=f"{row[0]}, {row[1]}, {row[2]},{row[3]} ,{row[4]},{row[5]},{row[6]},{row[7]}",fg="light blue").pack(anchor="w",padx=40)
    Label(f1, text="Welcome", font=('Aerial 15'),fg="dodger blue").pack(pady=10)
    # creating a button for select file and put in top frame, "command= select_file" is calling function.
    b1 = Button(f1, text="Cash In", command=cash_in,bg='sky blue').pack(padx=5, pady=5, ipadx=5)
    # creating a button for select file and put in top frame, "command= select_file" is calling function.
    b2 = Button(f1, text="Cash Out", command=cash_out,bg='sky blue').pack(padx=5, pady=5, ipadx=5)
    root.mainloop()  # ending GUI


################################################################## Cash in ############################################################


# ======================================================================================================================

# #-----------------------------------------------------End Deshboard Panel -------------------------------------
# ----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
    # signup database connect
    def action():
        if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = sqlite3.connect("data.db")
                cur = con.cursor()

                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "User Name Already Exits", parent=winsignup)
                else:
                    
                    cur.execute("insert into user values (:first_name, :last_name, :age,:city,:address,:username,:password)",
                                {
                                    "first_name": first_name.get(),
                                    "last_name": last_name.get(),
                                    "age": age.get(),
                                    # "var":var.get(),
                                    "city": city.get(),
                                    "address": add.get(),
                                    "username": user_name.get(),
                                    "password": password.get()
                                })
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Ragistration Successfull", parent=winsignup)
                    clear()
                    switch()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def clear():
        first_name.delete(0, END)
        last_name.delete(0, END)
        age.delete(0, END)
        # var.set("Male")
        city.delete(0, END)
        add.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window

    winsignup = Tk()
    winsignup.title("Case")
    winsignup.maxsize(width=500,  height=600)
    winsignup.minsize(width=500,  height=600)

    # heading label
    heading = Label(winsignup, text="Signup", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name = Label(winsignup, text="First Name :", font='Verdana 10 bold')
    first_name.place(x=80, y=130)

    last_name = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
    last_name.place(x=80, y=160)

    age = Label(winsignup, text="Age :", font='Verdana 10 bold')
    age.place(x=80, y=190)

    # Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
    # Gender.place(x=80,y=220)

    city = Label(winsignup, text="City :", font='Verdana 10 bold')
    city.place(x=80, y=260)

    add = Label(winsignup, text="Address :", font='Verdana 10 bold')
    add.place(x=80, y=290)

    user_name = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name.place(x=80, y=320)

    password = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password.place(x=80, y=350)

    very_pass = Label(winsignup, text="Verify Password:",
                      font='Verdana 10 bold')
    very_pass.place(x=80, y=380)

    # Entry Box ------------------------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    age = IntVar(winsignup, value='0')
    # var= StringVar()
    city = StringVar()
    add = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=40, textvariable=first_name)
    first_name.place(x=200, y=133)

    last_name = Entry(winsignup, width=40, textvariable=last_name)
    last_name.place(x=200, y=163)

    age = Entry(winsignup, width=40, textvariable=age)
    age.place(x=200, y=193)

    # Radio_button_male = ttk.Radiobutton(winsignup,text='Male', value="Male", variable = var).place(x= 200 , y= 220)
    # Radio_button_female = ttk.Radiobutton(winsignup,text='Female', value="Female", variable = var).place(x= 200 , y= 238)

    city = Entry(winsignup, width=40, textvariable=city)
    city.place(x=200, y=263)

    add = Entry(winsignup, width=40, textvariable=add)
    add.place(x=200, y=293)

    user_name = Entry(winsignup, width=40, textvariable=user_name)
    user_name.place(x=200, y=323)

    password = Entry(winsignup, width=40, textvariable=password)
    password.place(x=200, y=353)

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=200, y=383)

    # button login and clear

    btn_signup = Button(winsignup, text="Signup",
                        font='Verdana 10 bold', command=action)
    btn_signup.place(x=200, y=413)

    btn_login = Button(winsignup, text="Clear",
                       font='Verdana 10 bold', command=clear)
    btn_login.place(x=280, y=413)

    sign_up_btn = Button(winsignup, text="Switch To Login", command=switch)
    sign_up_btn.place(x=350, y=20)
    

    winsignup.mainloop()
# ---------------------------------------------------------------------------End Singup Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------
win = Tk()

# app title
win.title("Cash Management System")

# window size
win.maxsize(width=500,  height=500)
win.minsize(width=500,  height=500)


# heading label
heading = Label(win, text="Login", font='Verdana 25 bold')
heading.place(x=80, y=150)

username = Label(win, text="User Name :", font='Verdana 10 bold')
username.place(x=80, y=220)

userpass = Label(win, text="Password :", font='Verdana 10 bold')
userpass.place(x=80, y=260)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=40, textvariable=user_name)
userentry.focus()
userentry.place(x=200, y=223)

passentry = Entry(win, width=40, show="*", textvariable=password)
passentry.place(x=200, y=260)


# button login and clear

btn_login = Button(win, text="Login", font='Verdana 10 bold', command=login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text="Clear", font='Verdana 10 bold', command=clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win, text="Switch To Sign up", command=signup)
sign_up_btn.place(x=350, y=20)


win.mainloop()

# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
