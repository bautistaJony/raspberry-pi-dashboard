Dashboard de Monitoreo de Sistema (Raspberry Pi/ARM)
Este proyecto despliega un dashboard web ligero para el monitoreo de métricas de salud y logs críticos en un dispositivo headless (sin monitor) Raspberry Pi, utilizando la arquitectura de contenedores Docker y el framework Flask (Python).

Despliegue Rápido (Quick Start)
Para ejecutar este dashboard, solo se necesita tener Docker instalado en una Raspberry Pi con arquitectura ARM (como la Pi Zero 2 W o Pi 3/4).

1. Clonar el Repositorio
Abre la terminal de tu Raspberry Pi y clona este repositorio:

git clone https://github.com/bautistaTony/raspberry-pi-dashboard.git
cd raspberry-pi-dashboard
2. Construir la Imagen Docker
Construye la imagen. El proceso descargará la imagen base de Python para ARM e instalará Flask y Gunicorn.


# El argumento -t etiqueta la imagen como 'pi-dashboard'
sudo docker build -t pi-dashboard .
3. Ejecutar el Contenedor (Modo Privilegiado)
Ejecuta el contenedor con la configuración necesaria para acceder a los logs y puertos.
Nota Crítica: El flag --privileged es obligatorio para que el contenedor pueda ejecutar el comando dmesg y leer los logs del kernel del sistema operativo anfitrión.

sudo docker run -d \
--privileged \
-p 80:5000 \
-v /var/log:/var/log-host:ro \
--name dashboard-app \
pi-dashboard

Arquitectura del Proyecto
Dockerfile	Define el entorno Linux, instala dependencias (Flask, Gunicorn) y configura la ejecución.
app.py	Backend de la aplicación. Ejecuta comandos de Linux (df -h /, dmesg) y renderiza la plantilla HTML con los datos obtenidos.
templates/index.html	Frontend. Contiene el diseño CSS (Dark Mode) y la estructura HTML que recibe los datos dinámicos de Python.
requirements.txt	Lista las dependencias de Python necesarias (Flask, gunicorn).

Funcionalidades
Uso de Disco (Root)	df -h /	Métrica de salud: Verifica el espacio disponible en la tarjeta SD principal.
Logs del Kernel	`dmesg	tail -n 20`


Acceso al Dashboard
Una vez que el contenedor esté en estado Up, accede a la aplicación desde cualquier navegador en la misma red local.

Encuentra la IP: Obtén la Dirección IP de tu Raspberry
ip a
Navegador: Abre tu navegador y escribe la IP
