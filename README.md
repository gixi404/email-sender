## 📧 Envía emails automatizados a tus usuarios de Firebase

### 1. 📦 Instala las siguientes dependencias:

- `python-dotenv`
- `firebase-admin`

Puedes instalarlas utilizando pip:

```bash
pip install python-dotenv firebase-admin
```

### 2. 📝 Crea un archivo `.env` en el directorio raíz del proyecto y define las siguientes variables:

```env
YOUR_EMAIL_USER="correo-del@emisor.com"
YOUR_EMAIL_PASS="contraseña-de-aplicación"
```

[🔗 Crear contraseña de aplicación](https://myaccount.google.com/u/3/apppasswords?continue=https://myaccount.google.com/u/3/?hl%3Des_419%26utm_source%3DOGB%26utm_medium%3Dact%26gar%3DWzUwXQ&rapt=AEjHL4NS1EH-ILcnykdKnrqgSmF0G9giXU4pDOkKutLOkoQMT6WxJkz4lwiVCnFQbKAzkUl8gyh-rYA7V6xwAmjbrwFpEYTOIiA2jq1QBsXgPGDBmpUTdWU)

### 3. 🔐 Crea el archivo `firebase_credentials.json` en el directorio raíz del proyecto.

Instrucciones: Selecciona el proyecto > Configuración del proyecto > Cuentas de servicio > Generar nueva clave privada

### 4. 🗞️ Personaliza el archivo `templates.py` con el HTML que deseas enviar.

### 5. 🏃 Ejecuta el script `index.py` y se enviarán los emails:

```bash
python index.py
```
