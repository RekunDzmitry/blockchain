from dataclasses import dataclass
from model import Transaction

class Event:
    pass


@dataclass
class TransactionStarted(Event):
    transaction: Transaction

