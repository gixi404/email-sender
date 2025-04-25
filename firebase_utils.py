"""Módulo para interactuar con Firebase Admin SDK"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

keys = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(keys)

def get_emails() -> list[str]:
    """Obtiene una lista de los emails de usuarios registrados en Firebase"""
    emails: list = []
    page = auth.list_users()
    while page:
        for user in page.users:
            if user.email is None:
                continue
            emails.append(user.email)
        page = page.get_next_page()
    return emails
