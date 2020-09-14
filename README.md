# CIS 3319 Lab 1: Implementation and Application of DES

## By: Parth Patel

### 1) Language and External libraries used:
* Language: Python
* External Libraries: PyDes for DES encryption and decryption.
* Other libraries: Socket library for socket programming and sys
### 2) IDE used:
* IDE: Visual Studio Code (VSCODE)
* Other: Windows Command Line for the socket programming.
### 3) Detailed steps on how to run the code:
* 1) Open two command terminals.
* 2) Then for both terminals, go to the directory that contains server.py, client.py, and des_key.txt.
* 3) For one of the terminals, run the server by typing the command: python server.py.
* 4) For the other terminal, run the client by typing the command: python client.py
* 5) On the client terminal, type a message such as "This is the client." 
     The message is then encrypted using DES and sent to server.
* 6) On the sever terminal, the message is decrypted and prompt will come up to enter a message.
     Type a message such as "This is the server." The message is then encrypted using DES and sent to client.
* 7) Back on client terminal, the message from server is decrypted and a prompt will come up to enter a message.
* 8) This procedure will continously run between server and client until the user is done using the program.
