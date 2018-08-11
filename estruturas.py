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

y = Pilha(2)
y.push(1)
y.push(2)
print y.isFull()
print y.getArray()
y.pop()
print y.isFull()
y.push(55)
print y.getArray()
