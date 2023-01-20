class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def validateBst(tree, min=float('-inf'), max=float('inf')):
    if tree is None:
        return True
    
    if tree.value < min or tree.value >= max:
        return False

    return validateBst(tree.left, min, tree.value) and validateBst(tree.right, tree.value, max)