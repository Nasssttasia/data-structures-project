"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
import src
from src.stack import Stack, Node


class TestNode(unittest.TestCase):
    def test_node(self):
        node = Node(1, None)
        self.assertEqual(node.data, 1)
        self.assertEqual(node.next_node, None)

    def test_node_next_node(self):
        node1 = Node(1, None)
        node2 = Node(2, node1)
        self.assertEqual(node2.next_node, node1)
        self.assertEqual(node2.next_node.data, 1)


class TestStack(unittest.TestCase):
    def test_stack_empty(self):
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_stack_push1(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual(stack.top.data, 'data1')

    def test_stack_push2(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

    def test_stack_pop1(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data, 'data1')

    def test_stack_pop2(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(data, 'data2')