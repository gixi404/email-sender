"""
Módulo principal encargado de enviar emails a través de SMTP utilizando
credenciales almacenadas en variables de entorno. Se conecta a Firebase para obtener la lista
de destinatarios y utiliza una plantilla HTML personalizada para el contenido del mensaje
"""
import sys
import smtplib
from email.message import EmailMessage
from os import getenv
from dotenv import load_dotenv
from firebase_utils import get_emails
from templates import email_template

print("\n* Cargando...\n")
load_dotenv()

USER: str = getenv("YOUR_EMAIL_USER")
PASS: str = getenv("YOUR_EMAIL_PASS")

if not USER or not PASS:
    print("\n⭕ Las credenciales del email no están especificadas\n")
    sys.exit()

def send_email(emails: list[str], template: str) -> None:
    """Recibe como argumentos una lista de emails y un template HTML"""
    all_successfully: bool = True
    for email in emails:
        msg = EmailMessage()
        msg.add_alternative(template, subtype="html")
        msg["subject"] = "Lymbrarie"
        msg["to"] = email
        msg["from"] = USER
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(USER, PASS)
            server.send_message(msg)
            server.quit()
            print(f"> Correo enviado a '{email}'")
        except smtplib.SMTPException as e:
            all_successfully = False
            print(f"\nx Error enviando correo a '{email}' - {e}\n")
    if all_successfully:
        print("\n🟢 Todos los correos se han enviado correctamente.\n")
    else:
        print("\n🔴 No se han enviado todos los correos correctamente.\n")

send_email(emails=get_emails(), template=email_template())
