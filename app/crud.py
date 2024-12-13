import uuid
from .database import redis_client
from .schemas import TodoItem

def create_todo(todo: TodoItem):
    todo_id = str(uuid.uuid4())
    todo_dict = todo.dict()
    todo_dict['id'] = todo_id
    redis_client.hset(f"todo:{todo_id}", mapping=todo_dict)
    return todo_dict

def get_all_todos():
    keys = redis_client.keys("todo:*")
    return [redis_client.hgetall(key) for key in keys]