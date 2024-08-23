# GUI for client programming.

import threading
import tkinter as tk
import socket

host = "192.168.1.38"
port = 6060
clientSocket = socket.socket()
clientSocket.connect((host, port))

def printInUi(message, colour):
    messageLabel = tk.Label(message_frame, text = message,bg = "black", fg = colour)
    messageLabel.pack(anchor = 'w', padx = 5, pady = 2)
    entry.delete(0, tk.END)
    canvas.yview_moveto(1)

def sendMessage():
    message = entry.get()
    name = getName.get()
    finalMessage = name + ": " + message
    if message.lower().strip() != 'bye':
        clientSocket.send(finalMessage.encode())
        printInUi(finalMessage, "blue")

def receiveMessage():
    while True:
        reply = clientSocket.recv(1024).decode()
        printInUi(str(reply), "pink")


window = tk.Tk()
window.title("Chat Box.")
window.config(bg = 'lightgreen')
window.geometry("500x600")

label = tk.Label(window, text = "Chat Box", bg = 'black', fg = "lightblue")
label.pack(padx = 20, pady = 20)

askName = tk.Label(window, text = "Name: ", fg = "green")
askName.pack(padx = 30, pady = 30)

getName = tk.Entry(window, text = "Enter name")
getName.pack(padx = 30, pady = 30)

frame = tk.Frame(window, bg = "black")
frame.pack(fill = tk.BOTH, expand = True, padx=20, pady=10)

canvas = tk.Canvas(frame, bg="black")
canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

scrollbar = tk.Scrollbar(frame, orient = "vertical", command = canvas.yview)
scrollbar.pack(side = tk.LEFT, fill = tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

message_frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=message_frame, anchor="nw")

def on_frame_configure(event):
    # Update scrollregion to encompass the frame
    canvas.configure(scrollregion=canvas.bbox("all"))

message_frame.bind("<Configure>", on_frame_configure)


entry = tk.Entry(window, textvariable = "Enter message", font = ("Arial", 14), width = 30)
entry.pack(side=tk.LEFT, padx=10, pady=10, anchor='s')
button = tk.Button(window, text = "Send", command = sendMessage)
button.pack(side=tk.LEFT, padx=10, pady=10, anchor='s')

thread = threading.Thread(target = receiveMessage)
thread.start()
window.mainloop()