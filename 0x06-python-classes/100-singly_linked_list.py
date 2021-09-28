#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    __head = None

    def __init(self):
        pass

    def sorted_insert(self, value):
        node = Node(value)
        if self.__head is None or self.__head.data >= value:
            node.next_node = self.__head
            self.__head = node
            return
        cur = self.__head
        while cur.next_node is not None and cur.next_node.data < value:
            cur = cur.next_node
        node.next_node = cur.next_node
        cur.next_node = node

    def __repr__(self):
        node = self.__head
        reprs = ''
        while node is not None:
            reprs += '{:d}\n'.format(node.data)
            node = node.next_node
        return reprs[:-1]
