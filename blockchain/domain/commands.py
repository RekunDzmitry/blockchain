from dataclasses import dataclass
from model import Block


class Command:
    pass

@dataclass
class CreateGenesisBlock(Command):
    previous_block:Block

@dataclass
class AddBlock(Command):
    previous_block:Block

@dataclass
class RegisterNode(Command):
    previous_block:Block

@dataclass
class NewTransaction(Command):
    previous_block:Block

@dataclass
class Mine(Command):
    previous_block:Block

