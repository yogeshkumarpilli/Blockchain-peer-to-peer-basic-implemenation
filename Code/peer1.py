import socket
import threading
import json
import blockchain2
import queue
from tkinter import *
import random

trackerlist = []
memberlist = []
path = "peer1" + ".json"
memberList = []

def loadCheeses():
    block1.stack = blockchain2.loadblock(path)
    print(block1.stack)

class blocks:
    def __init__(self):
        self.stack = []
        self.received_transactionlist = queue.Queue()
        self.flag = threading.Event()

def connecttracker(address, port):
    def sendmessage(sock):
        while True:
            sock.sendall(bytes(input(""), 'utf-8'))
    def handle(address, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))
        send_clientport(sock)
        trackerlist.append(sock)
        iThread = threading.Thread(target=sendmessage, args=(sock,))
        iThread.daemon = True
        iThread.start()
        while True:
            header = sock.recv(1)
            if not header:
                break
            if header == b'\x01':
                size = int.from_bytes(sock.recv(2), byteorder='big')
                data = sock.recv(size)
            if header == b'\x02':
                size = int.from_bytes(sock.recv(2), byteorder='big')
                data = sock.recv(size)
                for el in json.loads(data):
                    if el not in memberList:
                        memberList.append(el)
                print(memberList)
    def send_clientport(sock):
        encode_message = bytes(str(23456), 'utf-8')
        size = len(encode_message).to_bytes(2, byteorder='big')
        sock.sendall(b'\x01' + size + encode_message)
    t = threading.Thread(target=handle, args=(address, port,))
    return t

def connectserver(address, port):
    connections = []
    peers = []
    def handle(address, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((address, port))
        sock.listen(1)
        while True:
            c, a = sock.accept()
            cThread = threading.Thread(target=handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            connections.append(c)
            peers.append(str(a[0]) + ':' + str(a[1]))
            print(str(a[0]) + ':' + str(a[1]), "connected")
            print("peers: ", peers)
            peerconnection(c)
    def recvall(sock, n):
        data = b''
        while len(data) < n:
            packet = sock.recv(1)
            if not packet:
                return None
            data += packet
        return data
    def handler(c, a):
        while True:
            header = c.recv(1)
            if (header == b'\x07'):
                size = c.recv(2)
                buf = int.from_bytes(size, byteorder='big')
                ch = recvall(c, buf)
                new_cheese = json.loads(ch)
                print(new_cheese)
                if blockchain2.addblock(block1.stack, new_cheese, path):
                    block1.flag.set()
                    print("new cheese added ", new_cheese)
                else:
                    print("new cheese not valid")
            if header == b'\x05':
                header2 = c.recv(1)
                if header2 == b'\x01':
                    blockchain_length = block1.stack[-1]["index"].to_bytes(2, byteorder='big')
                    c.sendall(b'\x05' + b'\x01' + blockchain_length)
                elif header2 == b'\x02':
                    blockchain_length = c.recv(2)
                    index = int.from_bytes(blockchain_length, byteorder='big')
                    cheeses_to_send = []
                    while index <= block1.stack[-1]["index"]:
                        cheeses_to_send.append(block1.stack[index])
                        index += 1
                    cheeses_string = json.dumps(cheeses_to_send)
                    print(cheeses_string)
                    bytes_cheese_string = bytes(cheeses_string, 'utf-8')
                    size = len(bytes_cheese_string)
                    size_bytes = size.to_bytes(2, byteorder='big')
                    c.sendall(b'\x05' + b'\x02' + size_bytes + bytes_cheese_string)
                    print("sent cheeses")
            if header == b'\x08':
                size = c.recv(2)
                buf = int.from_bytes(size, byteorder='big')
                data = c.recv(buf)
                transaction = json.loads(data)
                print("received transaction: ", transaction)
                block1.received_transactionlist.put(transaction)
            if not header:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                connections.remove(c)
                peers.remove(a[0])
                c.close()
                break
    def peerconnection(c):
        message = "Connect to " + "peer1" + " successful"
        encode_message = bytes(message, "utf-8")
        size = len(encode_message)
        size_bytes = size.to_bytes(2, byteorder='big')
        c.sendall(b'\x04' + size_bytes + encode_message)
    t = threading.Thread(target=handle, args=(address, port))
    return t

def connectmember(address, port):
    def handle(address, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, port))
        memberlist.append(sock)
        while True:
            header = sock.recv(1)
            if not header:
                break
            if header == b'\x04':
                size = sock.recv(2)
                size_int = int.from_bytes(size, byteorder='big')
                message = sock.recv(size_int)
                print(str(message, 'utf-8'))
            if header == b'\x05':
                header2 = sock.recv(1)
                if header2 == b'\x01':
                    length = sock.recv(2)
                    length_int = int.from_bytes(length, byteorder='big')

                if header2 == b'\x02':
                    size = sock.recv(2)
                    size = int.from_bytes(size, byteorder='big')
                    data = sock.recv(size)
                    cheeses_received = json.loads(data)
                    print(cheeses_received)
                    blockchain2.add_block(block1.stack, cheeses_received, path)
    t = threading.Thread(target=handle, args=(address, port,))
    return t

def mining():
    def handle():
        tomine = []
        while True:
            while len(tomine) < 3:
                blockchain2.checkwork(tomine, block1.received_transactionlist.get(), "peer1")
            val = blockchain2.minecheese(block1.stack, tomine, path, block1.flag)
            if val is True:
                newmine = json.dumps(block1.stack[-1])
                bytes_newmine = bytes(newmine, 'utf-8')
                size = len(bytes_newmine).to_bytes(2, byteorder='big')
                for s in memberlist:
                    s.sendall(b'\x07' + size + bytes_newmine)
                print("cheese mined", " size: ", len(bytes_newmine), " data: ", bytes_newmine)
            tomine = []
            block1.flag.clear()
    t = threading.Thread(target=handle, args=(), daemon=True)
    return t

def requestmemberlist():
    trackerlist[0].sendall(b'\x02')

def tracker():
    connecttracker('localhost', 5656).start()
    print("Connected to tracker")

def clientconnect1():
    for mem in memberList:
        addr = mem.split(":")
        connectmember(addr[0], int(addr[1])).start()

def show():
    print(str(memberList))

def showcheesestack():
    print("Cheesestack = " + json.dumps(block1.stack))

def test():
    keyss = blockchain2.genkey()
    pvt = keyss[0]
    pub = keyss[1]
    reckeys = blockchain2.genkey()
    recpub = reckeys[1]
    randomm = random.randint(1, 10)
    newtransaction = blockchain2.newtransaction(pvt, pub, recpub, randomm)
    newtransaction_str = json.dumps(newtransaction)
    print(newtransaction_str)
    encode = bytes(newtransaction_str, 'utf-8')
    size = len(encode).to_bytes(2, byteorder='big')
    for sock in memberlist:
        sock.sendall(b'\x08' + size + encode)

connectserver('localhost', 23456).start()
block1 = blocks()
loadCheeses()
mining().start()
tracker()

#tkinter gui
root = Tk()
root.title("Peer 1")
root.minsize(250, 200)
button2 = Button(root,text="Peer list",command = requestmemberlist)
button1 = Button(root,text="connect peers",command = clientconnect1)
button6 = Button(root,text="Create transaction",command=test)
button5 = Button(root,text="show cheese stack",command=showcheesestack)
button2.pack()
button1.pack()
button6.pack()
button5.pack()
root.mainloop()