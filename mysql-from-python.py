import os
import pymysql
# get username from github

username = os.getenv('GITHUB_ACTOR')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:  # pymysql.cursors.DictCursor
        sql = "SELECT * FROM Artist;"
        cursor.exectute(sql)
        result = cursor.fetchfall()
        print(result)
        # for row in cursor:
        # print(row)
finally:
    connection.close()
