'''
    Sorting Algorithms
    A sorting algorithm takes an unsorted list as an input and returns a sorted list for instance:
    [1,2,5,4,3] --> [1,2,3,4,5]
    Naturally these sorting algorithms operate in different time complexities but generally O(N log N) is the best one
    can hope for. Often O(N^2) is the worst time complexity, for instance with Selection Sort and Insertion Sort, where
    one has to iterate through the entire problem instance in a double-nested loop. Also in a quicksort with a bad pivot
    selection method it can degenerate into a O(N^2) time, if we for instance has the reversed list [5,4,3,2,1] and we
    only select the first element this will be bad since the element is an outer element. Generally one can conceptually
    understand that different sorting algorithms can be of different time complexity based on the nature of the problem.
    Here are some sorting algorithms in an increasingly order in terms of difficulty:
'''

import math
import shuffling_algorithms as shuffler

# simple_bubble_sort
# A simple bubble sort that iterates through the list with no optimizations and always flips elements elementwise so that
# the biggest element come to the right. Obviously the sorting space can be reduced by one for each iteration, as the biggest
# number will flip to the rightmost spot, however, this bubble sort makes no such optimization and does some redundant
# operations in favour of simplicity.

def simple_bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-1):
            if(list[j+1] < list[j]):
                list[j],list[j+1] = list[j+1],list[j]

    return list

# opt_bubble_sort
# Very similar to the OG bubble sort above but this one makes an optimization in the inner loop.

def opt_bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if (list[j + 1] < list[j]):
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

# selection_sort
# Selection sort is in my opinion one of the simpler sorting algorithms boths conceptually as well as concretely.
# The sorting algorithm makes two iterations, one outer, i = [0, length(list)], and one inner, j = [i+1, length(list).
# Conceptually what we are doing is moving to place i and scouting through the list for better candidates, that is of
# course, elements smaller than i. This is done at a complexity that is O(n^2), naturally, because the elementary operation
# can be the assigning of a minimum index and so the entire procedure will be done in: O(n^2).

