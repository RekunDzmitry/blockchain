import logging
from tokenize import Double

from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    Float,
    String,
    Date,
    DateTime,
    ForeignKey,
    event,
)
from sqlalchemy.orm import mapper, relationship

from blockchain.domain import model

logger = logging.getLogger(__name__)

metadata = MetaData()

transactions = Table(
    "transactions",
    metadata,
    Column("id",String(255)),
    Column("sender",String(255)),
    Column("recipient",String(255)),
    Column("amount", Float, nullable=False, server_default="0"),
)

blocks = Table(
    "blocks",
    metadata,
    Column("id",String(255)),
    Column("index",String(255)),
    Column("timestamp",DateTime),
    Column("proof",Integer),
    Column("previous_hash",String(255)),
    Column("transaction_id",ForeignKey("transactions.id")),
)

chain = Table(
    "chain",
    metadata,
    Column("id",String(255)),
    Column("block_id",ForeignKey("blocks.id")),
)