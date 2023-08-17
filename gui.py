import tkinter as tk
import socket

root = tk.Tk()
root.title('ZBANK LINK - LOGIN')
root.geometry('800x600')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)
client_socket.connect(server_address)

def main(username,password):
    print('Logged IN')
    print(username)
    print(password)
    usernameEntry.delete(0,tk.END)
    passwordEntry.delete(0,tk.END
    )
    client = tk.Toplevel(root)
    client.title(f'ZBANK LINK - {username}')
    client.geometry('800x600')

    def Balance():
        client_socket.send(f'balance.{username}'.encode('utf-8'))
        balance = client_socket.recv(1024)
        balance = balance.decode('utf-8')
        return balance

    clientTitle = tk.Label(client, text=f"ZBANK LINK - {username}")
    balance = Balance()
    balanceLabel = tk.Label(client,text=f"£{balance}")


    clientTitle.pack()
    balanceLabel.pack()

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    print(username)
    print(password)
    client_socket.send(f'login.{username}.{password}'.encode('utf-8'))
    resp = client_socket.recv(1024)
    resp = resp.decode('utf-8')
    if resp == "1":
        login = True
        print('Correct Details')
        main(username,password)
    elif resp == "0":
        print('Account Not Found')    
    else:
        print('Password Incorrect')

mainTitle = tk.Label(root, text="ZBANK LINK - LOGIN", font=('Arial', 40))
usernameLabel = tk.Label(root, text='Username:')
usernameEntry = tk.Entry(root)
passwordLabel = tk.Label(root, text="Password:")
passwordEntry = tk.Entry(root, show="*") 
loginBtn = tk.Button(root, text="Login", command=login)

mainTitle.pack()
usernameLabel.pack()
usernameEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
loginBtn.pack()
root.mainloop()
