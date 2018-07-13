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
        """
        TODO: to be defined1.
        """
        self._index = []
        self._transactions = transactions
        self._timestamp = timestamp
        self._previous_hash = previous_hash

    def compute_hash(self):
        """TODO: Docstring for compute_hash.
        :returns: TODO
        해시를 생성합니다.
        """
        print(self.__dict__)
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
        초기 블록을 생성합니다.
        해당 블록은 인덱스가 0 이고, 이전해시값이 0입니다.
        그리고 유효합니다.

        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()

        print(genesis_block.hash)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        """docstring for last_block"""
        return self.chain[-1]

    def proof_of_work(self, block):
        """TODO: Docstring for proof_of_work.
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.

        """
        block.nonce = 0

        computed_hash = block.compute_hash()

        # 개인적으로 이 부분 코드를 보고 얼마나 블록체인이.. 컴퓨팅 파워를 낭비하는 부분인지
        # 알 수 있습니다.
        while not computed_hash.startswith('0' * BlockChain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
            print(computed_hash, block.nonce)

        return computed_hash

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification
        """

        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash())
