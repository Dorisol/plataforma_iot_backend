from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.websockets.websockets_manager import ws_manager

router = APIRouter()

@router.websocket("/ws/dashboard")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            #mantener la conexión abierta
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        print("Cliente desconectado")
    finally:
        ws_manager.disconnect(websocket)
        await websocket.close()

