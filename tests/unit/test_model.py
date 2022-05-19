from blockchain.domain.model import User, Block, Transaction, Miner, Chain
import time

def test_block_adds_transaction():
    block = Block(
        index = 1, timestamp = time.time(), transactions = [], 
        proof = 1, previous_hash = 'aaa'
    )

    block.add_transaction(Transaction(User(),User(),1))

    assert len(block.transactions) == 1

def test_chain_adds_block():
    chain = Chain(blocks = [])
    
    block = Block(
        index = 1, timestamp = time.time(), transactions = [], 
        proof = 1, previous_hash = 'aaa'
    )

    chain.add_block(block)

    assert len(chain.blocks) == 1
    assert chain.last_block.index == 1

def test_miner_finds_valid_proof():
    miner = Miner(1)
    proof = miner.find_proof()

    assert miner.valid_proof(proof) == True