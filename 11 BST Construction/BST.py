class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        currentNode = self

        # traverse till the end - left node
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # if value is found

                # case 1: If it has both children
                if currentNode.left is not None and currentNode.right is not None:
                    # replace it's value with the minimum value in right subtree
                    currentNode.value = currentNode.right.getMinValue()
                    
                    # now delete the node, with minimum value in the right subtree
                    currentNode.right.remove(currentNode.value, currentNode)
                
                # case 2: if there's no parent of the node - the root node
                elif parentNode is None:
                    # Now we'll already checked for two-child scenario, now node will have either left or right child

                    # case 1: if there's only left node
                    if currentNode.left is not None:
                        # replace the value of the node with the value of the left node
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        # replace the value of the node with the value of the right node
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        pass
                # if the node to be deleted, the current node, is the left chhild of the parent, we can just assign currentNode's left ot parent's left
                elif parentNode.left == currentNode:
                    if currentNode.left is not None:
                        parentNode.left = currentNode.left
                    else:
                        parentNode.left = currentNode.right
                elif parentNode.right == currentNode:
                    if currentNode.left is not None:
                        parentNode.right = currentNode.left
                    else:
                        parentNode.right = currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
