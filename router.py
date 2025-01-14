from fastapi import FastAPI, HTTPException, status, Depends
from database import connect
from mysql.connector.connection import MySQLConnection
from crud import TodoBase, TodoCreate, TodoDelete, TodoUpdate, TodoGet


conn = connect()
#cursor = conn.cursor()



    


#create(db 커넥션이 유지되어야 한다) -> 커넥션이 연결되게 
#모델, 연결 전달되어야 함 
def create_todo(conn : MySQLConnection, todo_id: int, todo: TodoCreate):
    cursor = conn.cursor()

    todo_create = """
    INSERT INTO todo (date, title, context, todo_id, user_id)
    VALUES (%s, %s, %s, %s, %s);
    """
    values = (todo.date, todo.title, todo.context, todo_id, todo.user_id)

    cursor.execute(todo_create, values)

    conn.commit()

    return todo

def delete_todo(conn : MySQLConnection, todo_id: int):
    cursor = conn.cursor()

    todo_delete = "DELETE FROM todo WHERE todo_id = %s"
    cursor.execute(todo_delete, (todo_id,))
    conn.commit()

    return {"message": "deleted successfully"}


def update_todo(conn : MySQLConnection, todo_id: int, todo: TodoUpdate):
    cursor = conn.cursor()

    todo_update = """
    UPDATE todo
    SET date = %s, title = %s, context = %s
    WHERE todo_id = %s
    """
    values = (todo.date, todo.title, todo.context, todo_id)
    cursor.execute(todo_update, values)
    conn.commit()

    return get_todo(conn, todo_id)

def get_todo(conn : MySQLConnection, todo_id: int):
    cursor = conn.cursor(dictionary=True)
    todo_get = "SELECT * FROM todo WHERE todo_id = %s"
    print("todo_id is:", todo_id)
    cursor.execute(todo_get, (todo_id,))
    

    todo = cursor.fetchone()

    return todo

