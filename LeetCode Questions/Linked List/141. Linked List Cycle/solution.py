'''
    Explanation I: Using hashmaps


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None):
            return False
        
        slow = head
        fast = head
        
        while True:
            if(fast == None or fast.next == None):
                return False
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
            
        return True