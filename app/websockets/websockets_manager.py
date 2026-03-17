from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        #aqui se guardan todas las conexiones activas de React
        self.active_connections: list[WebSocket] = []

        async def connect(self, websocket: WebSocket):
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)

        async def disconnect(self, websocket: WebSocket):
            if websocket in self.active_connections:
                self.active_connections.remove(websocket)

        async def broadcast(self, data: str):
            #enviar mensaje a todos los clientes conectados
            for connection in self.active_connections:
                try:
                    await connection.send_text(data)
                except Exception as e:
                    print(f"Error al enviar mensaje por WS: {e}")


#instacia para toda la app
ws_manager = ConnectionManager()