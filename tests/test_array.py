from arrays.delete_nth import delete_nth_naive, delete_nth
from arrays.flatten import flatten

import unittest


class TestDeleteNth(unittest.TestCase):


	def test_delete_nth_naive(self):

		self.assertListEqual(delete_nth_naive([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])

		self.assertListEqual(delete_nth_naive([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])

		self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])

		self.assertListEqual(delete_nth_naive([], n=5),
                             [])

		self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])


	def test_delete_nth(self):

		self.assertListEqual(delete_nth_naive([20, 37, 20, 21, 37, 21, 21], n=1),
                             [20, 37, 21])

		self.assertListEqual(delete_nth_naive([1, 1, 3, 3, 7, 2, 2, 2, 2], n=3),
                             [1, 1, 3, 3, 7, 2, 2, 2])

		self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=3),
                             [1, 2, 3, 1, 1, 2, 2, 3, 3, 4, 5])

		self.assertListEqual(delete_nth_naive([], n=5),
                             [])

		self.assertListEqual(delete_nth_naive([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], n=0),
                             [])


class TestFlatten(unittest.TestCase):

	def test_flatten(self):
		nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]
		flattened = flatten(nested_list)
		self.assertEqual(flattened, [2, 1, 3, 4, 5, 6, 7, 8])

		nested_list = [[3, [4, 5], 6], 7, [8]]
		flattened = flatten(nested_list)
		self.assertEqual(flattened, [3, 4, 5, 6, 7, 8])

		nested_list = [[], [8]]
		flattened = flatten(nested_list)
		self.assertEqual(flattened, [8])