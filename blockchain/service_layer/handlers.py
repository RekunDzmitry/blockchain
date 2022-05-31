from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type
from blockchain.domain import commands, events, model
from . import unit_of_work


def validate_transaction():
    pass

def add_transaction(
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


EVENT_HANDLERS = {
    events.TransactionValid: [add_transaction],
    events.OutOfStock: [send_out_of_stock_notification],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.ValidateTransaction: validate_transaction,
    commands.CreateBatch: add_batch,
    commands.ChangeBatchQuantity: change_batch_quantity,
}  # type: Dict[Type[commands.Command], Callable]
