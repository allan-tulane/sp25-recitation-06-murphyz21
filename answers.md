# CMPS 2200 Recitation 06
## Answers

**Name:**_____Zoe Murphy____
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**

The recurrence for the recursive fibonacci sequence would be: W(n) = W(n-1) + W(n-2). 
The root is W(n). Then it breaks into W(n-1) and W(n-2). Then each of those branches breaks into two more. The leafs grow rapidly, with each one producing two more leafs, so it's growing exponentially. Therefore the work is O(2^n)

- **3)**

The span is the longest path. fib_recursive(n - 1) is the longer path. The span is S(n) = S(n-1) + 1. 
You can solve this just with basic math, S(n) = (n-1) + 1, so the span is O(n). 

- **4)**

Each recursive call calls on like n-1 and n-2 over and over again. So the counts for the smaller problems are going to rapidly/exponentially increase. 

- **6)** 
Work - each part is only called once since it like stores the values, so it's O(n) time. Fib top down is like only called once since every value i is only calculated once.
Span - goes through the calculation sequentially, one by one, it's also O(n) time. 

- **8)**

fib_bottom_up wll be called a max of two times. 
The work is also O(n), but the span is O(1) because everything is computed independently
