'''
  Greedy Algorithms:
  A greedy algorithm is an algorithm that locally looks to maximize (or minimize depending on the problem). This is often
  easy to understand and quick to implement but it is not guaranteed that there will be an optimal solution. For instance
  maybe we have a tree where each node holds two leaves. A typical Greedy Algorithm could be to always chose the greater
  of the two and so to try to find a maximum. However, one problem could be that a locally bad choice could make it so
  we would choose an overall better solution, a global maximum that is. Sometimes greedy algorithms can provide an
  optimal solution but in the case of a problem like this, a maximum sum of a tree where we only take the greatest with
  no other consider, then no, this will not always provide a guaranteed best solution though it could.
'''