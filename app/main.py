from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db, get_mydb, connect
from app.crud import TodoUpdate, TodoDelete, TodoCreate, TodoGet
import app.router as router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

@app.on_event("startup")
def startup_event():
    conn = connect()
    init_db(conn)

@app.post("/todo/create/{todo_id}")
def create_todo(todo_id: int, todo: TodoCreate, conn = Depends(get_mydb)):
    router.create_todo(conn, todo_id, todo)
    return {"message": "todo is created"}


@app.delete("/todo/delete/{todo_id}")
def delete_todo(todo_id: int, conn = Depends(get_mydb)):
    router.delete_todo(conn, todo_id)
    return {"message": "todo is deleted"}


@app.put("/todo/update/{todo_id}") #get 하나 해서 그거 있으면 그거를 바꿔야 한다.
def update_todo(todo_id: int, todo: TodoUpdate, conn = Depends(get_mydb)):

    get_todo = router.get_todo(conn, todo_id)

    if get_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"todo with id: {todo_id} does not exist",
        )

    
    return router.update_todo(conn, todo_id, todo)
    

@app.get("/todo/get/{todo_id}")
def get_todo(todo_id: int, conn = Depends(get_mydb)):#get 한게 있으면 가져오기
    #투두 제목, 내용 돌려주기
    get_todo = router.get_todo(conn, todo_id)

    if get_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f"todo with id: {todo_id} does not exist",
        )
    
    return get_todo


