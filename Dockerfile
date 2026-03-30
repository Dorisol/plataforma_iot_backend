FROM python:3.11-slim

#directorio de trabajo de contenedor 
WORKDIR /app

#dependencia para encriptar contraseñas de MQTT
RUN apt-get update && apt-get install -y mosquitto

#descargar dependencias de aqui
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copiar código back
COPY . .

#iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
