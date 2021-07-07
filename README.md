# Algorithms
In this repo I write different algorithms that I have learned both as a hub for myself as well as for any employers to see what I know how to implement. This includes sorting algortihms, like quicksort, mergesort, insertion sort etc. I also write programs based on dynamic programming where for instance we have the exponential growth of the fibonacci numbers, in a top down approach. In my tests I test the different times of a bottum up versus a top down and memoized version. Overall I have been working in the following folders:

- Sorting Algorithms
- Shuffling Algorithms
- Dynamic programming
- Recursions

## Shuffling & Sorting Algorithms
One of the biggest subfolders in this repository pertains to sorting algortithms. Here I have implemented a myriad of different sorting algortihms including a generalized quicksorting algorithm that takes as argument a function for which to select a pivot. The sorting algorithms are tested using a sorted list and its copied value unto another list. We shuffle the copied list around using Fisher-Yates Shuffling algorithm implemented in "shuffling algortihms", and we make assertions that the sorted list has to be equal to the list where a sorting algortihm was applied for each time a sorting algortihm runs. I have implemented different sorting algortihms from a stupid permutation_sort to a generalized quicksort where each one works though some sorting algorithms are simply much better.

As of right now the quicksort works well if the first element is selected as pivot, that is if we feed first_element_pivot() as an argument, for other pivot selection functions it doesn't work right now. The problem of course with selecting the first element is for instance a reversed list, we want to find a pivot somewhere in the middle but in a reversed list we will always get "extreme" elements. I have implemented a quicksort in Java in my programming DD1337 course where we took 3 elements and took the median of those three, and that selection method increased the time in which the sorting was made by quite a lot, and so I will make that work here as well.

## Dynamic Programming
Dynamic programming entails that we are making use of the way a problem can be broken up into overlapping subproblems. The fibonacci implementations are an example of that but there are others such as the Levenstein Distance etc, that is the smallest editing distance between two words W1, W2. This programming technique allows us to reduce the time complexity of problems from exponential time down to linear time sometimes, or atleast polynomial time. The Levenstein Distance, like fibonacci, are examples of how one can make that reduction in time complexity from brute force to dynamic programming.

## Recursions
Here I have only been playing with basic recursive algorithms, not done anything interesting really.
 
