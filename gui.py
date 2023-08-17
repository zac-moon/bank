import tkinter as tk

root = tk.Tk()
root.title('ZBANK LINK - LOGIN')
root.geometry('800x600')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(), 12345)
client_socket.connect(server_address)

def main():
    username = usernameEntry.get()
    password = passwordEntry.get()


mainTitle = tk.Label(root, text="ZBANK LINK - LOGIN", font=('Arial', 40))
usernameLabel = tk.Label(root, text='Username:')
usernameEntry = tk.Entry(root)
passwordLabel = tk.Label(root, text="Password:")
passwordEntry = tk.Entry(root, show="*") 
loginBtn = tk.Button(root, text="Login", command=main)

mainTitle.pack()
usernameLabel.pack()
usernameEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
loginBtn.pack()
root.mainloop()
