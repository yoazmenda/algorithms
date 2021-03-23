import unittest
import knapsack


class TestKnapsack(unittest.TestCase):
    def test(self):
        self.assertEqual(
            knapsack.find([(5, 60), (3, 50), (4, 70), (2, 30)], 5), 80)


if __name__ == '__main__':
    unittest.main()