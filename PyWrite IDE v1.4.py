import socket

print("PyWrite v1.4\nWaiting for CodeRunner to connect..\nMake sure to run CodeRunner\n")

HOST = '192.168.0.62'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

print(f"Connected to CODERUN_ADDR[{address}, type]")
print("All code will be viewed on the CodeRunner console.\n\n")

while True:
    cmd_input = input(">> ")
    client.send(cmd_input.encode('utf-8'))