# import connection file

import V0
from connection import *


obj = V0.case_in()

total_amount_ = V0.total_amount
name_ = V0.name

time_ = obj.date
description_ = obj.description
# payment_mode_ = obj.payment_mode
payment_mode_ = "Case"
deposite_amount_ = obj.deposite_amount
total_amount_ = total_amount_ + deposite_amount_
spent_amount_ = 50
total_amount_ = total_amount_ - spent_amount_


try:
    # insert query with autoincrement id
    con.execute('insert into data (name, time,description,payment_mode,deposite_amount,spent_amount,total_amount) values(?,?,?,?,?,?,?)',(name_,time_,description_,payment_mode_,deposite_amount_,spent_amount_,total_amount_))

    print("Data inserted")

except:
    print("Data Not Inserted")

# commit the query
con.commit()



