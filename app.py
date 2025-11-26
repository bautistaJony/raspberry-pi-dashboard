import os
import subprocess
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

def run_command(command):
    """Ejecuta un comando en el shell y devuelve la salida como texto."""
    try:
        # Ejecutar el comando en el shell. text=True asegura salida de texto.
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Devuelve el error si el comando falla
        return f"Error ejecutando '{command}': {e.stderr.strip()}"
    except FileNotFoundError:
        return f"Error: Comando no encontrado."

@app.route('/')
def dashboard():
    """Ruta principal que muestra el dashboard con métricas."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. Logs del Kernel (dmesg - Últimos 20)
    # Usamos la ruta absoluta del comando dmesg para mayor robustez
    dmesg_output = run_command("/usr/bin/dmesg | tail -n 20")

    # 2. Uso de Disco (df -h /)
    df_output = run_command("/usr/bin/df -h /")

    # NOTA: Los comandos de Uptime y Logs de Servicios han sido eliminados por solicitud.

    return render_template(
        'index.html',
        timestamp=current_time,
        dmesg_logs=dmesg_output,
        df_h=df_output
    )

if __name__ == '__main__':
    # Gunicorn ejecutará la aplicación en el puerto 5000 en el entorno Docker.
    # Esta parte se usa para pruebas locales.
    app.run(host='0.0.0.0', port=5000, debug=True)