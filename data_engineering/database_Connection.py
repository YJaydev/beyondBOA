import mysql.connector


db_connection = mysql.connector.connect(

host='localhost',
user='root',
passwd=''

)

print(db_connection)