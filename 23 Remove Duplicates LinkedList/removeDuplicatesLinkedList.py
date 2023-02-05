class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList

    # loop till the end of linked list
    while currNode.next is not None:
        # if next node has same value
        if currNode.value == currNode.next.value:
                # now we need to delete next node, by simply setting the next of currNode to next->next,
                # but we'll not move the node to next node, becaause there may still be duplicates
                currNode.next = currNode.next.next
        else:
            currNode = currNode.next
    return linkedList

        