import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\BiOSTAR\Documents\Database2.accdb;')
    print("Database is Connected")

except pyodbc.Error:
    print("Database is NOT connected")
