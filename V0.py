from tkinter import *
import datetime
from connection import *
from unicodedata import category

name = input("Enter your name : ")
total_amount=int(input("Enter totle amount : "))

class case_in:
    deposite_amount = int(input("Enter how many amount you want to deposite : "))
    date = datetime.datetime.now()
    description = input("Remark : ")
    # payment_mode = ["Case","Online","Paytm","Google Pay"]

class case_out:
    spent_amount = int(input("Enter how many amount you want to spent : "))
    date = datetime.datetime.now()
    description = input("Remark : ")
    # payment_mode = ["Case","Online","Paytm","Google Pay"]

In = case_in()
Out = case_out()




try:
    # insert query with autoincrement id
    con.execute('insert into data (name, time,description,payment_mode,deposite_amount,spent_amount,total_amount) values(?,?,?,?,?,?,?)',(name,time,description_,payment_mode_,deposite_amount_,spent_amount_,total_amount))

    print("Data inserted")

except:
    print("Data Not Inserted")




##################################### GUI #################################################
data = con.execute("select * from data")

def case_in():
    

    for row in data:
        Label(text=f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}", bg="black",fg="light blue").pack(anchor = "w",padx=40)

        # for i in list_:    # work of for loop is printing all list elements.
        #     Label(f2, text=f"({n}) {i}", bg="black",fg="light blue").pack(anchor = "w",padx=40)
        # n+=1 



root= Tk()  # starting GUI.
root.geometry("720x720")    # GUI window size.
root.title("Case Management System")   # window's title bar name.
root.minsize(720,720)   # minimum GUI window.

# # f1 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating horizontal frame.
# # f1.pack(side=TOP, fill="x")    # packing horizontal frame.

# # f2 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating Left vartical frame.
# # f2.pack(side=LEFT, fill="both",expand=True)    # packing Left vartical frame.

# # f3 = Frame(root, bg="black", borderwidth=6, relief=GROOVE)    # creating Right vartical frame.
# # f3.pack(side=RIGHT, fill="both",expand=True)    # packing right vartical frame.


Label(text="Wellcome", font=('Aerial 15'), bg="black", fg="dodger blue").pack(pady=10)    # creating a label in top frame.
b1=Button(text="case in", command= case_in,bg='sky blue').pack(padx=5, pady=5,ipadx=5)    # creating a button for select file and put in top frame, "command= select_file" is calling function.
root.mainloop() 



con.commit()    


    
    