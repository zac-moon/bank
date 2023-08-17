import tkinter as tk
import socket

root = tk.Tk()
root.title('ZBANK LINK - LOGIN')
root.geometry('800x600')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)
client_socket.connect(server_address)

def main():
    print('Logged IN')
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
