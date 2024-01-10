from fastapi import FastAPI, Depends
from typing import List
from pydantic import BaseModel
from ._database_table import Creating_table, Todo_Table
from ._database_connection import Session


app = FastAPI()

Creating_table()


class Todo(BaseModel):
    task: str
    status: str


@app.post("/api/todos/add")
async def create_todos(todo: Todo):
    with Session() as session:
        todo = Todo_Table(task=todo.task, status=todo.status)
        session.add(todo)
        session.commit()
        print("Data sent")

    return todo


@app.get("/api/todos/")
async def read_todos():
    with Session() as session:
        todos = session.query(Todo_Table).all()
    return todos


@app.put("/api/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    with Session() as session:
        updated_todo = (
            session.query(Todo_Table).filter(Todo_Table.id == todo_id).first()
        )
        updated_todo.task = todo.task
        updated_todo.status = todo.status
        session.commit()
    return updated_todo


@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    with Session() as session:
        deleted_todo = (
            session.query(Todo_Table).filter(Todo_Table.id == todo_id).first()
        )
        session.delete(deleted_todo)
        session.commit()
    return deleted_todo
