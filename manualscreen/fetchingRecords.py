from sys import path

import mysql.connector
from mysql.connector import errorcode
import pandas as pd


df= pd.DataFrame()
html_string =''
mydb = mysql.connector.connect(
        host='localhost',
        user='cloudpipe',
        password='Cloudpipe@1',
        database='cloudpipe',
        port='3306'
    )


def records2Html():

    print(mydb)
    db_conn = mydb.cursor()
    db_conn.execute("SELECT * FROM metadata")
    # mycursor.execute("SELECT * FROM customers")
    myresult = db_conn.fetchall()

    df = pd.DataFrame(myresult)
    df.columns = db_conn.column_names
    print(db_conn.column_names)

    return df.columns

def htmlcreation():
    db_conn = mydb.cursor()
    db_conn.execute("SELECT * FROM metadata")
    # mycursor.execute("SELECT * FROM customers")
    myresult = db_conn.fetchall()

    df = pd.DataFrame(myresult)
    df.columns = db_conn.column_names
    print(db_conn.column_names)
    html_string = '''<html>
         <head><meta charset=utf-8 />
         <style type="text/css">
         body{{background: rgb(0, 255, 255,0.2);
         }}
         table, th, td {{font-weight: 500;
         font-size:10pt; border:1px solid black;
         border-collapse:collapse; text-align:left;
         margin-left:auto;margin-right:auto;
         background-color: rgba(0, 128, 0, 0.2);
         }}

         th, td,h1 {{padding: 10px;font-family: Verdana, sans-serif;}}
         .Missing_Data tr:first-child td {{
         font-weight: 600;
         color:Grey;
         }}
         </style>
         </head>
         <body>
         <h1 style="color:DarkSlateGray;text-align:center;margin-left:auto;margin-right:auto;padding: 10px;">
         Editable Meta Data Library
         </h1>

         {table}
        '''
    piece = '''<form>
        <input type="button" onclick="changeContent()" value="Change content" >
        </form>
        </body>
        <script>
        function changeContent() {
        row_num = window.prompt("Input the Row number()", "1");
        col_num = window.prompt("Input the Column number()","1");
        content = window.prompt("Input the Cell content");
        var x=document.getElementById('myTable').rows[parseInt(row_num-1,10)].cells;
        x[parseInt(col_num-1,10)].innerHTML=content;
        }</script></html>'''

    # OUTPUT AN HTML FILE
    # df.style.set_table_attributes('style="align-self: center;"')
    html_file = open("templates/manualscreen/screen.html", "w")
    html_file.write(html_string.format(table=df.to_html(classes='Editable_Data', index=False, header=True))
                    .replace('<table border="1"', '<table border="1" id="myTable" style="align-self: center;"'))
    html_file.write(piece)
    html_file.close()
    if path.exists('templates/manualscreen/screen.html'):
        html_string = 'screen.html'
    else:
        html_string = '<h1>Something went wrong</h1>'
    return html_string
