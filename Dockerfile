# Usa la imagen oficial de Python para arquitectura ARM (Raspberry Pi)
FROM arm32v7/python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación (incluyendo app.py y la carpeta templates/)
COPY app.py .
COPY templates/ templates/

# Expone el puerto que usará Gunicorn/Flask
EXPOSE 5000

# Comando para ejecutar la aplicación con Gunicorn
# El uso de 4 workers es adecuado para la Raspberry Pi Zero 2 W.
# Ejecuta la aplicación Flask llamada 'app'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
