import unittest
from top_5oo_users.top_500_users import solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        leaderboard = solution()

    def test_something(self):
        self.assertEqual(len(solution().position), 500)


if __name__ == '__main__':
    unittest.main()
