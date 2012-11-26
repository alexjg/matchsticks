from matchsticks import Matcher, SubDictMatches
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


class SubDictMatchesTestCase(unittest.TestCase):

    def setUp(self):
        self.expected = {"key1":"value1", "key2":"value2"}
        self.matcher = SubDictMatches(self.expected)

    def test_no_assertion_error_throw_on_inexact_match(self):
        data = self.expected.copy()
        data["another_key"] = "another value"
        self.assertTrue(self.matcher == data)

    def test_no_assertion_error_thrown_on_exact_match(self):
        self.assertTrue(self.matcher == self.expected)

    def test_assertion_error_thrown_on_no_match(self):
        data = self.expected.copy()
        self.expected["key1"] = "someothervalue"
        with self.assertRaises(AssertionError):
            self.matcher == data
