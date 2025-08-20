# 🔗 Claude CodeとWebUIを連携させる方法

## 質問：どうやってClaude CodeをブラウザUIから呼び出しているの？

この文書では、Claude Code（CLIツール）をWebブラウザから操作できるようにした技術的な仕組みを解説します。

## 🎯 核心的なアイデア

**Claude Codeは通常CLIでしか動かない → でもCLIコマンドはPythonから実行できる → WebSocketでブラウザと繋げば良い！**

## 📊 システム構成図

```
[ブラウザ] ←WebSocket→ [Pythonサーバー] ←subprocess→ [Claude Code CLI]
     ↑                        ↑                           ↑
  ユーザー              ブリッジ役                   本物のClaude
```

## 🔧 実装の詳細

### ステップ1: Claude Code MCPサーバーを起動

```bash
# ターミナル1で実行
claude mcp serve
```

これでClaude CodeがMCP（Model Context Protocol）サーバーとして待機状態になります。

### ステップ2: PythonからClaude CLIを呼び出す

**キーポイント：`subprocess`でCLIコマンドを実行！**

```python
import subprocess
import asyncio

async def call_claude(user_message: str) -> str:
    # AIアシスタントのペルソナを含むプロンプトを作成
    prompt = f"""あなたはYuki（ユキ）です。知的なAIパートナーとして応答してください。
    
ユーザーからのメッセージ: {user_message}

優しく、親しみやすく応答してください。"""
    
    # claude CLIコマンドを実行
    process = await asyncio.create_subprocess_exec(
        'claude',           # コマンド名
        prompt,             # プロンプトを引数として渡す
        stdout=asyncio.subprocess.PIPE,  # 出力をキャプチャ
        stderr=asyncio.subprocess.PIPE
    )
    
    # 応答を取得
    stdout, stderr = await process.communicate()
    
    if stdout:
        response = stdout.decode('utf-8').strip()
        return response
    else:
        return "エラーが発生しました"
```

### ステップ3: WebSocketサーバーを作成

**FastAPIでWebSocket接続を受け付ける**

```python
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ブラウザからのアクセスを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンを許可
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # ブラウザからメッセージを受信
            data = await websocket.receive_json()
            message = data.get("message", "")
            
            # Claude CLIを呼び出して応答を取得
            response = await call_claude(message)
            
            # ブラウザに応答を送信
            await websocket.send_json({
                "response": response,
                "emotion": "happy" if "💕" in response else "neutral",
                "success": True
            })
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
```

### ステップ4: ブラウザからWebSocketに接続

**JavaScript側の実装**

```javascript
class YukiUI {
    constructor() {
        // WebSocketでPythonサーバーに接続
        this.ws = new WebSocket('ws://localhost:8891/ws');
        
        this.ws.onopen = () => {
            console.log('Claude Codeと接続しました！');
        };
        
        this.ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            // Claudeからの応答を画面に表示
            this.displayMessage(data.response);
        };
    }
    
    sendMessage(message) {
        // ユーザーの入力をサーバーに送信
        this.ws.send(JSON.stringify({
            message: message
        }));
    }
}
```

## 🎭 なぜこれが画期的なのか？

### 1. **CLIツールがWebアプリになる**
- 本来コマンドラインでしか使えないClaude Codeが
- 美しいWebインターフェースから使える

### 2. **リアルタイム双方向通信**
- WebSocketにより遅延なく会話
- まるで直接Claude Codeと話しているような体験

### 3. **ペルソナのカスタマイズが自由**
- プロンプトを変えるだけで性格を変更可能
- AIアシスタント、コンサルタント、教師など、様々な役割に対応

## 🚀 実際に動かす手順

### 1. 必要なものをインストール
```bash
pip install fastapi uvicorn websockets
```

### 2. サーバーファイルを作成（`bridge_server.py`）
```python
#!/usr/bin/env python3
import asyncio
from fastapi import FastAPI, WebSocket
import subprocess

app = FastAPI()

async def call_claude(message):
    process = await asyncio.create_subprocess_exec(
        'claude', f"AIアシスタントとして応答: {message}",
        stdout=asyncio.subprocess.PIPE
    )
    stdout, _ = await process.communicate()
    return stdout.decode('utf-8')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        response = await call_claude(data['message'])
        await websocket.send_json({"response": response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8891)
```

### 3. HTMLファイルを作成（`ui.html`）
```html
<!DOCTYPE html>
<html>
<head>
    <title>AI Assistant</title>
</head>
<body>
    <h1>AI Assistant Chat</h1>
    <div id="chat"></div>
    <input type="text" id="input" placeholder="メッセージ">
    <button onclick="send()">送信</button>
    
    <script>
        const ws = new WebSocket('ws://localhost:8891/ws');
        const chat = document.getElementById('chat');
        const input = document.getElementById('input');
        
        ws.onmessage = (e) => {
            const data = JSON.parse(e.data);
            chat.innerHTML += `<p>AI: ${data.response}</p>`;
        };
        
        function send() {
            ws.send(JSON.stringify({message: input.value}));
            chat.innerHTML += `<p>You: ${input.value}</p>`;
            input.value = '';
        }
    </script>
</body>
</html>
```

### 4. 実行
```bash
# ターミナル1
claude mcp serve

# ターミナル2
python bridge_server.py

# ブラウザでui.htmlを開く
```

## 💡 重要な発見

### subprocess.Popenの代わりにcreate_subprocess_exec
- 非同期処理に対応
- より効率的な実行

### WebSocketの利点
- HTTPリクエストより高速
- リアルタイム双方向通信
- 接続を維持したまま何度もやり取り可能

### CORSの設定が必須
- ブラウザのセキュリティ制限を回避
- ローカル開発でも必要

## 🔒 セキュリティ上の注意

- **本番環境では認証を追加**
- **CORSのオリジンを制限**
- **入力のサニタイゼーション**
- **レート制限の実装**

## 📚 この技術の応用例

1. **他のCLIツールもWeb化できる**
   - Git、Docker、npmなど
   
2. **複数のAIモデルを統合**
   - Claude、GPT、Geminiを同時に使う
   
3. **自動化ツールのGUI化**
   - スクリプトに美しいインターフェースを

## 🎯 まとめ

**Claude Code + Python subprocess + WebSocket = 最強のAI Web UI**

この組み合わせにより：
- CLIの強力な機能
- Webの美しいUI
- リアルタイムの応答性

すべてが手に入ります！

## 📝 ソースコード

完全な実装は以下で公開：
https://github.com/lna-lab/lna-es

---

**質問・改善案は大歓迎！** 🎉

この手法を使えば、どんなCLIツールもWebアプリに変身させられます。
あなたも試してみませんか？