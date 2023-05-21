import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP y credenciales
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'example@example.com'
smtp_password = 'example'

# Crear objeto EmailMessage
message = EmailMessage()

# Configurar remitente, destinatarios y asunto
message['From'] = 'example@example.com'
message['To'] = 'example@example.com'
message['Subject'] = 'this is a test email'

# Agregar contenido al mensaje en formato HTML y texto plano
message.add_alternative("""
    <html>
        <body>
            <h1>¡Hola!</h1>
            <p>this is a test email sent from Python.</p>
        </body>
    </html>
""", subtype='html')


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(message)
