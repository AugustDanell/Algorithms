# SORTING TESTS: -------------------------------------------------------------------------------------------------------
# List comprehensions generate two similar lists, one which is sorted and will not be changed and one which starts of
# as sorted but will be scrambled using the Fisher Yates Shuffling algorithm so we:
# 1. Define an ordered list.
# 2. Copy the list to a new one.
# 3. shuffle the new one into an unsorted list.
# 4. Apply the sorting algorithm.
# 5. Assert that the unsorted list equals the sorted list.

import shuffling_algorithms as shuffler
import sorting_algorithms as sorter
import time

if __name__ == "__main__":
    test_sorting_methods = False
    if(test_sorting_methods):
        def benchmark_quicksorts(sorted_data, **pivot_selections):
            unsorted_data = sorted_data.copy()                           # 0. Copy the value of the data (shallow copy).
            work_time_table = {}                                         # 1. Assign a table to place tested functions in.

            for name,f in pivot_selections.items():                      # 0. For each functional argument:
                shuffler.fisher_yates(unsorted_data)                     # 1. Shuffle the testdata around.
                tick1 = time.perf_counter()                              # 2. Start the clock.
                sorter.quick_sort(unsorted_data, lambda l,s,e: f(l,s,e)) # 3. Insert the pivot selection method for the function.
                tick2 = time.perf_counter()                              # 4. End the clock.
                work_time = tick2 - tick1                                # 5. Calculate the work time.
                work_time_table[name] = work_time                        # 6. Map the worktime to the tested function
                assert unsorted_data == sorted_data                      # 7. Make sure that it actually sorts and not fucks up.

            return work_time_table                                   # Finally: Return the worktime-function mapping.

        inclusive_roof = 25
        inclusive_roof += 1                                          # Making sure that the boundry is inclusive.
        sorted_list = [x for x in range(1,inclusive_roof)]
        list = [x for x in range(1, inclusive_roof)]

        list = shuffler.fisher_yates(list)
        assert sorter.simple_bubble_sort(list) == sorted_list

        list = shuffler.fisher_yates(list)
        assert sorter.opt_bubble_sort(list) == sorted_list

        list = shuffler.fisher_yates(list)
        assert sorter.selection_sort(list) == sorted_list

        list = shuffler.fisher_yates(list)
        assert sorter.insertion_sort(list) == sorted_list

        list = shuffler.fisher_yates(list)
        sorter.merge_sort(list)
        assert list == sorted_list

        list = shuffler.fisher_yates(list)
        assert sorter.naive_quick_sort(list) == sorted_list


        list = shuffler.fisher_yates(list)
        sorter.quick_sort(list)
        assert list == sorted_list

        small_list_sorted = [x for x in range(5,26,5)]
        small_list = small_list_sorted.copy()
        small_list = shuffler.fisher_yates(small_list)
        assert small_list_sorted == sorter.dumb_dumb_sort(small_list)

        bigList = [x for x in range(10)]
        shuffler.fisher_yates(bigList)
        #work_table = benchmark_quicksorts(bigList, take_first = lambda l,s,e: sorter.start_element(l,s,e), median_of_three = lambda l,s,e: sorter.median_of_three_index(l,s,e))
        #print(work_table)
        #shuffler.fisher_yates(bigList)
        #sorter.quick_sort(bigList, lambda l,s,e: sorter.median_of_three_index(l,s,e))
        sorter.quick_sort(bigList,  lambda l,s,e: sorter.end_element(l,s,e))
        print(bigList)

    '''OK!
        shuffler.fisher_yates(list)
        sorter.quick_sort(list, lambda l,s,e: sorter.start_element(l,s,e))
        assert sorted_list == list
    '''

# todo sorter.bucket_sort(list,5,sorter.insertion_sort(list))

# ----------------------------------------------------------------------------------------------------------------------

# Test for Recursive Algorithms ----------------------------------------------------------------------------------------
# In this segment we test the basic recursive algorithms implemented in 'recursions.py'.

    test_recursive_methods = True
    if test_recursive_methods:
        import recursions as recurser
        def benchmark_fibonaccis(problem_instance):
            t1 = time.perf_counter()
            recurser.fibonnaci(problem_instance)
            t2 = time.perf_counter()
            recurser.memoized_fibonacci(problem_instance)
            t3 = time.perf_counter()
            recurser.bottom_up_fibonacci(problem_instance)
            t4 = time.perf_counter()
            print("Benckmark for fibonnacci of size n =", problem_instance, ":")
            print("Naive_Fibbonacci:", t2-t1, "\nMemoized Fibonacci:", t3-t2, "\nBottom Up Fibonacci:", t4 - t3)

        assert recurser.fibonnaci(8) == 21
        assert recurser.memoized_fibonacci(8) == 21
        assert recurser.memoized_fibonacci(5) == recurser.fibonnaci(5)
        #benchmark_fibonaccis(30)

        assert recurser.multiplication(5,6) == 30
        assert recurser.multiplication(-5, 6) == -30
        assert recurser.multiplication(5, -6) == -30
        assert recurser.multiplication(5, 0) == 0
        assert recurser.multiplication(0, 0) == 0
        assert recurser.multiplication(0, 5) == 0

        assert recurser.faculty(5) == 120
        assert recurser.faculty(0) == 1
        assert recurser.tail_recursive_faculty(0) == 1
        assert recurser.tail_recursive_faculty(5) == 120
        assert recurser.tail_recursive_faculty(20) == recurser.faculty(20)

        assert recurser.how_far_from_palindrome("Hello") == 2
        assert recurser.how_far_from_palindrome("abba") == 0
        assert recurser.how_far_from_palindrome("abc") == 1
        assert recurser.merge_lists([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
#-----------------------------------------------------------------------------------------------------------------------

