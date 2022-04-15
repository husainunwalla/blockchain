import hashlib
from itertools import chain
import json

class Block:
    def __init__(self, prev_hash, transactions) -> None:
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.data = '-'.join(transactions) + '-' + prev_hash
        self.hash = hashlib.sha256(self.data.encode()).hexdigest()

class BlockChain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block('Initial', 'Husain Mints 100000 PLTC')

    def get_latest_block(self):
        return self.chain[~0]

    def add_block(self, transactions):
        self.chain.append(Block(self.get_latest_block().hash, transactions))
    
    def display_blockchain(self):
        for block in self.chain:
            print(block.transactions, ' ', block.hash)


t1 = 'Husain Sends 5 PLTC to Bill'
t2 = 'Elon Sends 0.1 PLTC to Steve'
t3 = 'Jeff Sends 99 PLTC to Mark'

myBlockChain = BlockChain()
myBlockChain.add_block(t1)
myBlockChain.add_block(t2)
myBlockChain.add_block(t3)

myBlockChain.display_blockchain()
