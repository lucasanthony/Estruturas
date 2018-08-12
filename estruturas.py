class Pilha(object):
    def __init__(self, size):
        self._size = size
        self._array = size*[None]
        self._top = -1

    def getArray(self):
        return self._array

    def isEmpty(self):
        return self._top == -1

    def isFull(self):
        return self._top == len(self._array)-1

    def push(self, element):
        if self.isFull():
            print "Pilha Cheia!"
            return()
        self._top += 1
        topo = self._top
        self._array[topo] = element

    def pop(self):
        if self.isEmpty():
            print "Pilha Vazia!"
            return()
        retorno = self._array[self._top]
        self._top -= 1
        return retorno

    def top(self):
        retorno = None
        if not self.isEmpty():
            retorno = self._array[self._top]

        return retorno

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

bst = BSTImpl()
bst.insert(5)
bst.insert(7)
bst.insert(3)
bst.insert(1)
bst.insert(9)

print bst.getRoot().getRight().getParent().getData()
