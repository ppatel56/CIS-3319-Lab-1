import socket
import sys
import pyDes

# Create a socket for the server with the standard parameters.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get the local host name and create a port number to bind with the server socket.
host = socket.gethostname()
port = 1234
client_socket.connect((host,port))
# Giving the client its name for the chat.
name = "Client"
print(" Connected to chat server")
# Send server the client's name and get the server's name.
client_socket.send(name.encode())
s_name = client_socket.recv(1024)
s_name = s_name.decode()
print("")
print(s_name, "has joined the chat room ")

# Open the text file containing the shared DES Key and store as a string variable.
with open("des_key.txt","r") as f:
    des_key = f.read()
# Make sure that the key has 8 characters and store it to variable 'k'
k = pyDes.des(des_key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

connection = True
# While connection is True.
while connection:
    # Enter a message to be encrypted and sent to server
    message = input(str("Please enter your message: "))
    
    str_message = message
    # The message is first encode as a byte object.
    message = message.encode()
    # Fucntion that encrypts message using the shared DES key.
    encrypted_message = k.encrypt(message)

    client_socket.send(encrypted_message)
    
    # Python doesn't allow the encrypted message to be decoded.
    print("***********************\nKey is: " + des_key)
    print("Sent plaintext is: " + str_message) 
    print(f"Sent ciphertext is (in byte object): {encrypted_message}")
    print("***********************\n")

    # Get the receiving encrypted message from server.
    recv_message = client_socket.recv(1024)
    # Decrypt the message from client with the shared DES key.
    decrypted_message = k.decrypt(recv_message).decode("utf-8")

    print("***********************") 
    print(f"Received ciphertext is (in byte object): {encrypted_message}")
    print("Received plaintext is: " + decrypted_message)
    print("***********************\n")

