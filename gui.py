import tkinter as tk

root = tk.Tk()
root.title('ZBANK LINK - LOGIN')
root.geometry('800x600')

def main():
    print('Main')

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
