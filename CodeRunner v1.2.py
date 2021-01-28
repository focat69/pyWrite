import socket

def code_runner():
    HOST = '127.0.0.1' # Must be same as PyWrite file ipv4
    PORT = 9090 # Must be same port too
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
                exec(server_command) # I know this is stupid.
                                     # Don't yell because I will change this.
            except:
                print("An error occurred.")
        except:
            break

code_runner()

