import socket
import threading
import tkinter as tk
from tkinter import END

HOST = "127.0.0.1"
PORT = 5050

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

conn = None



def receive_message():
    global conn

    if conn:
        try:
            msg = conn.recv(1024).decode()

            if msg:
                chat_box.insert(END, "Client: " + msg + "\n")

        except:
            pass



def send_message():
    global conn

    msg = entry.get()

    if msg and conn:
        conn.send(msg.encode())
        chat_box.insert(END, "Server: " + msg + "\n")
        entry.delete(0, END)



def connect_client():
    global conn
    conn, addr = server.accept()



root = tk.Tk()
root.title("Server")
root.geometry("300x350")

chat_box = tk.Text(root, height=15, width=35)
chat_box.pack()

receive_btn = tk.Button(root, text="Receive", command=receive_message)
receive_btn.pack()

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

entry = tk.Entry(root, width=35)
entry.pack()

threading.Thread(target=connect_client, daemon=True).start()

root.mainloop()