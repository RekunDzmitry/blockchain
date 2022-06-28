import time
import pytest

from blockchain.domain.model import (
    MasterNode, 
    Node, 
    Transaction, 
    User, 
    Chain, 
    Block
)


class TestModel:
    @pytest.fixture(scope = 'function', autouse =True)
    def setup_data(self):
        self.user1 = User(name = 'Test User 1', balance = 100, id = 'aaa')
        self.user2 = User(name = 'Test User 2', balance = 100, id = 'bbb')

        self.transaction1 = Transaction(
            sender = self.user1, 
            recipient = self.user2, 
            amount = 50
        )
        self.transaction2 = Transaction(
            sender = self.user2, 
            recipient = self.user1, 
            amount = 50
        )

        self.block1 = Block(
            hash = 'aaa', 
            previous_hash = 'aa', 
            transactions = [self.transaction1]
        )
        self.block2 = Block(
            hash = 'aaa', 
            previous_hash = 'aa', 
            transactions = [self.transaction2]
        )

        self.chain1 = Chain(blocks = [self.block1, self.block2])
        self.chain2 = Chain(blocks = [self.block1, self.block2])
        self.chain3 = Chain(blocks = [self.block1])

        self.node1 = Node(id = 'node1', chain = self.chain1)
        self.node2 = Node(id = 'node2', chain = self.chain2)
        self.node3 = Node(id = 'node3', chain = self.chain3)

        self.master = MasterNode(
            users = [self.user1, self.user2], 
            nodes = [self.node1, self.node2, self.node3]
        )
    
    def test_register_node_empty_history(self):
        node = Node()
        
        self.master.register_node(node)

        assert len(self.master.nodes) == 4
        for node in self.master.nodes:
            node.chain.blocks == [self.block1, self.block2]

    def test_register_node_reset_history(self):
        node = Node(id = 'node3', chain = Chain(blocks = [self.block2, self.block1]))
        
        self.master.register_node(node)

        assert len(self.master.nodes) == 4
        for node in self.master.nodes:
            node.chain.blocks == [self.block1, self.block2]

    def test_normal_transaction(self):
        transaction = Transaction(sender = self.user1, recipient = self.user2, amount = 10)

        self.master.transfere(transaction)
        
        assert self.user1.balance == 90
        assert self.user1.balance == 110

    def test_unexisted_user_transaction(self):
        fake_user = User(name = 'Fake User', balance = 1000, id = 'aaaa')
        transaction = Transaction(sender = self.user1, recipient = fake_user, amount = 10)

        assert self.user1.balance == 100
        assert self.user1.balance == 100

    def test_negative_balance_transaction(self):
        transaction = Transaction(sender = self.user1, recipient = self.user2, amount = 1000)

        self.master.transfere(transaction)
        
        assert self.user1.balance == 100
        assert self.user1.balance == 100

