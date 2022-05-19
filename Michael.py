import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\BiOSTAR\Documents\Database2.accdb;')
    print("Database is Connected")

    database = connection.cursor()
    mydata = (

        (10, "Michael S. Colcol", 19, "BSCPE", "Cavite", 99),

    )

    database.executemany('INSERT INTO Table1 VALUES (?,?,?,?,?,?)', mydata)
    connection.commit()
    # print(x)
    print("Data is inserted")

except pyodbc.Error:
    print("Database is NOT inserted")