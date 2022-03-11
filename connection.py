# import sqlite3 database
import sqlite3

# handel the exception in try and except block
try:
    # create a database with name of mymovie
    con = sqlite3.connect("data.db")
    print("Database is Created")  # message show
    con.commit()  # commit all task
except:  # except block
    print("Error is occurred")  # message show
