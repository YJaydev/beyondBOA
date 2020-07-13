import json

from django.core.serializers import serialize
from json2html import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connections,connection
from django.db.utils import OperationalError
from django.utils.datetime_safe import time
from sqlalchemy import create_engine
import pandas as pd
# import pymysql
from manualscreen import fetchingRecords
from jinja2 import Template
from django import forms


# csv_name = "Metadata Library.xlsx"
csv_name  = "../B2B/test.csv"





class someform(forms.Form):
    col_name = forms.CharField(max_length=100)
    id_num = forms.CharField(max_length=100)
    col_value = forms.CharField(max_length=250)





def screen1(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM metadata")
    results = cursor.fetchall()
    # return render(request,'1index.html',{'getStudentdetails': results})
    # return HttpResponse(results)
    return render(request, 'manualscreen/screen.html')


def tablecreation(request):
    # create sqlalchemy engine
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="cloudpipe",
                               pw="Cloudpipe@1",
                               db="cloudpipe"))

    # Creating a table from dataframe
    df = pd.read_excel(csv_name)
    df1 = df.values.tolist()
    df1.insert(0, df.columns.values)
    df = pd.DataFrame(df1)
    df.columns = df.iloc[0]
    df = df[1:]

    # Insert whole DataFrame into MySQL
    df.to_sql('metadata', con = engine, if_exists = 'append', chunksize = 10000)


def serialize_bootstraptable(queryset):
    json_data = serialize('json', queryset)
    json_final = {"total": queryset.count(), "rows": []}
    data = json.loads(json_data)
    for item in data:
        del item["model"]
        item["fields"].update({"id": item["pk"]})
        item = item["fields"]
        json_final['rows'].append(item)
    return json_final

def screen(request):
    db_conn = connection.cursor()
    db_conn.execute("SELECT * FROM metadata")
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    # print(db_conn.descrption)
    df.columns = fetchingRecords.records2Html()

    df=df.to_dict()
    return render(request, 'manualscreen/try.html', {'data': df})

def try1(request):
    db_conn = connection.cursor()
    db_conn.execute("SELECT * FROM metadata")
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    # print(db_conn.descrption)
    df.columns = fetchingRecords.records2Html()

    df=df.to_dict()
    # df = df.to_json()
    # for key, value in df.items():
    #     print (key," : " ,value)
    return render(request, 'manualscreen/try1.html', {'data': df})



# @api_view(['POST'])
def dataupdate(request):
    query = "SELECT * FROM metadata"
    if request.method == 'POST':
        form = someform(request.POST)

    db_conn = connection.cursor()
    # db_conn.execute(queryUpdate)
    db_conn.execute(query)
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    # print(db_conn.descrption)
    df.columns = fetchingRecords.records2Html()

    df=df.to_dict()
    # return Response(df)

    return  render(request, 'manualscreen/home.html' )
    # return redirect('dataUpdate' )
    # return render(df)


def data(request):
    query = "SELECT * FROM metadata"
    db_conn = connection.cursor()
    # db_conn.execute(queryUpdate)
    db_conn.execute(query)
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    df.columns = fetchingRecords.records2Html()
    df=df.to_dict()
    return render(request, 'manualscreen/try1.html', {'data': df} )
    # return render(df)




def update(request):
    print(request.POST.dict())

    tablename = "metadata"
    col_name = "`"+request.POST.get('Column Name')+"`"
    # print(col_name)
    id_num = "`Test Case ID`"
    col_value = "'"+request.POST.get('Column value')+"'"
    id_value = "'"+request.POST.get('Testcase Name')+"'"
    queryUpdate = "UPDATE " + tablename + " SET " + col_name + "=" + col_value + " WHERE " + id_num + "=" + id_value + ";"

    # query1 = "UPDATE metadata SET `Functionality Module` = 'testing' WHERE `Test Case ID` = 'TC 1';"
    print(queryUpdate)
    db_conn = connection.cursor()
    # db_conn.execute(queryUpdate)
    db_conn.execute(queryUpdate)
    myresult = db_conn.fetchall()
    print(myresult)


    return render(request, 'manualscreen/index.html')




def metadata(request):
    print(request.POST.dict())
    # print(request.GET.get('Testcase Name'))
    # print(request.GET.get('Column Name'))
    # print(request.GET.get('Column value'))


    # tablename = "metadata"
    # col_name = "`"+request.POST.get('Column Name')+"`"
    # # print(col_name)
    # id_num = "`Test Case ID`"
    # col_value = "'"+request.POST.get('Column value')+"'"
    # id_value = "'"+request.POST.get('Testcase Name')+"'"
    # queryUpdate = "UPDATE " + tablename + " SET " + col_name + "=" + col_value + " WHERE " + id_num + "=" + id_value + ";"
    #
    # # query1 = "UPDATE metadata SET `Functionality Module` = 'testing' WHERE `Test Case ID` = 'TC 1';"
    # print(queryUpdate)
    # db_conn = connection.cursor()
    # # db_conn.execute(queryUpdate)
    # db_conn.execute(queryUpdate)
    # myresult = db_conn.fetchall()
    # print(myresult)


    return render(request, 'manualscreen/metadata.html')




def anydata(request):
    query = "SELECT * FROM metadata1"
    db_conn = connection.cursor()
    db_conn.execute(query)
    final_result = [list(i) for i in db_conn.fetchall()]
    return JsonResponse(final_result, safe=False)