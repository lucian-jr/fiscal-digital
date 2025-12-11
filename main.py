from fastapi import FastAPI, BackgroundTasks, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
from ai_service import AnalisadorDeReclamacoes

app = FastAPI()
analisador = AnalisadorDeReclamacoes()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# ----------------------------------------------------------


class Reclamacao(BaseModel):
    titulo: str
    descricao: str
    cidadao: str
    

async def processar_reclamacao(reclamacao: Reclamacao):
    resultado = analisador.analisar_risco(reclamacao.descricao)
    
    if resultado["urgencia"]:
        mensagem_alerta = f"🚨 ALERTA: {resultado['categoria']} reportada por {reclamacao.cidadao}!"
        print(f"ENVIADO ALERTA VIA WEBSOCKET: {mensagem_alerta}")
        await manager.broadcast(mensagem_alerta)
        
    print(f"LOG: Reclamacao processada. Score: {resultado['score_risco']}")
    
@app.post("/api/v1/reclamacao")
async def criar_reclamacao(dados: Reclamacao, background_tasks: BackgroundTasks):
    background_tasks.add_task(processar_reclamacao, dados)
    
    return {"mensagem": "Reclamação recebida e está sendo processada."}

@app.websocket("/ws/monitoramento")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)        

        