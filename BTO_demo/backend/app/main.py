from fastapi import FastAPI, WebSocket
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()

# CORSを回避するために追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッドるHTTPメソッド
    allow_headers=["*"],  # 許可するヘッダー
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()  # クライアントからのWebSocket接続を受け入れる
    while True:  # 無限ループでクライアントからのメッセージを待機
        data = await websocket.receive_text()  # クライアントからテキストメッセージを受け取る
        await websocket.send_text(f"Message text was: {data}")  # 受け取ったメッセージを加工してクライアントに送り返す

