import socket

print("PyWrite v1.4\nWaiting for CodeRunner to connect..\nMake sure to run CodeRunner\n")

HOST = '127.0.0.1' # Enter your private IP (ipv4) using ipconfig (win) or ip addr (linux/mac)
PORT = 9090 # You can change this to what ever you want

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client, address = server.accept()

print(f"Connected to CODERUN_ADDR[{address}, type]")
print("All code will be viewed on the CodeRunner console.\n\n")

while True:
    cmd_input = input(">> ")
    client.send(cmd_input.encode('utf-8'))
