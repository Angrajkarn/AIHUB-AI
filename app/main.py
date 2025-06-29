from fastapi import FastAPI
from app.core.startup import setup_startup_tasks
from app.core.middleware import add_cors
from app.core.exceptions import custom_exception_handler
from app.routes import chat, summary, upload

app = FastAPI(title="AIHub Backend")

setup_startup_tasks(app)
add_cors(app)
app.include_router(chat.router)
app.include_router(summary.router)
app.include_router(upload.router)

app.add_exception_handler(Exception, custom_exception_handler)