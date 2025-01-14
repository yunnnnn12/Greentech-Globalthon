from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import mysql.connector

from mysql.connector.connection import MySQLConnection


def init_db(conn: MySQLConnection):
    query = """
    CREATE TABLE IF NOT EXISTS todo (
        date VARCHAR(255),
        title VARCHAR(255),
        context VARCHAR(255),
        todo_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT  
    )
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    


def connect():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "dmsdbs22",
        database = "todo"
    )

    return mydb



def get_mydb():
    conn = connect()

    try:
        yield conn
    finally:
        conn.close()





