from copy import deepcopy


class LinkedList:
    def __create(self, head, tail, length):
        self.h = head
        self.t = tail
        self.length = length
        return self

    def __copy(self, other):
        self.h = other.h
        self.t = other.t
        self.length = other.length

    def __init__(self, value=None):
        self.h = value
        self.t = None
        self.length = 0

    def __len__(self):
        return self.length

    def head(self):
        return self.h

    def tail(self):
        return self.t

    def get(self):
        return self.h, self.t

    def insert(self, value):
        if value is None:
            raise TypeError()

        if self.t is None:
            self.t = LinkedList(self.h)
        else:
            newTail = LinkedList()
            self.t = newTail.__create(self.h, self.t, self.length)
        self.h = value
        self.length += 1

    def pop(self):
        if self.length <= 0:
            return None
        else:
            head = self.h
            self.__copy(self.t)
            return head

    def contains(self, elem):
        if elem is None:
            return False

        if self.h == elem:
            return True
        else:
            return self.t.contains(elem)

    def delete(self, elem):
        if elem is None:
            return None
        else:
            self.__copy(self.__deleteAux(elem))

    def __deleteAux(self, elem):
        if self.h is None:
            return self
        elif self.h == elem:
            return self.t
        else:
            tail = self.t.__deleteAux(elem)
            return self.t.__create(self.h, tail, tail.length + 1)

    def __repr__(self):
        if self.h is None:
            return "()"
        else:
            return "(" + str(self.h) + ", " + self.t.__repr__() + ")"
