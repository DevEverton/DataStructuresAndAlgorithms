class Node:
   def __init__(self, val):
      self.val = val
      self.next = None

class MyLinkedList(object):

   def __init__(self, head=None):
        self.head = head

   def printList(self):
      currentNode = self.head
      while currentNode is not None:
         print(currentNode.val)
         currentNode = currentNode.next

   def get(self, index):
      """
      :type index: int
      :rtype: int
      """
      if self.head == None:
         print("It's empty")
         return -1

      curIndex = 0
      curNode = self.head

      while True:
         if curIndex == index:
            print(curNode.val)
            return curNode.val
         else:
            if curNode.next != None:
               curNode = curNode.next
            else:
               print("Index out of range")
               return -1
         curIndex += 1

        

   def addAtHead(self, val):
      """
      :type val: int
      :rtype: None
      """
      node = Node(val)
      if self.head == None:
         self.head = node
      else:
         node.next = self.head
         self.head = node

   def addAtTail(self, val):
      """
      :type val: int
      :rtype: None
      """
      node = Node(val)
      if self.head == None:
         self.head = node
         return None

      currentNode = self.head
      while currentNode is not None:
         if currentNode.next == None:
            currentNode.next = node
            break
         currentNode = currentNode.next


   def addAtIndex(self, index, val):
      """
      :type index: int
      :type val: int
      :rtype: None
      """
      node = Node(val)
      if self.head == None:
         if index == 0:
            self.head = node
         return None

      curIndex = 0
      currentNode = self.head
      if index == 0:
         node.next = self.head
         self.head = node
         return None
      while True:

         if curIndex + 1 == index:
            node.next = currentNode.next
            currentNode.next = node
            break
         currentNode = currentNode.next
         curIndex += 1
         if currentNode == None:
            break

   def deleteAtIndex(self, index):
      """
      :type index: int
      :rtype: None
      """
      if self.head == None:
         return None

      curIndex = 0
      previous = None
      currentNode = self.head

      while True:
         if curIndex == index:
            if previous == None:
               self.head = currentNode.next
               break
            previous.next = currentNode.next
            break
         previous = currentNode
         currentNode = currentNode.next
         curIndex += 1
         if currentNode == None:
            break




myLinkedList = MyLinkedList()
# obj.addAtHead(3)
# obj.addAtHead(7)
# obj.addAtHead(10)
# obj.addAtHead(2)
# obj.addAtTail(9)
# obj.addAtHead(1)
# obj.addAtIndex(6, 33)
# obj.deleteAtIndex(0)
# obj.printList()

myLinkedList.addAtIndex(1,0)

myLinkedList.get(0)



myLinkedList.printList()
