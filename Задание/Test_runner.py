#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
import Tests


testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(Tests)
#testResult = unittest.TestResult()
Test = unittest.TestSuite()
Test.addTest(unittest.makeSuite(Tests.SqlTest))
print("Count of tests: " + str(Test.countTestCases()) + "\n")
runner = unittest.TextTestRunner(verbosity=2)
#testResult = runner.run(suites)
runner.run(suites)
#print("errors")
#print(len(testResult.errors))
#print("failures")
#print(len(testResult.failures))
#print("skipped")
#print(len(testResult.skipped))
#print("testsRun")
#print(testResult.testsRun)