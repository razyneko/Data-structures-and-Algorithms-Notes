                                                        # Linkedlist Cycle 

# Problem Link: https://leetcode.com/problems/linked-list-cycle/description/
# How to find if a cycle / loop is present in LinkedList
    # Floyd's Tortoise and Hare Algo / Fast and Slow Pointer Algo
    # TC -> O(n) SC -> O(1)
    # YT Link : https://youtu.be/70tx7KcMROc?si=uxmNGQr2qWIcNsoY&t=2772
    # Alternate using hashmap

def hasCycle(head):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False

# Follow Up - Find length of the cycle
    # Keep counting from where slow and fast meet at first now just keep moving slow until it reaches fast again

                                                        # Linkedlist Cycle 2

# Problem Link : https://leetcode.com/problems/linked-list-cycle-ii/
# Solution Link : https://youtu.be/70tx7KcMROc?si=uchFobf8tyIFP-oc&t=3882
    # after finding where they meet create two new f and s and keep looping and s.next until length become 0 
    # and then move f until f and s are equal return that node

    # OR

    # just after slow and fast meet just slow = head and then traverse slow.next and fast.next until they reach the same node then return any of them
    # edgecase if length of loop == 0 return None                                                       


                                                        # Happy Number

# While theoretically, the process could involve up to 243 iterations to explore all possible sums below 243, in practice, it is guaranteed that any number will determine if it's happy or not in fewer than 20 iterations.
# Hashmap , Hashset and the concept of fast and slow pointer can be used

class Solution:
    def sum_of_square_of_digits(self, val):
        return sum(int(d)**2 for d in str(val))

    def isHappy(self, n: int) -> bool:
        s = n  # slow pointer
        f = n  # fast pointer

        while True:
            s = self.sum_of_square_of_digits(s)  # slow pointer moves one step
            f = self.sum_of_square_of_digits(self.sum_of_square_of_digits(f))  # fast pointer moves two steps

            if f == 1:  # if fast pointer reaches 1, it's a happy number
                return True
            if s == f:  # if slow pointer meets fast pointer, there's a cycle
                break

        return False  # cycle detected, not a happy number

# The fast pointer moves more quickly and will "visit" all values the slow pointer encounters (including 1) as part of its traversal. If the number is happy, the fast pointer will inevitably reach 1 first


# <--------------------------- LinkedList Reverse ----------------------->

# <------- Recursive Approach --------->

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def recursion(self, node, head, tail_wrapper):
#         if node == tail_wrapper[0]:
#             head[0] = tail_wrapper[0]
#             return

#         self.recursion(node.next, head, tail_wrapper)

#         # Reverse pointers
#         tail_wrapper[0].next = node
#         tail_wrapper[0] = node
#         tail_wrapper[0].next = None

#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return head

#         tail = head
#         while tail.next:
#             tail = tail.next

#         # Wrap head and tail in a list to allow modifications
#         head_wrapper = [head]
#         tail_wrapper = [tail]

#         self.recursion(head, head_wrapper, tail_wrapper)

#         return head_wrapper[0]


# Problem if i dont use list wrappers here -->

# The issue lies in the way Python handles variables when passed to a function. In Python, when you
# pass an object (like a ListNode) to a function, the function gets a reference to that object. If
# you modify the object itself (e.g., changing its attributes), those changes persist. However, if 
# you reassign the variable (like tail = node), it only affects the local reference in that function 
# and does not reflect outside of it.

# In your recursion function, when you update tail, you are only changing the local reference, and the 
# changes do not propagate back to the caller. Here's how you can fix this:

# <----------- In place Approach ----------->

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return None
        
#         prev = None
#         pres = head
#         next = pres.next

#         while pres is not None:
#             pres.next = prev
#             prev = pres
#             pres = next
#             if next is not None:
#                 next = next.next
        
#         return prev