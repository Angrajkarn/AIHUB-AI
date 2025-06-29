import firebase_admin
from firebase_admin import credentials
from fastapi import FastAPI
from .config import settings
import logging

def init_firebase():
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': settings.FIREBASE_PROJECT_ID,
    })

def configure_logging():
    logging.basicConfig(level=logging.INFO)

def setup_startup_tasks(app: FastAPI):
    init_firebase()
    configure_logging()