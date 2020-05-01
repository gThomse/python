import os
import pyodbc
import requests
import datetime
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
            strUpdate = "INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency]) "
            strUpdate = strUpdate + " SELECT '" + dateEx_l[0] + "' AS Expr1, " + baseC
            strUpdate = " AS Expr2, " + valC + " AS Expr3, " + targetC + " AS Expr4;"

            # Writing to local DB
            cursor.execute(strUpdate)
            conn.commit()
        except:
            print ('.', end='')



if __name__ == '__main__' :

    # Look for the database first before proceeding
    try:
        # Return absolute path for file :
        path_db = os.path.abspath("RBA ExchRatesHistory.accdb")
        print(path_db)

        # Set up Access Connection:
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
        cursor = conn.cursor()
        # Check date isn't today
        strMaxDate = "SELECT Max(CDate([Rate_Date])) FROM [Rate History];"
        cursor.execute(strMaxDate)

        # Retrieve last 'Max Date' from DB
        for row in cursor.fetchall():
            accessMaxDate = str(row[0]).split(' ')[0]
            print(accessMaxDate)
            print('In for look to retrieve data..')

        l_date = str(datetime.datetime.now()).split(' ')[0]

        if l_date > accessMaxDate:
            try:
                print ('Dates ok')
                # New date so new data should be available...
                # Then look for the RBA rate XML file...
                # file_name = 'rss-cb-exchange-rates.xml'  # This line used when testing was local. .. :)

                url_file_name = 'https://www.rba.gov.au/rss/rss-cb-exchange-rates.xml'
                page = requests.get(url_file_name)
                main(page.text)


            except:
                print ('Issues detected retrieving the file... \nPlease check the link\n{url_file_name}\n\nHave a nice day')
        else:
            print ('Looks like the data has already been loaded\nHave a nice day')
    except:
        print()


    # Closing the database..

    conn.close()
