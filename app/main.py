from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
import json

app = FastAPI()

# Redis Connect
redis = Redis(host="localhost", port=6379, decode_responses=True)

# 연결 테스트
try:
    if redis.ping():
        print("Redis 연결 성공!")
except Exception as e:
    print(f"Redis 연결 실패: {e}")

class Todo(BaseModel):
    id: str
    title: str
    description: str = ""
    done: bool = False  # Add 'done' to handle task completion

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI To-Do List with Redis"}

@app.post("/todo/")
def create_todo(todo: Todo):
    todo_data = {"title": todo.title, "description": todo.description, "done": todo.done}
    # Set the data with a TTL of 10 seconds
    redis.set(todo.id, json.dumps(todo_data), ex=10)
    return {"message": f"To-Do item {todo.id} created and will expire in 10 seconds"}

@app.get("/todo/{id}")
def get_todo(id: str):
    todo = redis.get(id)
    if not todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return json.loads(todo)

@app.put("/todo/{id}")
def update_todo(id: str, todo: Todo):
    # Check if the To-Do item exists
    existing_todo = redis.get(id)
    if not existing_todo:
        raise HTTPException(status_code=404, detail="To-Do item not found")

    # Update the existing To-Do item
    updated_data = {
        "title": todo.title,
        "description": todo.description,
        "done": todo.done,
    }
    redis.set(id, json.dumps(updated_data), ex=10)  # Optional: Reset TTL if needed
    return {"message": f"To-Do item {id} updated successfully", "updated_data": updated_data}

@app.delete("/todo/{id}")
def delete_todo(id: str):
    # Attempt to delete the To-Do item from Redis
    result = redis.delete(id)
    if result == 0:
        # If result is 0, the key does not exist in Redis
        raise HTTPException(status_code=404, detail="To-Do item not found")
    return {"message": f"To-Do item {id} deleted successfully"}
