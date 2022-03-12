from tkinter import *
from connection import *



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


Label(text="Wellcome", font=('Aerial 15'), bg="black", fg="dodger blue").pack(pady=10)    # creating a label in top frame.
b1=Button(text="case in", command= case_in,bg='sky blue').pack(padx=5, pady=5,ipadx=5)    # creating a button for select file and put in top frame, "command= select_file" is calling function.
root.mainloop() 



con.commit()

