# adding an element is *O(1) --- worst --> O(n)
# removing and element *O(1) --- worst --> O(n)



# <----------------- Collision Handling ------------------->

# <-------- Seperate chaining ----------->
# the element with same hash are chained with a linked list

# <-------- Linear Probing ------->
# the element with same hash is put just after the intital value present at that index
# if prevValue is deleted, to traverse to get another ones , use like a placeholder or smth to make sure that it gets iterated