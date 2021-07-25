'''
    Recursions
    Recursions are naturally something that every programmer needs to know, certainly if writing in Python where the
    Pythonic way of coding is one of elegance and simplicity. The first, though a naive implementation, is an implementation
    of the fibonacci sequence and it is almost the "hello world" of recursive programs. Like with all recursions we need:
    1. A base case
    2. An recursive case
    Every successive recursive call is put on the stack and is systematically worked through. Though simple one has to be
    aware of avoiding huge recursions or in some cases infinite recursions as that will surely give one the error caused
    by a Stack Overflow.
'''



# FIB 1: Naive Recursion
def fibonnaci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

# Fib 2: Memo Recursion
def memoized_fibonacci(n):
    global stored_values
    stored_values = {}
    return rec_fibonacci(n)

def rec_fibonacci(n):
    if (n == 1 or n == 2):
        return 1
    elif stored_values.__contains__(n):
        return stored_values[n]
    else:
        fib = rec_fibonacci(n-1) + rec_fibonacci(n-2)
        stored_values[n] = fib
        return fib

# Fib 3 - Bottom Up Iteration
def bottom_up_fibonacci(n):
    f1 = 1
    f2 = 1
    fn = 2
    i = 3
    while(i < n):
        f1 = f2
        f2 = fn
        fn = f2 + f1
        i += 1

    return fn



# What is the difference between the fibonacci implementations above?
# :---------------------------------------------------------------------------------------------------------------------
''' 
 Fib 1 - Fibonnaci using a simple recursion:
 This is what we muse call a naive_fibonacci, it uses recursion in an irresponsible way, that is, with regards to time
 complexity. For large numbers of n there will be a big overlap and the time complexity will grow in exponential time.

 FIB 2: memoized_fibonacci() - Fibonacci implementation number 2, slightly harder, much better.
 This fibonacci sequence still uses the same recursive structure as does the naive_fibonacci.
 However, it very importantly saves its values into a dictionary called stored_values from which we can with ease
 always extract the value. The drawback is that we get a linear memory complexity, that is O(n), for big n we have
 to save every entry once. When its saved, however, we can access it directly thus making use of having solved that
 subproblem of lesser fibonacci numbers. Fib(8) = 21 = 13 + 8 = (8+5) + (8 = 5 + 3) is such an example. Here we see an
 overlap with 8 and with 5, if we have solved them we can access them in constant time, and as such we can save time
 Instead of the problem being of exponential time it can be of linear time. We have one function that initiates a table
 and then we start the recursion:

 FIB 3: bottom_up_fibonacci()
 This is the hardest but by far best implementation of fibonacci, it makes use of the structure of the problem and work
 from the ground up, avoiding overlap as such, but unlikes FIB 2 also avoids the memory usage. This Fibonacci problem
 is an entry into the world of dynamic programming, that is, a problem where the problem is built upon subproblems and
 in which there is an overlap. The first implementation, FIB 1, that is, makes no attempt at all at exploiting this but
 rather uses a mindless brute force method, and is as such of exponential time complexity. FIB 3 is the fastest of them
 all and uses only constant memory space, Time: O(n), Memory: O(1). The code also is iterative, meaning there will be
 no problem in maximum recursion depths, the code can quickly handle very big fibonacci numbers such as fib(1000000).'''

# :---------------------------------------------------------------------------------------------------------------------

# A faculty function, working the way one expects it to do mathmatically. The faculty is calculated recursively, each
# time a recursive call is placed on the stack for a given n-1, and we multiplicate it with n as one would expect.

def faculty(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n*faculty(n-1)

''' tail_recursive_faculty
    Tail recursion is a thing in recursive functions. What it means is that we never traverse up again, rather we always
    push our work to our tail and once we reach the bottom we return it. In the faculty function above, faculty(n), we 
    go down till we reach n = 1 and then we traverse up again, merging together the factors. In tail_recursice_faculty we
    optimize so that when we reach the bottom we are done. In practice the time complexity is similar to that of iteration.
    Note: In functional languages such as Haskell we do not have iteration and so tail_recursion is the functional answer to
    iteration.
'''
def tail_recursive_faculty(n,packed_mult = 1):
    if(n == 1 or n == 0):
        return packed_mult
    else:
        return tail_recursive_faculty(n-1,packed_mult*n)


# A recursive function that conceptualizes multiplication via addition. Instead of doing the prebuilt multiplication
# algorithm this algorithm simply makes use of addition for as many times as needed for a number, and so we apply the
# factor2 as a term for factor1 times, and if factor1 is negative we first make a sign switch in the outer parenthesis.

def multiplication(factor1,factor2):
    if(factor2 == 1):
        return factor1

    elif factor2 == 0:
        return 0

    elif factor2 > 1:
        return factor1 + multiplication(factor1,factor2-1)

    else: # factor2 negative
        return -(multiplication(factor1, -factor2))

# Returns Levehnstein distance for how far a word W is from being a palindrome:
def how_far_from_palindrome(W):
    sum = 0
    if(len(W) <= 1):
        return sum
    else:
        if(W[0] == W[-1]):
            return how_far_from_palindrome(W[1:-1])
        else:
            return how_far_from_palindrome(W[1:-1]) + 1

def merge_lists(l1,l2):
    if(l1 == []):
        return l2
    else:
        l2.insert(0,l1.pop())
        return merge_lists(l1, l2)
