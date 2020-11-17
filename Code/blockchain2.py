import hashlib
import json
import datetime
import io
from ecdsa import VerifyingKey, SigningKey, SECP256k1

cheesestack = []
transactionlist = []


# DEFINING CHEESE
def reblochoncheese():
    cheese = {}
    cheese['index'] = 0
    cheese['timestamp'] = str('2020-03-10 09:00:00.000000')
    cheese['transactions'] = []
    cheese['previous_essence'] = ''
    cheese['nonce'], cheese['essence'] = proofofwork(cheese['index'], cheese['timestamp'], cheese['transactions'],
                                                     cheese['previous_essence'])
    return cheese


# HASH FUNCTION
def hash(index, time_stamp, transactions, nonce, reblochonessence):
    return hashlib.sha1(bytes(index) +
                        str(time_stamp).encode('utf-8') +
                        str(transactions).encode('utf-8') +
                        bytes(nonce) +
                        str(reblochonessence).encode('utf-8')).hexdigest()


# PROOF OF WORK
def proofofwork(index, time_stamp, transactions, reblochonessence, event):
    nonce = 0
    hash_zero = False
    while not event.isSet():
        if hash_zero is False:
            nonce += 1
            essence = hash(index, time_stamp, transactions, nonce, reblochonessence)
            if essence.startswith('0000'):
                hash_zero = True
                return nonce, essence
    return -1, -1

# DEFINING PUBLIC AND PRIVATE KEYS
def genkey():
    signing_key = SigningKey.generate(curve=SECP256k1)
    prvstr = signing_key.to_string().hex()
    verkey = signing_key.get_verifying_key()
    pubstr = verkey.to_string().hex()
    return prvstr, pubstr
def signature(message, prvstr):
    private = bytes.fromhex(prvstr)
    signing_key = SigningKey.from_string(private, curve=SECP256k1)
    signature = signing_key.sign(message).hex()
    return signature
def verifytransactionn(message, signature, pubstr):
    public = bytes.fromhex(pubstr)
    verkey = VerifyingKey.from_string(public, curve=SECP256k1)
    return verkey.verify(bytes.fromhex(signature), message)
def newtransaction(pvt, pub, publicrecv, amount):
    mess = publicrecv + str(amount)
    signature1 = signature(mess.encode('utf-8'), pvt)
    details = {'from': pub, 'to': publicrecv, 'amount': amount, 'signature': signature1}
    return details

# MINING
def minecheese(blockchain, transactions, file_path, event):
    index = blockchain[-1]['index'] + 1
    time_stamp = datetime.datetime.now()
    reblochonessence = blockchain[-1]['essence']
    if not event.isSet():
        nonce, essence = proofofwork(index, time_stamp, transactions, reblochonessence, event)
        if nonce == -1 and essence == -1:
            return -1
        cheese = {}
        cheese['index'] = index
        cheese['timestamp'] = str(time_stamp)
        cheese['transactions'] = []
        for trans in transactions:
            cheese['transactions'].append(trans)
        cheese['previous_essence'] = reblochonessence
        cheese['nonce'] = nonce
        cheese['essence'] = essence
        if not event.isSet():
            if validateblock(blockchain[-1], cheese):
                blockchain.append(cheese)
                saveblock(blockchain, file_path)
                return True
            else:
                return False
        else:
            return -1
    else:
        return -1


# VERIFY THE TRANSACTION
def checkwork(trans_lst, details, miner, reward=1):
    mess = str(details['to']) + str(details['amount'])
    valid = verifytransactionn(mess.encode('utf-8'), details['signature'], details['from'])
    if valid:
        details['miner'] = miner
        details['reward'] = reward
        trans_lst.append(details)


# ADDS MINED BLOCK TO THE CHAIN
def addblock(cheesestack, cheese, file_path):
    if validateblock(cheesestack[-1], cheese):
        cheesestack.append(cheese)
        saveblock(cheesestack, file_path)
        return True
    else:
        return False

# ADD RECEIVED BLOCKS FROM PEERS TO THE CHAIN
def add_block(cheesestack, cheeses, file_path):
    changed = False
    for ch in cheeses:
        if validateblock(cheesestack[-1], ch):
            cheesestack.append(ch)
            changed = True
        else:
            break
    if changed:
        saveblock(cheesestack, file_path)


# SAVES BLOCK IN JSON FILE
def saveblock(blockchain, file_name):
    with io.open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(blockchain, ensure_ascii=False))


# LOAD THE BLOCK FROM FILE
def loadblock(file_name):
    with open(file_name) as json_data:
        blocklist = json.load(json_data)
        return blocklist


def validateblock(prevblock, nextblock):
    index = prevblock['index'] + 1
    essence = prevblock['essence']
    new_index = nextblock['index']
    new_time_stamp = nextblock['timestamp']
    newtransactionactions = nextblock['transactions']
    new_reblochonessence = nextblock['previous_essence']
    new_nonce = nextblock['nonce']
    new_essence = nextblock['essence']
    new_hash = hash(new_index, new_time_stamp, newtransactionactions, new_nonce, new_reblochonessence)
    if new_index != index:
        print("error0")
        print(index)
        print(new_index)
        return False
    elif essence != new_reblochonessence:
        print("error1")
        print(essence)
        print(new_reblochonessence)
        return False
    elif new_essence != new_hash:
        print("error2")
        print(new_essence)
        print(new_hash)
        return False
    else:
        return True


def validatechain(received_blocklist):
    i = 0
    length = len(received_blocklist)
    valid = True
    while i <= length - 1 and valid == True:
        valid = validateblock(received_blocklist[i], received_blocklist[i + 1])
        length -= 1
    return valid


