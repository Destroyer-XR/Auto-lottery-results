import socketio #pip install "python-socketio[client]"

sio = socketio.Client()

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

def main():
    sio.connect("wss://api.lotteryresulte.org", transports=["websocket"])
    sio.wait()
    
    
if __name__ == "__main__":
    main()
    