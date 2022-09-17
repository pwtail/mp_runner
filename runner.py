import unittest

from result import MPResult


class MPRunner(unittest.TextTestRunner):
    resultclass = MPResult


class MPLoader(unittest.TestLoader):
    def loadTestsFromTestCase(self, testCaseClass):
        return MPSuite(testCaseClass)


class TestProgram(unittest.TestProgram):

    def __init__(self, *args, **kwargs):
        kwargs['testLoader'] = MPLoader()
        super().__init__(*args, **kwargs)