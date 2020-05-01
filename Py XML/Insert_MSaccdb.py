
import os
import datetime
import pyodbc


path_db = os.path.abspath("RBA ExchRatesHistory.accdb")

#obdc_connection = "r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path_db
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
cursor = conn.cursor()

cursor.execute('SELECT Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency] FROM [Rate History]')

for row in cursor.fetchall():
    print(row)

strMaxDate = "SELECT Max(CDate([Rate_Date])) FROM [Rate History];"
cursor.execute(strMaxDate)

# Retrieve last 'Max Date' from DB
for row in cursor.fetchall():
    accessMaxDate = str(row[0]).split(' ')[0]
    print(accessMaxDate)

now = datetime.datetime.now()
print(f'Now : "{now.year}"')
# Insert Date test here so Program doesn't proceed if accessMaxDate == Today


# INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency] )
# SELECT "1.12.2010" AS Expr1, "AUS" AS Expr2, 2 AS Expr3, "FOR" AS Expr4;

dateEntered = input("Provide a date in dd/mm/yyyy format please? ")
# Needs some error checking here...
print ('<'+dateEntered+'>')

strInput = "INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency]) "
strInput = strInput + " SELECT '" + dateEntered.strip() + "' AS Expr1, 'AUSs' AS Expr2, 2 AS Expr3, 'FOR' AS Expr4;"

print("strInput = ", strInput)
cursor.execute(strInput)

cursor.execute(strMaxDate)

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
