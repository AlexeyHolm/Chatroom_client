import socket
import threading
import time

SERVER_HOST = 'IP HAS BEEN REMOVED TEMP'
SERVER_PORT = 5000
separator_token = "<SEP>"

# create the client socket
client_socket = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}")
client_socket.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected to the server.")
time.sleep(1)
print("[*] Verifying")
time.sleep(1)

# prompt the user for a name
name = input("Enter a Username: ")

# send the name to the server
client_socket.send(name.encode())

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'NAME':
                client_socket.send(name.encode())
            else:
                print(message)
        except:
            print("[!] An error occurred.")
            client_socket.close()
            break

def send():
    while True:
        message = input(" ")
        if message.lower() == 'exit':
            client_socket.send(f"{name}{separator_token}has left the chat".encode())
            client_socket.close()
            break
        else:
            client_socket.send(f"{name}{separator_token}{message}".encode())

            # check if user joined or left the chat
            if message.lower() == 'join':
                print(f"{name} has joined the chat.")
            elif message.lower() == 'leave':
                print(f"{name} has left the chat.")
            elif message.lower() == 'you':
                print(f"{name}: {message[3:]}") # print only the message content after 'YOU '

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
