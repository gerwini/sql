import os
import datetime
import pymysql
# get username from github

username = os.getenv('GITHUB_ACTOR')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1995-05-09 14:04:56"),
                ("Fred", 100, "1911-09-12 11:04:56")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    connection.close()
