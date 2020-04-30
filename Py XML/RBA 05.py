import os
import pyodbc
import requests
from xml.etree import ElementTree as ET

class Error (Exception):
    pass

class BoundaryException(Error):
    pass

def line_no(no):
    local_no = no
    print(f'line no is {local_no}')
    local_no += 1
    return(local_no)

def main(file_text_as_string):
    myroot = ET.fromstring(file_text_as_string)

    dateEx =  myroot[2][3].text
    dateEx_l = dateEx.split('T')
    valC  = myroot[2][6][3][1][1].text
    baseC = myroot[2][6][3][2].text
    targetC = myroot[2][6][3][3].text

    # print (dateEx_l[0], baseC, valC, targetC )

    for i in range(2,40):
        try:
            # print (i, myroot[i].tag)
            dateEx = myroot[i][3].text
            dateEx_l = dateEx.split('T')  # List with Date and time
            valC = myroot[i][6][3][1][1].text  # Exchange rate
            baseC = myroot[i][6][3][2].text  # Our Country Abbreviation
            targetC = myroot[i][6][3][3].text  # Target Country Abbreviation

            print(f'On the {dateEx_l[0]}: $1 {baseC}  = {valC} {targetC}')

        except:
            print ('.', end='')



if __name__ == '__main__' :
    file_name = 'rss-cb-exchange-rates.xml'



    # url_file_name = 'https://www.rba.gov.au/rss/rss-cb-exchange-rates.xml'
    # page = requests.get(url_file_name)

    path_db = os.path.abspath("RBA ExchRatesHistory.accdb")
    print(path_db)

    obdc_connection = "r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + path_db
    ##print (obdc_connection)
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
    # ##conn = pyodbc.connect(obdc_connection)
    cursor = conn.cursor()
    cursor.execute('SELECT Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency] FROM [Rate History]')

    strInput = "INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency]) "
    strInput = strInput + " SELECT '1.12.2010' AS Expr1, 'AUS' AS Expr2, 2 AS Expr3, 'FOR' AS Expr4;"

    print("strInput = ", strInput)

# SELECT "1.12.2010" AS Expr1, "AUS" AS Expr2, 2 AS Expr3, "FOR" AS Expr4;"
#     cursor.execute('INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency])
# SELECT "1.12.2010" AS Expr1, "AUS" AS Expr2, 2 AS Expr3, "FOR" AS Expr4;)
    #
    for row in cursor.fetchall():
        print(row)

    # main(page.text)

# INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency] )
# SELECT "1.12.2010" AS Expr1, "AUS" AS Expr2, 2 AS Expr3, "FOR" AS Expr4;


  # else:
  #   print ('Doing nothing')
