# BLOCKCHAIN PROTOCOL-TEAM-H 

The goal of the project is to implement a blockchain peer-to-peer system inspired by Bitcoin, but different.

**BLOCKCHAIN NOMENCLATURE**
1. Block is denoted as Cheese and Blockchain as Cheese Stack.
2. Every cheese has the following items -
      1. Index
      2. Time Stamp
      3. Transaction List
            1. All transactions are stored in a JSON object.
            2. It has the following attributes -
                  1. Sender
                  2. Receiver
                  3. Amount
                  4. Signature
                  5. Miner name
                  6. Miner reward
      4. Nonce
      5. Essence
      6. Essence of previous Cheese
3. ReblochonCheese is the genesis block.

-------------------------------------------------------------------------------------------
**NETWORK**
1. The Blockchain network has tracker and miners.
2. Tracker is a server which contains the list of miners (with IP address and Port number)
3. Miners can communicate with the tracker for the list of members in the network.
4. The transactions are synchronized between the miners.

**Connection**
1. Miner requests to connect to the tracker and can also ask for miner list.
2. A miner generating cheese should broadcast to other miners.
3. If there is a conflict between two Cheese indices, then the miner can add the cheese to his stack or request for the full Cheese Stack.

**Cheese  Validation**
1. We validate the Cheese to decide whether to accept it or not.
2. We check the following:
      1. If the nonce is giving the essence starting with "0000".
      2. Previous essence match.
      3. Order of the index of new cheese.

**Mining**
1. Miners work to find the nonce to generate the essence starting with "000". (proof of work)
2. Once approved, he adds it to the longest cheese stack he has and broadcasts it to the network.
3. The reward is added in the transaction list in the new cheese with his name.
4. Miners collect the new transactions that are broadcasted and they verify transaction by using the digital signature and public keys.
5. Once verified, every miner updates his cheese stack.
6. Miners can request other miners for the updated cheese stack.

**Diagram for the Blockchain architecture**
<img src=https://github.com/UJM-INFO/2020-net-h/blob/anindamaulik/Untitled2.jpg>

1. The idea is to have a tracker and three peers for simulating basic Blockchain working.
2. The peers connect to the tracker first and then they are interconnected to eachother.
3. After the connection has been established between the three peers, a random transaction is generated.
4. This transaction is sent to all the peers and they start the mining process.
5. The peer who mines first, broadcasts it to the system and it is added to the blockchain.

#### Note - The number of peers can be increased as per requirement. The same code of the "peer1.py" can be used but the only thing need to be modified is the port number of the connection and the IP address. The working of the network is similar with any number of peers used.
