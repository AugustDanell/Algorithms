'''
  Shuffling Algorithms:
  A shuffling algorithm is simply an algorithm that permutes the indices of a list, but presumably does it in a way that
  is random. So for instance [1,2,3,4,5] -> any permutation in a random way, including the identity-permutation. For
  instance this can be done in a permutation sort where the shuffling is redone until the list is sorted.
'''

import random

# A simple but good shuffling algorithm
def fisher_yates(list):
    for i in range(len(list)-1,0, -1):
        rand = random.randint(0, i)
        #print("Indices: ", i, rand)
        list[i],list[rand] = list[rand],list[i]

    return list
