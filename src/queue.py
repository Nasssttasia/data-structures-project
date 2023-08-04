class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head=None, tail=None):
        """Конструктор класса Queue"""
        self.head = head
        self.tail = tail

    def enqueue(self, data, next_node=None):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, next_node)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass

    def __str__(self):
        value = []
        next_value = self.head
        while next_value:
            value.append(next_value.data)
            next_value = next_value.next_node
        return '\n'.join(value)