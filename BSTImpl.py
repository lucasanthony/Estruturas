# bst.py

import bstNode

NIL = bstNode.BSTNode()

class BSTImpl(object):
    def __init__(self):
        self._root = NIL

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
            node.setLeft(NIL)
            node.setRight(NIL)

            if node.getParent() == None:
                node.setParent(NIL)

            node.getLeft().setParent(node)
            node.getRight().setParent(node)

        else:
            if node.getData() > element:
                self.insertAux(node.getLeft(), element)

            elif node.getData() < element:
                self.insertAux(node.getRight(), element)
