"""#import requried modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def listen_for_messages_from_server(client):
    while true:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]
            print(f"{username}: {content}")
        else:
            print(f"Message received from client is empty")
        
def send_message_to_server(client):
    while 1:
        message = input("Message: ")
        if message != '':
            client.send(message.encode())
        else:
            print("Message cannot be empty")
            exit(0)
            
            

def communicate_to_server(client):
    username =  input("Enter username:")
    if username != '':
        client.send(username.encode())
    else:
        print("Username cannot be empty")
        exit(0)
    threading.Thread(target=listen_for_messages_from_server,args=(client, )).start()
    send_message_to_server()
    

# main function
def main():
    
    #createing a socket object
    client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
try :
    client.connect((HOST, PORT))
    print ("Successfully connect to server")
except :
        print(f"Unable to connect to server {HOST} {PORT}")
    # send data to the server
    
communicate_to_server(client)
    
    
if __name__ == '__main__':
    main()"""
    
"""import socket

HOST = '127.0.0.1'
PORT = 1234

def communicate_to_server()






def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        # Send data to the server
        client.sendall(b'Hello, server!')
    except ConnectionRefusedError:
        print(f"Connection refused: Check if the server is running on {HOST}:{PORT}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    main()""""""

import socket ooooooooooooooo
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

import sys  # Import sys module for sys.exit


HOST = '127.0.0.1'
PORT = 1234

Mistyrose2 = '#EED5D2'
Cornsilk1 = '#FFF8DC'
Plum2 = '#EEA9A9'
Black = '#000000'
Mistyrose4 = '#8B7D7B'

Button_Font = ("Helvetica",15)
Small_Font = ("Helvetica", 13)

#SOCK_STREAM: we are using TCP Packets for Communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.End, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect(client):
    try:
        client.connect((HOST, PORT))
        print("Successfully connect to server")
        add_message("[SERVER]:Successfully connect to server")
    except Exception as e:  # Capture the exception object to print specific error message
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}: {e}")
        
        
        
        
        sys.exit(0)  # Use sys.exit(0) to exit the program
    print("Button is working")
    
    username = username_textbox.get()
    if username != '':
        client.send(username.encode())
    else:
        message_box.showerror("Invalid username","Username cannot be empty")
        
    
    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()
    
    
def send_message(message):
    while True:  # Infinite loop for continuously sending messages
        message = message_textbox.get()
        if message != '':
            client.send(message.encode())
        else:
            message_box.showerror("Empty message","Message cannot be empty")
            


root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100,bg='mistyrose2')
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg= 'cornsilk1')
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg= 'plum2')
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text=" Enter Username: ", font=("Helvetica", 18), bg='Mistyrose2', fg=Black)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=Button_Font, bg=Mistyrose4, fg=Black, width=21)
username_textbox.pack(side=tk.LEFT)

username_textbox = tk.Entry(top_frame, font=Button_Font, bg=Plum2, fg=Black, width=7)
username_textbox.pack(side=tk.LEFT, padx=15)

username_button = tk.Button(top_frame, text= "Join", font=Button_Font, bg=Plum2, fg=Black, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, font=Button_Font, bg=Mistyrose4, fg=Black, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text= "Send", font=Button_Font, bg=Plum2, fg=Black, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=Small_Font, bg=Plum2, fg=Black, width=68, height=26.5)
message_box.pack(side=tk.TOP, padx=15)

message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)




def listen_for_messages_from_server(client):
    
    while True:  # Fixed capitalization
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]
            add_message(f"{username}: {content}")
            a
        else:
            message_box.showerror("Error","Message received from server is empty")

    
def main():
    
    root.mainloop()
    
if __name__ == '__main__':
    main()"""


# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 1234

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

    # try except block
    try:

        # Connect to the server
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        add_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)

def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=600, height=100, bg=Mistyrose2)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg=Cornsilk1)
middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=Plum2)
bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Enter username:", font=FONT, bg=Mistyrose2, fg=Black)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=Mistyrose4, fg=Black, width=21)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, bg=Plum2, fg=Black, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=Mistyrose4, fg=Black, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=Plum2, fg=Black, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=Plum2, fg=Black, width=68, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


def listen_for_messages_from_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split('~')[1]

            add_message(f"[{username}] {content}")
            
        else:
            messagebox.showerror("Error", "Message recevied from client is empty")

# main function
def main():

    root.mainloop()
    
if __name__ == '__main__':
    main()