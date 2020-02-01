""" This class is a simple helper to insert and maintain the MySQL DB """
import mysql.connector


class DbHelper:

    def __init__(self, obj):
        self.obj = obj
   
    def push_data(self):
        cnx = mysql.connector.connect(host="db", user='user', password="test", database='trafikverket')
        cursor = cnx.cursor()
        print(self.obj.sql)
        print(self.obj.values)
        cursor.execute(self.obj.sql, self.obj.values)
        cnx.commit()
        cnx.close()

    def remove_duplicates(self):
        cnx = mysql.connector.connect(host="db", user='user', password="test", database='trafikverket')
        cursor = cnx.cursor()
        cursor.execute(self.obj.sql_duplicate)
        cnx.commit()
        cnx.close()

    # @ToDo Add more db queries
