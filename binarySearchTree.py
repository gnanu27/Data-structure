class BinarySearchTree():
    class _Node:
        __slots__ = '_element', '_right', '_left' 
        def __init__(self, element, left=None, right=None):
            self._element = element
            self._right = right
            self._left = left
    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, e):
        troot = self._root
        ttroot = None
        while troot:
            ttroot = troot
            if e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right

        node = self._Node(e)

        if self._root:
            if e < ttroot._element:
                ttroot._left = node
            elif e > ttroot._element:
                ttroot._right = node
        else:
             self._root = node

    def search(self, e):
        troot = self._root
        while troot:
            if e < troot._element:
                troot = troot._left
            elif e > troot._element:
                troot = troot._right
            else: 
                return True
        return False

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element)
            self.inorder(troot._right)


B = BinarySearchTree()
B.insert(50)
B.insert(30)
B.insert(40)
B.insert(20)
B.insert(70)
B.insert(60)

B.inorder(B._root)
print( )
print(B.search(30))





