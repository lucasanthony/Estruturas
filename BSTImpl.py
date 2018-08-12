# BSTImpl.py

class BSTNode(object):
    def __init__(self, data, left, right, parent):
        self._dada = data
        self._left = left
        self._right = right
        self._parent = parent

    def __init__(self):
        self._data = None
        self._left = None
        self._right = None
        self._parent = None

    def isEmpty(self):
        return self._data == None

    def isLeaf(self):
        return self._data != None and self._left.isEmpty() and self._right.isEmpty()

    def getData(self):
        return self._data

    def setData(self, date):
        self._data = date

    def getLeft(self):
        return self._left

    def setLeft(self, left):
        self._left = left

    def getRight(self):
        return self._right

    def setRight(self, right):
        self._right = right

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent


class BSTImpl(object):
    def __init__(self):
        self._root = BSTNode()

    def getRoot(self):
        return self._root

    def isEmpty(self):
        return self._root.isEmpty()

    def insert(self, element):
        if element != None:
            self.insertAux(self._root, element)

    def insertAux(self, node, element):
        if node.isEmpty():
            node.setData(element)
            node.setLeft(BSTNode())
            node.setRight(BSTNode())

            if node.getParent() == None:
                node.setParent(BSTNode())

            node.getLeft().setParent(node)
            node.getRight().setParent(node)

        else:
            if node.getData() > element:
                self.insertAux(node.getLeft(), element)

            elif node.getData() < element:
                self.insertAux(node.getRight(), element)
