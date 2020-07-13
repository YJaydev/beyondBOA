from django.db import connection
from django.shortcuts import render, redirect
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from manualscreen import fetchingRecords
from .models import Task
from .serializer import TaskSerializer
import pandas as pd

# @api_view(['GET', 'POST'])
# def apioverview(request):
#     return JsonResponse("API BASE POINT", safe=False)

@api_view(['GET'])
def apioverview(request):
    api_url={}
    return Response(api_url)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetails(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task= Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task= Task.objects.get(id=pk)
    task.delete()
    return Response("item is deleted")

@api_view(['POST'])
def dataUpdate(request, pk):
    query = "SELECT * FROM metadata"

    tablename = "metadata"
    col_name="`Functionality Module`"
    id_num = "`Test Case ID`"
    col_value= "'testing123'"
    id_value="'TC 1'"
    queryUpdate = "UPDATE "+tablename+ " SET " + col_name+"="+col_value + " WHERE "+ id_num +"=" +id_value+";"

    query1 = "UPDATE metadata SET `Functionality Module` = 'testing' WHERE `Test Case ID` = 'TC 1';"

    db_conn = connection.cursor()
    db_conn.execute(queryUpdate)
    db_conn.execute(query)
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    # print(db_conn.descrption)
    df.columns = fetchingRecords.records2Html()

    df=df.to_dict()
    return Response(df)


@api_view(['POST'])
def dataUpdate1(request):
    query = "SELECT * FROM metadata"

    tablename = "metadata"
    col_name="`Functionality Module`"
    id_num = "`Test Case ID`"
    col_value= "'testing123'"
    id_value="'TC 1'"
    queryUpdate = "UPDATE "+tablename+ " SET " + col_name+"="+col_value + " WHERE "+ id_num +"=" +id_value+";"

    query1 = "UPDATE metadata SET `Functionality Module` = 'testing' WHERE `Test Case ID` = 'TC 1';"

    db_conn = connection.cursor()
    db_conn.execute(queryUpdate)
    db_conn.execute(query)
    myresult = db_conn.fetchall()
    df = pd.DataFrame(myresult)
    # print(db_conn.descrption)
    df.columns = fetchingRecords.records2Html()

    df=df.to_dict()
    # return Response(df)

    # return  render(request, 'api/home.html' )
    return redirect(request, 'api/home.html')

