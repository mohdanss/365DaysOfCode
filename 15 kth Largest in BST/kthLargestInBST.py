# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    visitedNodes = []
    reverseInOrder(tree, k, visitedNodes)
    return visitedNodes[k - 1]

def reverseInOrder(node, k, visitedNodes):
    if node is None or len(visitedNodes) >= k:
        return
    
    reverseInOrder(node.right, k, visitedNodes)
    if len(visitedNodes) < k:
        visitedNodes.append(node.value)
        reverseInOrder(node.left, k, visitedNodes)
