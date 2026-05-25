import socket
import tkinter as tk
from tkinter import END

HOST = "127.0.0.1"
PORT = 5050

client = socket.socket()
client.connect((HOST, PORT))



def receive_message():
    try:
        msg = client.recv(1024).decode()

        if msg:
            chat_box.insert(END, "Server: " + msg + "\n")

    except:
        pass



def send_message():
    msg = entry.get()

    if msg:
        client.send(msg.encode())
        chat_box.insert(END, "Client: " + msg + "\n")
        entry.delete(0, END)



root = tk.Tk()
root.title("Client")
root.geometry("300x350")

chat_box = tk.Text(root, height=15, width=35)
chat_box.pack()

receive_btn = tk.Button(root, text="Receive", command=receive_message)
receive_btn.pack()

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

entry = tk.Entry(root, width=35)
entry.pack()

root.mainloop()