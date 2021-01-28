import socket

def code_runner():
    HOST = '192.168.0.62'
    PORT = 9090
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print("Code Runner v1.2")
    except:
        print("Connection to IDE failed.\nMake sure you run the ide first.")
        input("...")
        exit()

    while True:
        try:
            server_command = client.recv(1024).decode('utf-8')
            try:
                exec(server_command)
            except:
                print("An error occurred.")
        except:
            break

code_runner()

