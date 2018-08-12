import BSTImpl

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

bst = BSTImpl.BSTImpl()
bst.insert(5)
bst.insert(7)
bst.insert(3)
bst.insert(1)
bst.insert(9)

print bst.getRoot().getRight().getParent().getData()
