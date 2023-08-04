"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
import src
from src.queue import Queue

class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def enqueue(self):
        self.assertEqual(self.head.enqueue('data1'), 'data1')



