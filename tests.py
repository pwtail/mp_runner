import unittest


class Test1(unittest.TestCase):

    def test1(self):
        assert 2 == 1 + 1

    def test2(self):
        assert 1 == 2


class Test2(unittest.TestCase):

    def test1(self):
        assert 2 == 1 + 1

    def test2(self):
        assert 1 == 2

class Test3(unittest.TestCase):

    def test1(self):
        assert 2 == 1 + 1

    def test2(self):
        assert 1 == 2