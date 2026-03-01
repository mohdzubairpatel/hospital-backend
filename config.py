import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="anees",
        database="hospital_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    

