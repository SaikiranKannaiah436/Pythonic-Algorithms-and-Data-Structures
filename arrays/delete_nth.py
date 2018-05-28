"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""

from collections import defaultdict


# naive method O(n^2)
def delete_nth_naive(lst, n):
	new_lst = []
	for num in lst:
		if new_lst.count(num) < n:
			new_lst.append(num)
	return new_lst


# O(n) using in-built data structures
def delete_nth(lst, n):
	new_lst = []
	freq = defaultdict(int)
	for num in lst:
		if freq[num] < n:
			new_lst.append(num)
			freq[num] += 1
	return new_lst







			


