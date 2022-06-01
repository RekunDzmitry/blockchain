import hashlib
from typing import List
import json

class User:
    pass

class Transaction:
    def __init__(self, id:str, sender:User, recipient:User, amount:int):
        self.id = id
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

class Block:
    def __init__(
        self, id:str, index:int, timestamp:float, transactions: List[Transaction], 
        proof:int, previous_hash: str
    ):
        self.index = index
        self.timestamp = timestamp
        self._transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def add_transaction(self, transaction:Transaction) -> None:
        self._transactions.append(transaction)

    @property
    def hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Chain:
    def __init__(self, blocks:List[Block]):
        self._blocks = blocks

    def add_block(self, block:Block):
        self._blocks.append(block)

    @property
    def last_block(self) -> Block:
        return self._blocks[-1]


class Blockchain:
    def __init__(self, chain: Chain , last_proof:int):
        self.last_proof = last_proof

    def proof_of_work(self, last_block):
        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return 

    def find_proof(self) -> int:
        proof = 0
        while self.valid_proof(proof) is False:
            proof +=1

        return proof

    def valid_proof(self, proof) -> bool:
        guess = f'{self.last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000" 

    def valid_chain():
        pass