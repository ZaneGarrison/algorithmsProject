class binaryTree:
    def __init__(self, item=None):
        self.value = item
        self.leftChild = None
        self.rightChild = None

    def setValue(self, v):
        self.value = v

    def getValue(self):
        return self.value

    def setLeftChild(self, child):
        self.leftChild = child

    def getLeftChild(self):
        return self.leftChild

    def setRightChild(self, child):
        self.rightChild = child

    def getRightChild(self):
        return self.rightChild


