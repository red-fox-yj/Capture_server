from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from distribution import _distribute

app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse("welcome")


@app.websocket("/wss")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive()
        print(data)
        await websocket.send_json(_distribute(data["text"]))


# 程序入口
uvicorn.run(app, host="0.0.0.0", port=8000)
