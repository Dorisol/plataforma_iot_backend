import json
import paho.mqtt.client as mqtt
from uuid import UUID
import uuid
from app.db.session import SessionLocal
from app.models.MedicionesModel import Mediciones

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado exitosamente al Broker MQTT")
        client.subscribe("v1/+/+/data")
    else:
        print(f"Error de conexión al broker, código: {rc}")

def on_message(client, userdata, msg):
    #print(f"\nNuevo mensaje recibido en tópico: {msg.topic}")
    db = None
    
    try:
        # El tópico viene como: v1/uuid_tenant/uuid_dispositivo/data
        parts = msg.topic.split('/')
        if len(parts) < 4:
            print(f"Tópico no reconocido: {msg.topic}")
            return

        # Convertir strings a objetos UUID para que SQLAlchemy no falle
        tenant_uuid = UUID(parts[1])
        device_uuid = UUID(parts[2])
        
        payload = json.loads(msg.payload.decode())
        #print(f"Payload decodificado: {payload}")

        db = SessionLocal()
        # Crear el registro usando el modelo de SQLAlchemy
        nueva_medicion = Mediciones(
            idMedicion = uuid.uuid4(),
            idTenant=tenant_uuid,
            idUsuario=device_uuid,
            variable=payload.get("variable"),
            val=payload.get("val"),
            unit=payload.get("unit"),
            metadata_medicion={"device": str(device_uuid)}
        )
        
        db.add(nueva_medicion)
        db.commit()
        #print("¡Medición guardada en la base de datos!")
    except Exception as e:
        print(f"ERROR procesando mensaje: {e}")
    finally:
        if db:
            db.close()

def start_mqtt():
    client = mqtt.Client()
    # Credenciales configuradas en el ESP32... Aqui debo cuidar las credenciales que debo pasar..
    client.username_pw_set("esp_user_1", "4321")
    client.on_connect = on_connect
    client.on_message = on_message
    
    # 'mosquitto' es el nombre del servicio en docker-compose.yml
    try:
        client.connect("mosquitto", 1883, 60)
        client.loop_start()
    except Exception as e:
        print(f"No se pudo iniciar el cliente MQTT: {e}")