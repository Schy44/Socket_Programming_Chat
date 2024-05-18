import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 5
active_clients = []  # List of all currently connected users

# Function to listen for incoming messages from a client
def listen_for_messages(client, username):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                final_msg = username + '~' + message
                send_messages_to_all(final_msg)
                add_message(final_msg)
            else:
                print(f"The message sent from client {username} is empty")
        except Exception as e:
            print(f"Error: {e}")
            remove_client(client)
            break
            
# Function to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())        

# Function to send a message to all the clients that are currently connected to the server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    # Server will listen for client message that will contain the username
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} joined the chat"
            send_messages_to_all(prompt_message)
            update_clients_list()
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

# Function to remove a client from the active_clients list
def remove_client(client):
    for i, (username, cli) in enumerate(active_clients):
        if cli == client:
            del active_clients[i]
            break
    update_clients_list()

# Function to start the server
def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        server.listen(LISTENER_LIMIT)
        add_message(f"Server started on {HOST}:{PORT}")
        threading.Thread(target=accept_clients).start()
    except Exception as e:
        messagebox.showerror("Server Error", f"Unable to start server: {e}")

# Function to accept clients
def accept_clients():
    while True:
        try:
            client, address = server.accept()
            add_message(f"Connected to {address[0]}:{address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to stop the server
def stop_server():
    global server
    try:
        server.close()
        add_message("Server stopped")
    except Exception as e:
        messagebox.showerror("Server Error", f"Unable to stop server: {e}")

# Function to add message to the message box
def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

# Function to update the list of connected clients
def update_clients_list():
    clients_listbox.delete(0, tk.END)
    for username, client in active_clients:
        clients_listbox.insert(tk.END, username)

# GUI Setup
root = tk.Tk()
root.title("Chat Server")
root.geometry("600x400")

# Frames
left_frame = tk.Frame(root, width=200, bg='#E8E8E8')
left_frame.pack(side=tk.LEFT, fill=tk.Y)
right_frame = tk.Frame(root, width=400, bg='#D8D8D8')
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Left Frame
start_button = tk.Button(left_frame, text="Start Server", command=start_server)
start_button.pack(pady=10)
stop_button = tk.Button(left_frame, text="Stop Server", command=stop_server)
stop_button.pack(pady=10)

clients_label = tk.Label(left_frame, text="Connected Clients")
clients_label.pack(pady=10)
clients_listbox = tk.Listbox(left_frame)
clients_listbox.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

# Right Frame
message_box = scrolledtext.ScrolledText(right_frame, state=tk.DISABLED, height=20)
message_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Start the GUI
root.mainloop()
