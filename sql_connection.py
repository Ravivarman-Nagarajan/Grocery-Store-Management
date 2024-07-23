__cnx  = None

import mysql.connector

def get_sql_connection():
    global __cnx 
    if __cnx is None :
        __cnx = mysql.connector.connect(user='root', password='Ravi452', host='127.0.0.1',
        database='grocery_store')

    return __cnx