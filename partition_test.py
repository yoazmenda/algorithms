# https://afteracademy.com/blog/partition-equal-subset-sum
import unittest
import partition


class PartitionTest(unittest.TestCase):
    def test(self):
        self.assertTrue(partition.brute_force([1, 6, 11, 6]))
        self.assertFalse(partition.brute_force([1, 6, 11, 7]))
        self.assertTrue(partition.brute_force([1, 2, 3, 6]))
        self.assertFalse(partition.brute_force([1, 2, 5]))

    if __name__ == '__main__':
        unittest.main()