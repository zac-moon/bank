import socket

host = socket.gethostbyname()
port = 12345      

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Server listening on", host, "port", port)

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from:", client_address)

    data = client_socket.recv(1024).decode() 
    datas = data.split('.')
    cmd = datas[0]

    if cmd == "login":
        username = datas[1]
        password = datas[2]
        print(f'{client_address} tried login as {username} with password {password}')
        try:
            with open(f'db/users/{username}') as file:
                tru_pass = file.read().strip()  
            if password == tru_pass:
                client_socket.send('1'.encode())
                print(f'{client_address} logged in successfully as {username} with password {password}')
            else:
                client_socket.send('0'.encode())
                print(f'{client_address} tried incorrect password {password}')
        except FileNotFoundError:
            client_socket.send('2'.encode())
            print(f'{client_address} tried account {username} {password}- Account Not Found')

    if cmd == 'balance':
        print(f'{client_address} requested Balance Mode.')
        username = datas[1]
        try:
            with open(f'db/balance/{username}', 'r') as file:
                balance = file.read().strip()
                print(f'read balance for {client_address} as {balance}')
            print(f'{client_address} requested balance for {username}- BALANCE RETURNED ({balance})')
            client_socket.send(balance.encode())
            print(f'Sent Balance {balance} to {client_address}')
        except FileNotFoundError:
            print(f'{client_address} requested balance for {username}- NO BALANCE FILE FOUND')
            client_socket.send('0'.encode())

    client_socket.close()
