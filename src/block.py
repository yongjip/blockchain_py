"""
File: block.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
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

    def __init__(self):
        """TODO: to be defined1. """

        self.unconfirmed_transactions = []  # data yet to get into blockchain
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """TODO: Docstring for create_genesis_block.
        :returns: TODO

        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
