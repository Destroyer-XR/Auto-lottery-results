sio = socketio.Client()
import socketio #pip install "python-socketio[client]"

@sio.event
def connect():
    print(f"✅ Connected, SID: {sio.sid}")

@sio.event
def disconnect():
    print("🔴 Disconnected")

@sio.on("server")
def on_server(data):
    print(data)
    ret = f"{data['lotteryName']}\n"
    ret += f"{data['thaiDate']}\n"
    ret += f"⏰เวลาผลออก {data['time']}\n"
    ret += "➖➖➖➖➖➖➖➖➖\n"
    ret += f"\n  {data['st3']} ➖ {data['st2']}\n\n"
    ret += "➖➖➖➖➖➖➖➖➖"
    print(ret)

def startLottery():
    sio.connect("wss://api.lotteryresulte.org", transports=["websocket"])
    sio.wait()