def minHeightBst(array):
    mid = (len(array) - 1) // 2

    if len(array) == 0:
        return
        
    node = BST(array[mid])

    node.left = minHeightBst(array[:mid])
    node.right = minHeightBst(array[mid + 1:])

    return node

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
