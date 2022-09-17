from unittest import TestSuite


class MPSuite(TestSuite):

    def __init__(self, testcase_cls):
        self.testcase_cls = testcase_cls

    def run(self, result, debug=False):
        super().run(result)