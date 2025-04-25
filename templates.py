"""Módulo que contiene plantillas HTML para ser utilizadas en emails"""

def email_template() -> str:
    """Retorna una cadena de texto con el contenido HTML del correo"""
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valoramos tu opinión</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333333;
            max-width: 500px;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .email-container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            max-width: 600px;
            margin: 0 auto;
        }
        h1 {
            color: #6A1B9A;
            font-size: 24px;
            margin-top: 0;
        }
        .footer a {
            text-align: "start";
            font-size: 14.5px;
            margin-top: 30px;
            text-align: center;
        }
        .social-links {
            margin: 15px 0;
            text-align: center;
        }
        .bold {
            font-weight: bold;
        }
        .signature {
            margin: 20px 0;
        }
        .btn {
            display: inline-block;
            background-color: #8A2BE2;
            color: #ffffff !important;
            text-decoration: none;
            padding: 12px 25px;
            border-radius: 4px;
            font-weight: bold;
            margin: 15px 0;
            text-align: center;
        }
        .btn:hover {
            background-color: #6A1B9A;
        }
        .text-center {
            text-align: center;
        }
        .logo {
            text-align: center;
            margin-bottom: 20px;
        }
        .logo img {
            max-width: 150px;
            height: auto;
        }
        .mt {
            margin: 30px 0;
        }
        .text-header {
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <h1>En Lymbrarie valoramos tu opinión</h1>
        
        <p class="text-header">Nos encantaría que nos dieras tu feedback sobre tu experiencia con Lymbrarie. Puede ser desde una pequeña sugerencia hasta una gran necesidad. Te aseguramos que no te tomará más de <b>1 minuto</b>.</p>
        
        <div class="text-center mt">
            <a href="https://forms.gle/DU6vFCCtbfLemEaS9" target="_blank" class="btn">Responder encuesta</a>
        </div>
        
        <div class="signature">
            <p>Gracias por ayudarnos a mejorar,</p>
            <p class="bold">El equipo de Lymbrarie</p>
        </div>
        <div class="footer">
            <a href="https://lymbrarie.com" target="_blank">lymbrarie.com</a>
        </div>
    </div>
</body>
</html>
"""
