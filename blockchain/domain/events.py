from dataclasses import dataclass
from model import Transaction

class Event:
    pass


@dataclass
class TransactionAdded(Event):
    transaction: Transaction


@dataclass
class TransactionAborted(Event):
    transaction: Transaction

