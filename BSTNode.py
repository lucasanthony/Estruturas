# bstNode

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
