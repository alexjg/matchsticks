Matchsticks is a library of complex argument matchers to be used with mock. Currently it contains a matcher for comparing dictionaries only by the keys specified in some expected dictionary, for example::

    expected = {
        "key1": "value1",
    }
    actual = {
        "key1":"value1",
        "key2": "value2",
    }
    matcher = SubDictMatches(expected)
    matcher == actual #Returns True

This will raise an assertion error if the keys from expected do not match thos in actual. This is so the matcher can be used in a mock::

    mock.assert_called_with(matcher)
