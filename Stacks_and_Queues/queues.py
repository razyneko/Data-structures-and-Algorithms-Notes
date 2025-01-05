# they are based on FIFO 

# these are usually not implemented using lists(dynamic arrays)
# doubly linked list is used for the queue implementation

# because popping from start will be O(n) for lists
# hence doubly linked lists are used

# Enqueue() --- append to queue
# Dequeue() --- pop from start

# .pop() returns removed

# if stk:
#     return True    --->  if stk is not empty

# for queues use 
# from collections import deque
# deque --- double ended queue
# use deque.popleft() for dequeue opn   ---> O(1)  --> implemented as a doubly linked list

# for peek
# q[0] ---from left side
# q[-1] --- from right side