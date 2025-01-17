import uvicorn
from fastapi import FastAPI

from fastapi_todo.views.todo_views import todo_router
from fastapi_todo.views.user_views import user_router

app = FastAPI(openapi_url="/openapi.json")

app.router.prefix = "/api/v1"

app.include_router(user_router, prefix="/users")
app.include_router(todo_router, prefix="/todos")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080, log_level='debug');
