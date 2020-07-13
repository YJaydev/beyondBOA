import json

from django.core.serializers import serialize
from json2html import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connections, connection
from django.db.utils import OperationalError
from django.utils.datetime_safe import time
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from manualscreen import fetchingRecords
from jinja2 import Template
from django import forms

# csv_name = "Metadata Library.xlsx"
# csv_name = "../B2B/test.csv"
#

# INSERTING RECORDS INTO DATABASE
# engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                        .format(user="cloudpipe",
#                                pw="Cloudpipe@1",
#                                db="cloudpipe"))
#
# # Creating a table from dataframe
# df = pd.read_csv(csv_name)
# df1 = df.values.tolist()
# df1.insert(0, df.columns.values)
# df = pd.DataFrame(df1)
# df.columns = df.iloc[0]
# df = df[1:]
#
# # Insert whole DataFrame into MySQL
# df.to_sql('metadata1', con=engine, if_exists='append', chunksize=10000)
#


# CHECKING DATABASE RECORDS AFTER INSERTION
# con = pymysql.connect('localhost', 'cloudpipe',
#     'Cloudpipe@1', 'cloudpipe')
#
# with con:
#
#     cur = con.cursor()
#     cur.execute("SELECT * FROM metadata1")
#
#     rows = cur.fetchall()
#
#     for row in rows:
#         print("{0} {1} {2}".format(row[0], row[1], row[2]))
#         print(row)
