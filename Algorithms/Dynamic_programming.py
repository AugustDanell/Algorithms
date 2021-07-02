'''
    Dynamic Programming:
    Dynamic Programming is a programming technique to find an optimal solution faster than a brute force algorithm. The
    idea is to make use of overlapping subproblems and using already solved subproblems to solve the problem at hand.
    A starting example of this is fibonacci, where it is common to define it using a recursive brute force method, this
    is defined as fib1 in the file 'recursions.py', and it is a top-down approach. It formulates first a base case and then
    uses the following recursive formula: fib(x) = fib(x-1) + fib(x-2). This works but it is very slow with a horrible,
    exponential time complexity and so after values like x = 35 etc, the computer has problems in making the computation.
    This is because of the exponentiall growing timecomplexity, which arises from the fact that every fib(x) has two fib calls.

    Dynamic programming can be employed here, making an observation that we can actually avoid a lot of work here. Many of
    the subproblems are reiterated, for instance fib(8) = fib(7) + fib(6) = fib(6) + fib(5) + fib(6) + fib(5) + fib(4) ...
    Fib2 is a memorized implementation of fibonacci
'''

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

# Levenstein distance problem - closest_distance_two_words ()
# This is a function that takes in two words which we must call W1 and W2. The function should then calculate the smallest
# editing distance between the two, and an edit can be three things:
# 1. The adding of a character.
# 2. The removal of a character.
# 3. The change of a character.
# Naturally we could traverse through the entire problem space, however, there is a problem here. For every character that
# is wrong we have to make the decision which one of the editing distances to make, and as can be seen, such an endeavour
# will take us into the realm of exponential time complexity. There has to be a smart way in which we can solve this problem.

def closest_distance_two_words(W1, W2, previous_word, memoize = None):
    memoize = [[]]
    previous_word = " "

def partial_distance(W1, W2, L1, L2, memo, previous_word):
    pass

