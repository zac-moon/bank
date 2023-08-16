import socket
import tkinter as tk

def loggedin(username, password):
    loginwin = tk.Toplevel(root)
    loginwin.title(f'ZBANK LINK - {username}')
    loginwin.geometry('800x600')
    def getBal():
        client_socket.send(f"balance.{username}".encode())
        bal = client_socket.recv(1024).decode()
        client_socket.close()
        return bal

    balance = tk.StringVar()
    balance.set(f'Balance : £{getBal()}') 

    balanceLabel = tk.Label(loginwin, textvariable=balance, font=('Arial', 60))
    balanceLabel.pack()

root = tk.Tk()
root.title("ZBANK LINK - LOGIN")
root.geometry('800x600')

server_host = socket.gethostbyname()
server_port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

def main():
    username = usernameEntry.get()
    password = passwordEntry.get()
    client_socket.send(f'login.{username}.{password}'.encode())
    data = client_socket.recv(1024).decode()
    if data == '1':
        usernameEntry.delete(0, tk.END)
        passwordEntry.delete(0, tk.END)
        loggedin(username, password)

loginTitle = tk.Label(root, text='Login To ZBANK LINK', font=('Arial', 40))
usernameLabel = tk.Label(root, text='Username:')
usernameEntry = tk.Entry(root)
passwordLabel = tk.Label(root, text="Password:")
passwordEntry = tk.Entry(root, show="*")
loginButton = tk.Button(root, text="Login", command=main)

loginTitle.pack()
usernameLabel.pack()
usernameEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
loginButton.pack()

root.mainloop()
client_socket.close()
