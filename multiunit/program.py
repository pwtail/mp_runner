import itertools
import os
import sys
import typing
import unittest
from contextvars import ContextVar

import fasteners
import multiprocessing as mp

lock = fasteners.InterProcessLock('.multiunit.lock')
worker_info = ContextVar('worker_id')


class WorkerInfo(typing.NamedTuple):
    id: int
    count: int


class TestResult(unittest.TextTestResult):

    def printErrors(self):
        with lock:
            super().printErrors()


class TestRunner(unittest.TextTestRunner):
    resultclass = TestResult


class TestLoader(unittest.TestLoader):

    def loadTestsFromTestCase(self, testCaseClass):
        name = f'{testCaseClass.__module__}.{testCaseClass.__name__}'
        hash = sum(ord(x) for x in name)

        worker_id, count = worker_info.get()

        if hash % int(count) == int(worker_id) - 1:
            return super().loadTestsFromTestCase(testCaseClass)
        return ()


class TestProgram(unittest.TestProgram):
    initialized = False

    def __init__(self, *args, module=None, testLoader=TestLoader(), **kwargs):
        super().__init__(*args, module=module, testLoader=testLoader, **kwargs)
        self.initialized = True

    @property
    def runTests(self):
        if not self.initialized:
            return lambda *args: None
        return super().runTests

    def _getParentArgParser(self):
        parser = super()._getParentArgParser()
        parser.add_argument('--parallel', type=int, default=4,
                            help='The number of worker processes')
        return parser


def work(id, argv):
    program = TestProgram(argv=argv)
    info = WorkerInfo(id, program.parallel)
    worker_info.set(info)
    program.runTests()


def main():
    (program := TestProgram()).parseArgs(sys.argv)
    count = program.parallel
    with mp.Pool(count) as pool:
        args = itertools.product(
            range(count), [sys.argv]
        )
        pool.starmap(work, args)

    print('end')