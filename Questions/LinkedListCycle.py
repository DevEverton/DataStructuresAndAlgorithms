
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
        	return False
        	
        current = head
        s = set()
        while current.next != None:
        	if current in s:
        		return True
        	else:
        		s.add(current)
        		current = current.next
        return False
        


n0 = ListNode(3)
n1 = ListNode(2)
n2 = ListNode(0)
n3 = ListNode(-4)

n0.next = n1
n1.next = n2
n2.next = n3
#n3.next = n1

sol = Solution()

sol.hasCycle(n0)