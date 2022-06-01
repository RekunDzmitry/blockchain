from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type
from blockchain.domain import commands, events, model
from . import unit_of_work


def validate_transaction():
    pass

def create_transaction(
    cmd: commands.AddTransaction,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        transaction = uow.transactions.get(id = cmd.id)
        if transaction is None:
            model.Block.transactions.append(
                model.Transaction(cmd.id, cmd.sender, cmd.recipient, cmd.amount)
            )
            uow.transactions.add(transaction)
        uow.commit()

def update_chain():
    pass


EVENT_HANDLERS = {
    events.BlockMined: [add_reward_transaction, add_block],
    events.TransactionCreated: [add_transaction],
    events.NodeRegistered: [add_node],
    events.ChainRejected:[replace_chain],
    events.ChainRApproved:[approve_chain]
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.Mine: find_proof,
    commands.NewTransaction: create_transaction,
    commands.RegisterNode: register_node,
    commands.RegisterNode: resolve_conflicts,
}  # type: Dict[Type[commands.Command], Callable]
