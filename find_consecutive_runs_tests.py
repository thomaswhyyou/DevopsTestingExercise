from unittest import TestCase

import find_consecutive_runs as fcr

class TestFindConsecutiveRuns(TestCase):

    def test_empty_list(self):
        test_sample = []
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(result, None)

    def test_not_enough_integers(self):
        test_sample = [1, 2]
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(result, None)

    def test_consecutive_runs_one_direction(self):
        test_sample = [1, 2, 3, 4]
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(type(result), list)
        self.assertEqual(result, [0, 1])

        # Check for non-contiguous list of numbers too.
        test_sample = [1, 2, 3, 4, 14, 15, 20, 21, 22, 55, 56, 57, 58]
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(type(result), list)
        self.assertEqual(result, [0, 1, 6, 9, 10])

    def test_consecutive_runs_both_directions(self):
        test_sample = [1, 2, 3, 4, 14, 20, 19, 18, 0, 0, -1, -2, -3, 10, 11, 12]
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(type(result), list)
        self.assertEqual(result, [0, 1, 5, 9, 10, 13])

    def test_consecutive_runs_instruction_example(self):
        test_sample = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
        result = fcr.find_consecutive_runs(test_sample)
        self.assertEqual(type(result), list)
        self.assertEqual(result, [0, 4, 6, 7])

