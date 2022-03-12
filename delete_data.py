# import connection file
from connection import *

try:  # handle the exception
    # create a table query with replace

    con.execute('DELETE FROM data')

    print("Table data removed")  # message show

except:
    print("Table data Not removed")  # Error message show

con.commit()  # commit the table
