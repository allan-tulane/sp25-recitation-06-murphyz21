def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    ###TODO
    # base case
    if n == 0:
        return 0
    # base case
    elif n == 1:
        return 1
    # recursive call and counts function update
    else:
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    
    
def fib_top_down(n, fibs):
    ###TODO
    # checking if it's already computed
    if fibs[n] != -1:
        return fibs[n]
    # Base case
    if n == 0:
        fibs[0] = 0
        # base case
    elif n == 1:
        fibs[1] = 1

        # recursive call
    else:
        fibs[n] = fib_top_down(n - 1, fibs) + fib_top_down(n - 2, fibs)
    return fibs[n]


def fib_bottom_up(n):
    ###TODO
    # base case
    if n == 0:
        return 0
    # starting a list for fib numbers
    fibs = [0] * (n + 1)
    # base case
    fibs[0] = 0
    # base case
    fibs[1] = 1
    # iteratvely getting fib numbers
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]




