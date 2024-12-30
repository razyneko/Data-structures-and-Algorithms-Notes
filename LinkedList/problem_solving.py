# inserting a value at a particular node index

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = Node(1)
first = Node(2)
second = Node(3)
third = Node(4)
head.next = first
first.next = second
second.next = third

def displayLL(head):
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    
# displayLL(head)
curr = head
def insert_using_recursion(val, index, curr):
    if index == 1:
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        displayLL(head)
        return
    curr = curr.next
    return insert_using_recursion(val, index - 1,curr)

insert_using_recursion(17,2,head)