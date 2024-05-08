# Import required modules
"""import socket
import threading

HOST ='127.0.0.1'
PORT = 1234
LISTENER_LIMIT = 5
# Main function
def main():
    #creating the socket class object
    #AF_INET: we are going to use IPv4 addresses
    #SOCK_STREAM: we are going to use TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # creating a try socket catch block
    try:
        # binding the socket to the host and port
        #Provide the server with an address in the form of host IP and Port
        server.bind((HOST, PORT))
        print (f"Running the server on {HOST} {PORT}")
    except:
        print("Unable to bind to host (HOST) and port (PORT)")
        # set server limit
        server.listen()
        
        #This while loop will keep listening to client connections
        while 1:
            client, address = server.accept
            print ("Successfully Connected to Client {address[0]} {address[1]}")
        
    if __name__ == '__main__':
    main()"""
    
"""import socket


HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 5
active_client = [] #List of all active clients

# function to listen for incoming messages from a client
def listen_for_messages(client, username):
    # Function body

    while True:
        message = client.recv(2048).decode('utf-8')
        if message !='':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"Client{username} message is empty")
    
 #funtion to send message to a single client  
def send_messages_to_all(client, message):
    client.sendall(message.encode())

# Function to send any new messages to all the clients that
# are currently connected to the server
def send_messages_to_all(from_username, message):
    for user in active_client:
        send_message_to_client(user[1], message)
        


#Function to handle client
def client_handler(client):
    # Server will listen for client message that will
    # Contain the username
    while True:
        username = client.recv(2048).decode('utf-8')
        if  username != '':
            active_client.append((username, client))
            prompt_message = "SERVER~" + f"(username) added to the chat"
            send_messages_to_all(prompt_message)
        break
        else:
    print("Client username is empty")
            
    threading.Thread(target=listen_for_messages, args=(client,username, )).start()
    
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        #set server limit
        server.listen()
        print(f"Running the server on {HOST}:{PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}: {e}")
        return

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]}:{address[1]}")
        threading.Thread(target=client_handler, args=(client, )).start()
if __name__ == '__main__':
    main()"""
    
"""import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 5
active_client = []  # List of all active clients

# Function to listen for incoming messages from a client
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"Client {username} message is empty")

# Function to send message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to send any new messages to all the clients that are currently connected to the server
def send_messages_to_all(from_username, message):
    for user in active_client:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    while True:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_client.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Running the server on {HOST}:{PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}: {e}")
        return

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]}:{address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()"""




import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
LISTENER_LIMIT = 5
active_clients = []  # List of all currently connected users

# Function to listen for incoming messages from a client
def listen_for_messages(client, username):
    while True:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from client {username} is empty")

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
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

# Main function
def main():
    # Creating the socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except Exception as e:
        print(f"Unable to bind to host {HOST} and port {PORT}: {e}")
        return

    server.listen(LISTENER_LIMIT)

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()
