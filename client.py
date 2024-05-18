# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 12345

Mistyrose2 = '#EED5D2'
Cornsilk1 = '#FFF8DC'
Plum2 = '#EEA9A9'
Black = '#000000'
Mistyrose4 = '#8B7D7B'
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

# Creating a socket object
# AF_INET: we are going to use IPv4 addresses
# SOCK_STREAM: we are using TCP packets for communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
try:
        server_ip = server_ip_textbox.get()
        server_port = int(server_port_textbox.get())
        client.connect((server_ip, server_port))
        add_message("[SERVER] Successfully connected to the server")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to server: {e}")
        return

    username = username_textbox.get()
    if username:
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid Username", "Username cannot be empty")
        return

    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)

   def send_message():
    message = message_textbox.get()
    recipient = recipient_textbox.get()
    if message:
        if recipient:
            final_message = f"@{recipient} {message}"
        else:
            final_message = message
        client.sendall(final_message.encode())
        message_textbox.delete(0, tk.END)
    else:
        messagebox.showerror("Empty Message", "Message cannot be empty")

def listen_for_messages_from_server(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                username, content = message.split('~')
                add_message(f"[{username}] {content}")
            else:
                messagebox.showerror("Error", "Received empty message")
        except Exception as e:
            messagebox.showerror("Connection Error", f"Lost connection to server: {e}")
            client.close()
            break

# GUI Setup
root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=4)
root.grid_rowconfigure(5, weight=1)

# Top frame
top_frame = tk.Frame(root, width=600, height=50, bg=Mistyrose2)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)
server_ip_label = tk.Label(top_frame, text="Server IP:", font=FONT, bg=Mistyrose2)
server_ip_label.pack(side=tk.LEFT, padx=5)
server_ip_textbox = tk.Entry(top_frame, font=FONT, bg=Mistyrose4, fg=Black, width=15)
server_ip_textbox.pack(side=tk.LEFT, padx=5)
server_port_label = tk.Label(top_frame, text="Port:", font=FONT, bg=Mistyrose2)
server_port_label.pack(side=tk.LEFT, padx=5)
server_port_textbox = tk.Entry(top_frame, font=FONT, bg=Mistyrose4, fg=Black, width=5)
server_port_textbox.pack(side=tk.LEFT, padx=5)

# Username frame
username_frame = tk.Frame(root, width=600, height=50, bg=Mistyrose2)
username_frame.grid(row=1, column=0, sticky=tk.NSEW)
username_label = tk.Label(username_frame, text="Enter username:", font=FONT, bg=Mistyrose2, fg=Black)
username_label.pack(side=tk.LEFT, padx=10)
username_textbox = tk.Entry(username_frame, font=FONT, bg=Mistyrose4, fg=Black, width=20)
username_textbox.pack(side=tk.LEFT)
username_button = tk.Button(username_frame, text="Join", font=BUTTON_FONT, bg=Plum2, fg=Black, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

# Middle frame
middle_frame = tk.Frame(root, width=600, height=400, bg=Cornsilk1)
middle_frame.grid(row=2, column=0, sticky=tk.NSEW)
message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=Plum2, fg=Black, width=68, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(padx=10, pady=10)

# Bottom frame
bottom_frame = tk.Frame(root, width=600, height=50, bg=Mistyrose2)
bottom_frame.grid(row=3, column=0, sticky=tk.NSEW)
recipient_label = tk.Label(bottom_frame, text="To:", font=FONT, bg=Mistyrose2)
recipient_label.pack(side=tk.LEFT, padx=5)
recipient_textbox = tk.Entry(bottom_frame, font=FONT, bg=Mistyrose4, fg=Black, width=10)
recipient_textbox.pack(side=tk.LEFT, padx=5)
message_label = tk.Label(bottom_frame, text="Message:", font=FONT, bg=Mistyrose2)
message_label.pack(side=tk.LEFT, padx=5)
message_textbox = tk.Entry(bottom_frame, font=FONT, bg=Mistyrose4, fg=Black, width=15)
message_textbox.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=Plum2, fg=Black, command=send_message)
send_button.pack(side=tk.LEFT, padx=5)


# Start the GUI
root.mainloop()

           
