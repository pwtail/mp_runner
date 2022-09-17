import unittest

import fasteners

lock = fasteners.InterProcessLock()

class MPResult(unittest.TextTestResult):

    def printErrors(self):
        with lock:
            super().printErrors()