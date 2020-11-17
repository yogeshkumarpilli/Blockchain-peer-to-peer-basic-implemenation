# 2020-net-h
# Blockchain peer-to-peer network basic implementation.

### To implement, the following codes should be run in order -
#### 1. Tracker.py
#### 2. Peer1.py
#### 3. Peer2.py
#### 4. Peer3.py

## Process
### 1. As soon as the peer files and tracker file  are run, the connection to the tracker is established automatically.

<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Tracker%20output.JPG">

### 2. Then a GUI window appears for each peer as shown below -

<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/peer.JPG">

### 3. Click on "peer list" box in all the peer GUIs to request for the list of peers from the tracker.Showing only peer1 as other two are similar to peer1

- Peer1 Output console 
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer1%20output%20before%20connecting%20to%20peers.JPG">

### 4. Then, click on "connect peers" box in all GUIs to get the connection between all peers.
- Peer1 Output Console
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer1%20output%20after%20clicking%20on%20peerlist.JPG">

- Peer2 Output Console
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer2%20output%20after%20clicking%20on%20peerlist.JPG">

- Peer3 Output Console
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer3%20output%20after%20clicking%20on%20peerlist.JPG">

### 5. Now, all the peers are interconnected to each other.

- Peer1 Output Console after interconnection
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer1%20connected%20with%20other%20peers.JPG">

- Peer2 Output Console after interconnection
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer2%20connected%20with%20other%20peers.JPG">

- Peer3 Output Console after interconnection
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer3%20connected%20with%20other%20peers.JPG">

### 6. There is a box with title "create transaction" in every peer GUI. Using this we can generate random transactions and send it to all the other peers. Then, every peer tries to mine using the transaction and whichever peer mines first will get a reward.

- Peer1 has created transaction and its displayed in peer1.py output console
<img src ="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer1%20when%20create%20the%20transactions.JPG">

- Peer2 has received transaction and its displayed in peer2.py output console
<img src ="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer2%20Receives%20Transaction.JPG">

- Peer3 has received transaction and its displayed in peer3.py output console
<img src ="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer3%20Receives%20the%20transaction.JPG">

### 7. The message will be shown in terminal as "cheese mined" and broadcasted to all peers.

- This shows new cheese is added in other peers
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer1%20CheeseMining%20Process.JPG">

- This shows new cheese is minied in this peer
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer2%20Cheese%20mining%20process.JPG">

- This shows new cheese is added in other peers
<img src="https://github.com/UJM-INFO/2020-net-h/blob/master/images/Peer3%20Cheese%20Mining%20Process.JPG">

### 8. The existing cheeseblock can anytime be requested by clicking on "show cheese stack" box.

- Cheese Stack is shown in all the peers. We have taken only one cheese stack output here

<img src= "https://github.com/UJM-INFO/2020-net-h/blob/master/images/CheeseStack.JPG">

### 9. Note - All the results are displayed in the terminal of corresponding peer code. This feature has not been added in the GUI.

## References:
- Bitcoin: A Peer-to-Peer Electronic Cash System "https://bitcoin.org/bitcoin.pdf"
- BlockChain and Networking "https://www.rad.com/blog/blockchain-and-networking"
- Bitcoin network "https://en.wikipedia.org/wiki/Bitcoin_network"
- Develop a blockchain application from scratch in Python "https://developer.ibm.com/technologies/blockchain/tutorials/develop-a-blockchain-application-from-scratch-in-python/"
- Socket Programming Documentation https://docs.python.org/2/library/socket.html
- Threading Documentation - https://docs.python.org/2/library/threading.html
- Udemy course - https://www.udemy.com/course/network-socket-programming-in-python-3-practical-way-r/
- Git reference - https://github.com/Elvin-Arrow/Blockchain-on-sockets/blob/master/server.py
- https://github.com/emrekaragozoglu/blockchain-python
