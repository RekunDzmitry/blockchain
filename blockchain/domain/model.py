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
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def add_transaction(self, transaction:Transaction) -> None:
        self.transactions.append(transaction)

    @property
    def hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


class Miner:
    def __init__(self, last_proof:int):
        self.last_proof = last_proof

    def find_proof(self) -> int:
        proof = 0
        while self.valid_proof(proof) is False:
            proof +=1

        return proof

    def valid_proof(self, proof) -> bool:
        guess = f'{self.last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000" 


class Chain:
    def __init__(self, blocks:List[Block]):
        self.blocks =blocks

    def add_block(self, block:Block):
        self.blocks.append(block)

    @property
    def last_block(self) -> Block:
        return self.blocks[-1]