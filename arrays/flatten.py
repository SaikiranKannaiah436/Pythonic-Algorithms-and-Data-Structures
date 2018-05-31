"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

from collections import Iterable

# Recursion
def flatten(input_arr, out_arr=None):

	if out_arr == None:
		out_arr = []

	for element in input_arr:
		if isinstance(element, Iterable):
			flatten(element, out_arr)
		else:
			out_arr.append(element)

	return out_arr

