import socket
import sys
import pyDes

# Create a socket for the server with the standard parameters.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get the local host name and create a port number to bind with the server socket.
host = socket.gethostname()
port = 1234
server_socket.bind((host,port))
# Giving the server its name for the chat.
name = "Server"
print("")
print("Server is waiting for incoming connections.....\n")
# Server is listening for a socket, in this case only one socket. 
server_socket.listen(1)
# Accept the connection to client and get it's name.
client_connection, addr = server_socket.accept()
print("Recieved connection\n")
s_name = client_connection.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")
# Send client the server's name.
client_connection.send(name.encode())

# Open the text file containing the shared DES Key and store as a string variable.
with open("des_key.txt","r") as f:
        des_key = f.read()
# Make sure that the key has 8 characters and store it to variable 'k'
k = pyDes.des(des_key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

connection = True
# While connection is True.
while connection:
        # Get the receiving encrypted message from client.
        recv_message = client_connection.recv(1024)
        # Decrypt the message from client with the shared DES key.
        decrypted_message = k.decrypt(recv_message).decode("utf-8")

        # Since received message from client is encrypted as a byte object,
        # Python doesn't allow it to be decoded.
        print("***********************\n") 
        print(f"Received ciphertext is (in byte object): {recv_message}")
        print("Received plaintext is: " + decrypted_message)
        print("***********************\n")

        message = input(str("Please enter your message: "))
        str_message = message
        message = message.encode()
        # Encrypt the server's message to client using the shared DES key.
        encrypted_message = k.encrypt(message)
        client_connection.send(encrypted_message)

        print("***********************\nKey is: " + des_key)
        print("Sent plaintext is: " + str_message) 
        print(f"Sent ciphertext is (in byte object): {encrypted_message}")
        print("***********************\n")