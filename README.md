# FastTasks
This project is a simple and efficient TODO list management application built using FastAPI and Redis. It allows users to add, view, and delete tasks seamlessly while leveraging Redis for fast and reliable data storage. The application is designed to be lightweight, scalable, and easy to integrate into other systems or services.

Key Features:

Add tasks to the TODO list.
View all tasks in the TODO list.
Delete specific tasks from the list.
Fast and efficient backend powered by Redis.
RESTful API structure for easy interaction and integration.
Technology Stack:

Backend: FastAPI (Python)
Database: Redis (In-memory data storage)
This application is ideal for those looking to manage tasks efficiently with a modern and minimalistic backend.

## Installation
Create a virtual environmen
```
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Application
```
uvicorn main:app --reload
```
