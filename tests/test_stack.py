"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
import src
from src.stack import Stack


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def push(self):
        self.assertEqual(self.stack.push('data1'), 'data1')

    def pop(self):
        self.assertEqual(self.stack.pop(), None)

    def str(self):
        self.assertEqual(self.__str__(), 'data1')