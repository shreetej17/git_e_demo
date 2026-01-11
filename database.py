import mysql.connector

def connect_db(user, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database="prod"
        )
        return conn
    except:
        print("DB connection failed")
        return None
