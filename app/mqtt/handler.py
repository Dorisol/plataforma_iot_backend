import json
import paho.mqtt.client as mqtt
from uuid import UUID
import uuid
from app.db.session import SessionLocal
from app.core.config import settings
from app.models.MedicionesModel import Mediciones

mqtt_client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado exitosamente al Broker MQTT", flush=True)
        #client.subscribe("v1/+/+/data")
        client.subscribe("v1/#") 
    else:
        print(f"Error de conexión al broker, código: {rc}", flush=True)

def on_message(client, userdata, msg):
    print("Holaaaaaaaaaaaaaaaaaaaaaaaaaa", flush=True)
    print(f"\nNuevo mensaje recibido en tópico: {msg.topic}", flush=True)
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
            idDispositivo=device_uuid,
            variable=payload.get("variable"),
            val=payload.get("val"),
            unit=payload.get("unit"),
            metadata_medicion={"device": str(device_uuid)}
        )
        
        db.add(nueva_medicion)
        db.commit()
        print("Medicion guardada")
    except Exception as e:
        print(f"ERROR procesando mensaje: {e}")
    finally:
        if db:
            db.close()

def start_mqtt():
    global mqtt_client
    mqtt_client.username_pw_set(settings.USER_MQTT, settings.PASSWORD_MQTT)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    
    # 'mosquitto' es el nombre del servicio en docker-compose.yml
    try:
        mqtt_client.connect("mosquitto", 1883, 60)
        mqtt_client.loop_start()
    except Exception as e:
        print(f"No se pudo iniciar el cliente MQTT: {e}")