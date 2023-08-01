class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
                Конструктор класса Node

                :param data: данные, которые будут храниться в узле
                """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top  # тут записываешь текущую голову
        new_top = Node(data, next_node)
        self.top = new_top  # здесь в голову записываешь созданную Node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data
