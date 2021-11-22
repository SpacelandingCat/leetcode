# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        l = 0
        a = head
        while a != None:
            l += 1
            a = a.next
        m = math.floor(l / 2)
        i = 0
        a = head
        b = ListNode()
        while i < m:
            i += 1
            c = ListNode(a.val)
            c.next = b
            b = c
            a = a.next
        if l % 2 == 1:
            a = a.next
        while a != None:
            if b.val != a.val:
                return False
            a = a.next
            b = b.next
        return True
        
        
    def isPalindromeExtraSpaseN(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        s1 = ''
        s2 = ''
        s3 = ''
        l = 0
        a = head
        while a != None:
            l += 1
            a = a.next
        m = math.floor(l / 2)
        i = 0
        a = head
        while i < m:
            i += 1
            s1 += str(a.val)
            a = a.next
        if l % 2 == 1:
            a = a.next
        else:
            a = a
        while a != None:
            s2 += str(a.val)
            a = a.next
        l = len(s1)
        i = 0
        while i < l:
            s3 += s1[l-1-i]
            i += 1
        if s2 == s3:
            return True
        return False
        
        
    def isPalindromeWithoutExtraSpace(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        l = 0
        a = head
        while a != None:
            l += 1
            a = a.next
        m = math.floor(l / 2)
        i = 1
        a = head
        while i < m:
            i += 1
            a = a.next
        if l % 2 == 1:
            b = a.next
        else:
            b = a
        while m > 0:
            i = 1
            a = head
            while i < m:
                a = a.next
                i += 1
            b = b.next
            if a.val != b.val:
                return False
            m -= 1
        return True
