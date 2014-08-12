#!/usr/bin/env python

import unittest
import names
import random

minAdj = len(names.adjectives)-1
minAni = len(names.animals)-1

class FlaskTests(unittest.TestCase):

    def testNames(self):

        return "%s%s" % (
            names.adjectives[random.randint(0, minAdj)],
            names.animals[random.randint(0, minAni)]
        )

if __name__ == '__main__':
    unittest.main()
