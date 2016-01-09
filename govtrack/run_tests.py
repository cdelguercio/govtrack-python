#!/usr/bin/env python

"""
Lifted directly from https://github.com/jeffschenck/authorizesauce/
"""

import os
import sys
from unittest2 import TestLoader, TextTestRunner


if __name__ == '__main__':
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    govtrack_dir = os.path.join(tests_dir, os.path.pardir)
    sys.path.append(govtrack_dir)
    suite = TestLoader().discover(tests_dir)
    runner = TextTestRunner(verbosity=1)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())
