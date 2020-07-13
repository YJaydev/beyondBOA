import os

import pdfkit
from pandas import read_csv

import appconstants
import pandas as pd

import sendingemails

csv_name = "datasource/missing_data.csv"



if os.path.isfile(csv_name):
    df = read_csv(csv_name)
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
       Missing Data from Meta Data Library
       </h1>
       
         {table}
       
       </body>
       </html>'''

    # OUTPUT AN HTML FILE
    # df.style.set_table_attributes('style="align-self: center;"')
    html_file = open("datasource/missingReport.html", "w")
    html_file.write(html_string.format(table=df.to_html(classes='Missing_Data', index=False, header=False)))

    html_file.close()





path_wkthmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)

pdfkit.from_url("datasource/missingReport.html", "datasource/Missing_Report.pdf", configuration=config)


print(os.path.isfile('datasource/Missing_Report.pdf'))

# if os.path.isfile('datasource/Missing_Report.pdf'):
#     sendingemails.emailnotification.sendingEmail('datasource/Missing_Report.pdf')