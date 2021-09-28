#!/usr/bin/python3
''' module for SingLinkedList and Node '''


class Node:
    ''' A singly linked list node '''
    def __init__(self, data, next_node=None):
        ''' constructor '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        ''' node's value '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' node's value setter '''
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' next item in the list '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' next item setter '''
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    ''' A linked list that only links forward '''
    __head = None

    def __init(self):
        ''' constructor '''
        pass

    def sorted_insert(self, value):
        ''' inserts a node into a sorted position '''
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
        ''' string representation of the list '''
        node = self.__head
        reprs = ''
        while node is not None:
            reprs += '{:d}\n'.format(node.data)
            node = node.next_node
        return reprs[:-1]
