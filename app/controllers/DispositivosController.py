from sqlalchemy.orm import Session
from app.models.DispositivosModel import Dispositivos
from app.schemas import DispositivosSchema
from uuid import UUID
from fastapi import HTTPException
import subprocess
import docker

ACL_PATH = "/mosquitto_config/acl_file"
PASS_PATH = "/mosquitto_config/password_file"

#traer todos los dispositivos del tenant 
def get_dispositivos(db: Session, idTenant: UUID):
    return db.query(Dispositivos).filter(Dispositivos.idTenant == idTenant).all()

def get_todos_dispositivos(db: Session):
    return db.query(Dispositivos).all()

#agregar un nuevo dispositivo
def crearDispositivo(db: Session, nuevoDispositivo: DispositivosSchema.DispositivosCreate):
    try:
        nuevo_dispositivo = Dispositivos(
            idTenant=nuevoDispositivo.idTenant,
            username=nuevoDispositivo.username,
            apiKey=nuevoDispositivo.apiKey,
            rol=nuevoDispositivo.rol,
            isActivo=nuevoDispositivo.isActivo,
            protocolo=nuevoDispositivo.protocolo,
            imagenesDisponibles=nuevoDispositivo.imagenesDisponibles
        )
        db.add(nuevo_dispositivo)
        db.commit()
        db.refresh(nuevo_dispositivo)

        #aqui añadir nuevo dispositivo en el ACL file y password 
        if nuevo_dispositivo.protocolo=="MQTT":
            registrar_dispositivo_mqtt(nuevo_dispositivo.idTenant, nuevo_dispositivo.idDispositivo, nuevo_dispositivo.username, nuevo_dispositivo.apiKey)

        return nuevo_dispositivo
    
    except Exception as e:
        db.rollback() 
        print("Error real en la BD: ", str(e))
        raise HTTPException(status_code=400, detail=f"Error en BD: {str(e)}")
    


def registrar_dispositivo_mqtt(tenant_id: str, dispositivo_id: str, username_mqtt: str, password_mqtt: str):
    
    # 1. Agregar el usuario y encriptar contraseña en password_file
    try:
        # Esto ejecuta: mosquitto_passwd -b /mosquitto_config/password_file <usuario> <contraseña>
        subprocess.run(
            ["mosquitto_passwd", "-b", PASS_PATH, username_mqtt, password_mqtt],
            check=True
        )
        print("Usuario MQTT creado y encriptado exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar mosquitto_passwd: {e}")
        return False

    # 2. Agregar los permisos en el acl_file
    try:
        with open(ACL_PATH, "a") as file:
            file.write(f"\n# Reglas autogeneradas para {username_mqtt}\n")
            file.write(f"user {username_mqtt}\n")
            file.write(f"topic write v1/{tenant_id}/{dispositivo_id}/data\n")
            file.write(f"topic write v1/{tenant_id}/{dispositivo_id}/status\n")
            file.write(f"topic read v1/{tenant_id}/{dispositivo_id}/config\n")
        print("Reglas ACL añadidas exitosamente.")
    except:
        print("Error al escribir en ACL")
        return False

    # 3. Recargar Mosquitto automáticamente usando Docker
    try:
        client = docker.from_env()
        mosquitto_container = client.containers.get("iot_mosquitto")
        #señal de recarga (SIGHUP equivale al número 1)
        mosquitto_container.kill(signal=1)
        
        print("Mosquitto recargó los archivos exitosamente sin apagarse.")

    except Exception as e:
        print(f"Error al escribir en ACL: {e}")
        return False

    return True