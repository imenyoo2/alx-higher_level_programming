#!/usr/bin/python3
"""defines class Node"""


class Node:
    """defines a node of a singly lined list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """getter of data private attribute"""
        return self.__data

    @property
    def next_node(self):
        """getter of next_node private attribute"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter of data private attribute"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter of next_node private attribute"""
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initiate a new singly linked list"""
        self.__head = None

    def __str__(self):
        """convert class to string"""
        result = ""
        buffer = self.__head
        while buffer is not None:
            result += str(buffer.data) + "\n"
            buffer = buffer.next_node
        return result[:-1]


    def sorted_insert(self, value):
        """inserts a new node in sorted position"""
        new = Node(value)
        if self.__head == None:
            self.__head = new
        else:
            buffer = self.__head
            if buffer.data >= new.data:
                new.next_node = buffer
                self.__head = new
            else:
                while True:
                    if buffer.next_node is None:
                        buffer.next_node = new
                        break
                    elif buffer.next_node.data >= new.data:
                        new.next_node = buffer.next_node
                        buffer.next_node = new
                        break
                    buffer = buffer.next_node
