class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, sum = 0, sums = []):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums
    
def calculateBranchSum(node, currSum, sums):
    if node is None:
        return 

    currSum += node.value

    if node.left is None and node.right is None:
        sums.append(currSum)

    calculateBranchSum(node.left, currSum, sums)
    calculateBranchSum(node.right, currSum, sums)
    