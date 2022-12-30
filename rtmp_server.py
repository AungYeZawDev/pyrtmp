from pyrtmp.server import RTMPServer

def on_connect(client):
    print(f'New RTMP connection from {client.ip}')

server = RTMPServer(port=1935, on_connect=on_connect)
server.start()