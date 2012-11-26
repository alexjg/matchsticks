from matchsticks import Matcher
import unittest

class MatcherTestCase(unittest.TestCase):

    def setUp(self):
        obj = "1234"
        compare_func = lambda obj1, obj2: obj1[:2] == obj2[:2]
        self.matcher = Matcher(compare_func, obj)

    def test_eq_behaviour_matches_compare_func_on_equal(self):
        self.assertTrue(self.matcher == "1245")

    def test_eq_behaviour_matches_compare_func_on_inequality(self):
        with self.assertRaises(AssertionError):
            self.matcher == "1345"

