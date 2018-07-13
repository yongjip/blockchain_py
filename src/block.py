"""
File: block.py
Author: dan
Email: elastic7327@email.com
Github: https://github.com/elastic7327
Description: a block module
"""

from hashlib import sha256
import json
import time


class Block:

    """Docstring for Block. """

    def __init__(self, index, transactions, timestamp, previous_hash):
        """TODO: to be defined1.

        :index: TODO
        :transactions: TODO
        :timestamp: TODO

        """
        self._index = []
        self._transactions = transactions
        self._timestamp = timestamp
        self._previous_hash = previous_hash

    def compute_hash(self):
        """TODO: Docstring for compute_hash.
        :returns: TODO

        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class BlockChain(object):

    """Docstring for BlockChain. """

    # difficulty of Pow algorithm

    difficulty = 2

    def __init__(self):
        """TODO: to be defined1. """

        self.unconfirmed_transactions = []  # data yet to get into blockchain
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """TODO: Docstring for create_genesis_block.
        A function to generate genesis block and appends it to
        the chain. the block has index 0, previous_hash as 0, and
        a valid hash
        :returns: TODO

        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        """docstring for last_block"""
        return self.chain[-1]
