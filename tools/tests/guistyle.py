import tkinter as tk
from ttkthemes import ThemedStyle

def hellobtn():
    print('Hello Button')
    print(helloEntry.get())

root = tk.Tk()
root.title("Hello World")


helloLabel = tk.Label(root, text='Hello World')
helloButton = tk.Button(root, text='Hello Button', command=hellobtn)
helloEntry = tk.Entry(root)

helloLabel.pack()
helloButton.pack()
helloEntry.pack()
root.mainloop()
