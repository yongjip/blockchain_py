"""
File: test_block.py
Author: Me
Email: yourname@email.com
Github: https://github.com/yourname
Description:
"""

from src.tests.base import TestBaseClass
from src.block import Block, BlockChain


class TestBlockClass(TestBaseClass):

    def test_smoke_test(self):
        """
        Just simple smoke test for importing
        단순 초기 스모크 테스트입니다.
        """
        assert 1 is 1, "Just Small Import Test"

    def test_create_genesis_block_chain(self):
        """
        test create genesis block
        제네시스 블록(초깃값 블록) 을 생성하는 테스트입니다.
        """
        blk = BlockChain()
        blk.create_genesis_block()

        assert len(blk.chain) == 2

    def test_create_genesis_block_and_get_last_block(self):

        blk = BlockChain()
        blk.create_genesis_block()

        assert len(blk.chain) == 2

        assert blk.last_block == blk.chain[-1]
