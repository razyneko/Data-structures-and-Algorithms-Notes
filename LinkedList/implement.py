# Singly Linked List

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

Head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

Head.next = A
A.next = B
B.next = C

# print(Head)

# Traversing the SLL

# curr = Head

# while curr:
#     print(curr)
#     curr = curr.next

# Display LL - o(n)

def displaySLL(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    return " -> ".join(elements)
# print(displaySLL(Head))

# -----------------------------------------------

# Search for node value  -O(n)

def search(head, value):
    curr = head

    while curr:
        if curr.val == value:
            return True
        curr = curr.next
    return False

# print(search(Head,9))


# Doubly Linked List

class node:

    def __init__(self, val , next= None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev



dlHead = node(1)
a = node(2)
b = node(3)
c = node(4)
dlTail = node(5)

dlHead.next = a
a.prev = dlHead
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = dlTail
dlTail.prev = c

def displayDLL(head, tail, order="regular"):
    if order == "regular":
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
    
        return " <-> ".join(elements)
    elif order == "reverse":
        curr = tail
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.prev
    
        return " <-> ".join(elements)
    else:
        return "Provide correct order name"

# print(displayDLL(dlHead,dlTail, order="regular"))

# Insert at the beggining (Getting new head)

# def insert_at_beggining(head, tail, val):
#     new_head = node(val, next=head)
#     head.prev = new_head
#     return new_head, tail

# OHead, tail = insert_at_beggining(dlHead, dlTail, 10)

# print(displayDLL(OHead, dlTail))

def insert_at_end(tail, val):
    new_tail = node(val)
    new_tail.prev = tail
    tail.next = new_tail

# --------------------------------------------------------------
