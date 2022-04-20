import hashlib
from itertools import chain
import json
from flask import Flask, jsonify, render_template
import datetime

class Block:
    def __init__(self, index, proof, prev_hash) -> None:
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.proof = proof
        self.prev_hash = prev_hash

class BlockChain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,1,'0')

    def get_latest_block(self):
        return self.chain[~0]

    def add_block(self):
        self.chain.append(Block(len(self.chain) - 1, self.proof_of_work(self.chain[~0].proof), self.hash(self.chain[~0])))

    def proof_of_work(self, previous_proof):
          # miners proof submitted
        new_proof = 1
        # status of proof of work
        check_proof = False
        while check_proof is False:
            # problem and algorithm based off the previous proof and new proof
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            # check miners solution to problem, by using miners proof in cryptographic encryption
            # if miners proof results in 4 leading zero's in the hash operation, then:
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                # if miners solution is wrong, give mine another chance until correct
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        data = block.timestamp + str(block.index) + str(block.proof) + block.prev_hash
        return hashlib.sha256(data.encode()).hexdigest()

app = Flask(__name__)
my_block_chain = BlockChain()

@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/mine', methods=['GET'])
def mine():
    my_block_chain.add_block()
    response = {'message' : 'Success', 'index' : my_block_chain.chain[~0].index, 'Timestamp' :my_block_chain.chain[~0].timestamp }
    return jsonify(response), 200

@app.route('/show_chain', methods=['GET'])
def show_chain():
    response = {'chain': my_block_chain.chain,
                'length':len(my_block_chain.chain)}
    return json.dumps(response, default=vars), 200

app.run(host='0.0.0.0', port=5000, debug = True)