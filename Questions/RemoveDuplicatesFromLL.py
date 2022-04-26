class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
    while node.next != None:
        if node.value == node.next.value:
            node.next = node.next.next
        else:
            node = node.next
    return linkedList

