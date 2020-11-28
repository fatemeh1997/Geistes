import socket
import threading
from geistes import Geistes


class ClientThread(threading.Thread):
    g = Geistes()
    g.background_music()
    g.first_surface()
    global name_dict
    name_dict = {}

    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAdd = clientAddress
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from: ", clientAddress)
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            name_dict[msg] = self.clientAdd
            print("from ", msg, name_dict[msg])
            self.csocket.send(bytes(msg, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 14200
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
