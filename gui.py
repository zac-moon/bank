import tkinter as tk
import socket

root = tk.Tk()
root.title('ZBANK LINK - LOGIN')
root.geometry('800x600')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)
client_socket.connect(server_address)

def main(username):
    def balance():
        client_socket.send(f'balance.{username}'.encode('utf-8'))
        balance = client_socket.recv(1024).decode('utf-8')
        return balance

    def transfer():
        pass

    client = tk.Toplevel(root)
    client.title(f'ZBANK LINK - {username}')
    client.geometry('800x600')

    client_title = tk.Label(client, text=f"ZBANK LINK - {username}")
    balance_label = tk.Label(client, text=f"BALANCE : £{balance()}", font=('Arial', 90))
    transfer_btn = tk.Button(client, text="TRANSFER", command=transfer)

    client_title.pack()
    balance_label.pack()
    transfer_btn.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    client_socket.send(f'login.{username}.{password}'.encode('utf-8'))
    resp = client_socket.recv(1024).decode('utf-8')
    if resp == "1":
        print('Correct Details')
        main(username)
    elif resp == "0":
        print('Account Not Found')
    else:
        print('Password Incorrect')

main_title = tk.Label(root, text="ZBANK LINK - LOGIN", font=('Arial', 40))
username_label = tk.Label(root, text='Username:')
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")
login_btn = tk.Button(root, text="Login", command=login)

main_title.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_btn.pack()
root.mainloop()
