from socket import *
serverPort = 13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind( ('',serverPort) )
serverSocket.listen(1)
print('O servidor esta pronto para receber')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.
    encode())
    connectionSocket.close()