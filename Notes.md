## Can we change the maximum recursion depth (at least in python) ?
- Yes, by using **sys** module we can use `sys.setrecursionlimit('value')`

## Steps to write a Recursive Function :

 ### Step 1 : Identify the recursive case i.e, the flow of problem by breaking it into smaller sub problems.
 ### Step 2 : Set up the base condition for getting out of recursive loop.
 ### Step 3 : Check for unintentional cases where code might fail , such  as constraint on the input. [assert keyword]

## Recursion vs Iteration :
- Iteration is faster than recursion , recursion is used where there is no overhead(both men=mory and space) , it's easy to code but takes up memory and slower , it can be used where time and memory are not concern and problem can be broken into smaller subproblems
