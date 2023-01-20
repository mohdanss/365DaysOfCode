def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree

    while currentNode is not None:
        if abs(currentNode - target) < abs(closest - target):
            closest = currentNode.value

        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
        
    return closest

    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