def selection_sort(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if(list[j] < list[min_index]):
                min_index = j

        list[i],list[min_index] = list[min_index],list[i]

    return list


# insertion_sort()
# An Insertion_sort uses a sorting mechanism in which we take an element i, which we iterate through and in this implementation
# we call it 'comparing_element'. This element is put into an own loop where we iterate down to the buttom, swapping elements as we go.
# We have to parts of the list, one which is sorted and one which is not, and we work our way through the unsorted part.
# Also in O(n^2)

def insertion_sort(list):
    n = len(list)
    for i in range(1, n):

        comparing_element = list[i]
        j = i - 1
        while j >= 0 and comparing_element < list[j]:
            list[j+1] = list[j]
            j -= 1

        list[j+1] = comparing_element

    return list

# merge_sort()
# The merge_sort is a divide and conquer algorithm operating in O(n log n), it breaks down the problem instance into its smallest component and
# from there reconstructs it, making good use of the fact that all of the sublists of the initial list are already ordered and so we can compare
# them list-wise. This implementation uses a small optimization in that the length of a problem can be passed down as an argument and so we do not
# have to measure the length for each recursion, this is done automatically for us, making use of what we have.
# Parts of the implementation from: https://www.geeksforgeeks.org/merge-sort/

def merge_sort(list, length = -1):
    if(length == -1):
        length = len(list)

    if(length > 1):
        split_point = length//2
        Left_length = math.ceil(length/2)
        Right_length = math.floor(length/2)

        Left  = list[split_point:]
        merge_sort(Left, Left_length)


        Right = list[:split_point]
        merge_sort(Right, Right_length)

        l = r = k = 0

        while l < Left_length and r < Right_length:
            if Left[l] < Right[r]:
                list[k] = Left[l]
                l += 1
            else:
                list[k] = Right[r]
                r += 1
            k += 1

        while not l == Left_length:
            list[k] = Left[l]
            l += 1
            k += 1

        while not r == Right_length:
            list[k] = Right[r]
            r += 1
            k += 1

# median_of_three()
# This is a helper function for a quick sorting algorithm. The sorting algorithm builds upon the idea of using pivots,
# these pivots should be in the middle for an optimal effect. That is if we have for example a shuffling of [1,2,3,4,5],
# the best pivot would be 3. The median_of_three functions selects three values and takes the middle value of these, so
# as to provide as a good pivot as possible with three current elements.

def median_of_three(l, length = -1):
    length = len(l)

    e1 = l[0]
    e2 = l[length//2]
    e3 = l[length-1]

    l2 = [e1,e2,e3]
    l2.sort()
    return l2[1]


def median_of_three_index(l = None, start = -1, end = -1):

    e1 = l[start]
    e2 = l[(start+end)//2]
    e3 = l[end]

    d = {
        e1 : 0,
        e2 : (start+end)//2,
        e3 : end
    }

    l2 = [e1,e2,e3]
    l2.sort()
    return d[l2[1]]

def start_element(l = [], start = -1, end = -1):
    return start

def end_element(l = [], start = -1, end = -1):
    return end

# quick_sort()
# A sorting algorithm where a pivot is chosen and where we "meet in the middle". That is, we iterate through an array
# with an index that is coming from two directions, and for each index we compare the element there with a pivot element.
# This quicksort is a generalized quicksort that takes in as a parameter a function that determines how to select the
# ever so important pivot element.


def partition(l, f, start, end):
    # 1.
    length = len(l)
    if length == 1 or length == 0:
        return l

    else:

        # 2.
        pivot_index = f(l,start,end)
        pivot = l[pivot_index]
        #l[start], l[pivot_index] = l[pivot_index], l[start]



        # 3.
        low_bound  = start + 1
        high_bound = end
        legal_bound   =   lambda x,y   : x <= y
        can_move_high =   lambda x,y,p : l[high_bound] >= p
        can_move_low  =   lambda x,y,p : l[low_bound]  <= p

        # 4.
        while legal_bound(low_bound, high_bound):
            while legal_bound(low_bound,high_bound) and can_move_high(low_bound, high_bound, pivot):
                high_bound = high_bound -1

            while legal_bound(low_bound,high_bound) and can_move_low(low_bound,  high_bound, pivot):
                low_bound += 1

            if(legal_bound(low_bound,high_bound)):
                l[low_bound],l[high_bound] = l[high_bound],l[low_bound]
            else:
                break


        l[pivot_index],l[high_bound] = l[high_bound],l[pivot_index]

        return high_bound


def quick_sort(l, f = start_element, start = -1, end = -1):
    if(start == -1):
        start = 0
    if(end == -1):
        end = len(l) - 1

    if start >= end:
        return

    p = partition(l,f, start, end)

    if p > start:
        quick_sort(l,f,start,p-1)

    if p < end:
        quick_sort(l,f,p+1,end)

# naive_quick_sort()
# A Naive implementation of the quicksort I found online and worked on.
# Worked on from: https://stackoverflow.com/questions/18262306/quicksort-with-python

def naive_quick_sort(l, length = -1):
    smaller_than_pivot = []
    length1 = 0
    equal_to_pivot =     []
    greater_than_pivot = []
    length2 = 0

    if(length == -1):
        length = len(l)

    if(length > 1):
        pivot = median_of_three(l)
        for e in l:
            if(e > pivot):
                greater_than_pivot.append(e)
                length2 += 1
            elif(e < pivot):
                smaller_than_pivot.append(e)
                length1 += 1
            else:
                equal_to_pivot.append(e)

        return naive_quick_sort(smaller_than_pivot, length1) + equal_to_pivot + naive_quick_sort(greater_than_pivot, length2)
    else:
        return l

# dumb_dumb_sort()
# The dumb_dumb_sort is a sorting algorithm akin to taking a deck of cards and tossing them sky high for them to land,
# to repeat this process again and time again, until the deck finally lands in a sorted way. It is a dumb algorithm
# to use all permutations and randomly iterate them until a match is find but this algorithm .. This algorihm is even
# dumber, still, see in a problem size of 5 for instance there are !5 = 120 permutations, and so a permutation sort will
# exhaust those. The dumb_dumb_sort may even reaccess a previously accessed permutation, thus, another dumb has to be
# prefixed just to make it clear that this algorithm is indeed very dumb and if you want to see the extent of its dumbness
# you can use it on a problem instance greater than 10, and then go for a run.
# Even the best case scenario is bad since even if it by a stroke of luck makes the right permutation first time,
# something that is of probabilitiy E(x) = 1/n!, it will still be in atleast linear time due to the fisher yates algoritm.

def Sorted(l):
    sorted = True
    i = 1
    length = len(l)
    while i < length:
        if(l[i-1] > l[i]):
            sorted = False
            break

        i+= 1

    return sorted

def dumb_dumb_sort(l):
    while not Sorted(l):
        shuffler.fisher_yates(l)

    return l

# TODO
def bucket_sort(l, amount_of_buckets, f):
    big_bucket = [[]]*amount_of_buckets
    upper_bound = max(l)
    lower_bound = min(l)



