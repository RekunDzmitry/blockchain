from dataclasses import dataclass
from model import Block


class Command:
    pass

@dataclass
class InstantiateBlock(Command):
    previous_block:Block

@dataclass
class StartTransaction(Command):
    previous_block:Block

