# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/16/2022
# Description:


class Node:
    """___"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """___"""

    def __init__(self):
        """___"""
        self._head = None


    def get_head(self):
        """____"""
        return self._head


    def add(self, val):
        """___"""
        new_node = Node(val)

        if self._head is None:
            self._head = new_node
        else:
            tail = self.rec_add(self._head)
            tail.next = new_node

    def rec_add(self, node):
        """___"""
        if node.next is not None:
            return self.rec_add(node.next)
        else:
            return node


    def remove(self, val):
        """___"""
        if self._head is None:
            return
        elif self._head.data == val:
            self._head = self._head.next
        else:
            self.rec_remove(self._head.next, self._head, val)

    def rec_remove(self, node, prev, val):
        """___"""
        if node.data == val:
            if node.next is None:
                prev.next = None
            else:
                prev.next = node.next
        elif node.next is not None:
            self.rec_remove(node.next, node, val)


    def contains(self, val):
        """___"""
        if self._head is None:
            return
        else:
            self.rec_remove(self._head, val)

    def rec_contains(self, node, val):
        """___"""
        if node.data == val:
            return True
        elif node.next is not None:
            self.rec_contains(node.next, val)
        else:
            return False


    def insert(self, val, pos):
        """___"""
        new_node = Node(val)

        if pos == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            self.rec_insert(self._head.next, self._head, val, pos-1)

    def rec_insert(self, node, prev, val, pos):
        """___"""
        if pos == 0:
            new_node = Node(val)
            new_node.next = node
            prev.next = new_node
        elif node.next is not None:
            self.rec_insert(node.next, node, val, pos-1)
        else:
            new_node = Node(val)
            prev.next = new_node


    def reverse(self):
        """___"""
        if self._head is None:
            return
        else:
            self.rec_reverse(self._head, None)

    def rec_reverse(self, node, prev):
        """___"""
        if node.next is not None:
            self.rec_reverse(node.next, node)
        else:
            self._head = node

        node.next = prev


    def to_plain_list(self):
        """___"""
        plain_list = []

        if self._head is None:
            return plain_list
        else:
            self.rec_to_plain_list(self._head, plain_list)
        return plain_list

    def rec_to_plain_list(self, node, list):
        """___"""
        list.append(node.data)
        if node.next is not None:
            self.rec_to_plain_list(node.next, list)
