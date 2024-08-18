from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        
        if list1 is None and list2 is None:
            return None
        if list1 is not None and list2 is None:
            return list1
        if list2 is None and list2 is not None:
            return list2
        
        res = ListNode()
        l1 = list1
        l2 = list2
        aux = res

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                aux.next = ListNode(l1.val)
                l1 = l1.next
            else:
                aux.next = ListNode(l2.val)
                l2 = l2.next
            aux = aux.next
        
        if l1 is not None:
            aux.next = l1
        elif l2 is not None:
            aux.next = l2

        return res.next
    
sol = Solution()
print("Merged Linked Lists:")