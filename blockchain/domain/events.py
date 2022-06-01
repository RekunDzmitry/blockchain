from dataclasses import dataclass
from model import Transaction

class Event:
    pass


@dataclass
class TransactionAdded(Event):
    transaction: Transaction

@dataclass
class NodeRegistered(Event):
    transaction: Transaction

@dataclass
class TransactionAborted(Event):
    transaction: Transaction

@dataclass
class BlockAdded(Event):
    transaction: Transaction

@dataclass
class BlockMined(Event):
    transaction: Transaction