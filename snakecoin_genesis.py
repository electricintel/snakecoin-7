import datetime as date
from snakecoin_block import Block

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")
