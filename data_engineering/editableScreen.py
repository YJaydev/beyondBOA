import os

from pandas import read_csv

import data_engineering.appconstants as appconstants
import pandas as pd

import data_engineering.sendingemails as sendingemails

csv_name = "datasource/Metadata Library.xlsx"
# test_pr_in=pd.read_excel(csv_name,error_bad_lines=False)
df = pd.read_excel(csv_name)
df1 = df.values.tolist()
df1.insert(0, df.columns.values)
df = pd.DataFrame(df1)

html_string = '''<html>
       <head>

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

       </body>
       </html>'''

# OUTPUT AN HTML FILE
# df.style.set_table_attributes('style="align-self: center;"')
html_file = open("datasource/editableScreen.html", "w")
html_file.write(html_string.format(table=df.to_html(classes='Editable_Data', index=False, header=False))
                    .replace('<table border="1"', '<table border="1" style="align-self: center;"').replace('<td>','<td contenteditable="true">'))

html_file.close()

