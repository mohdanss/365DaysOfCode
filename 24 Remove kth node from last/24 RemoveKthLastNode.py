# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    currNode = head
    prevToTarget = head

    while currNode is not None:
        currNode = currNode.next
        if k < 0:
            prevToTarget = prevToTarget.next
        k -= 1
    
    if k >= 0:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prevToTarget.next = prevToTarget.next.next

'''
Explanation:
    - We use two pointers, one to traverse the list and the other to keep track of the node before the target node.
    - We traverse the list until the current node is None.
    - We decrement k every time we traverse the list.
    - When k is less than 0, we move the prevToTarget pointer to the next node.
    - When k is 0, we have reached the target node.
    - If k is greater than 0, we have to remove the head node, because the target node is the head node OR the k value is greater than the length of the list.
    - If k is less than 0, we remove the target node by setting the next pointer of the prevToTarget node to the next node of the target node.
'''
