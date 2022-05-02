import unittest
import subprocess
import sys
import os

"""
This is a test suite for assignment 150441 from course 27193.

This example is used to showcase how to test an exercise that simply prints the
expected output. It is generally advisable to run the tests in a new process as
to stop the student's code from potentially accessing the test suite's internals.

Using the subprocess.check_output() function, the output of the student's code is
returned (as a byte string), which we can then decode to a string, parse and check.
"""


class TestFinalResult(unittest.TestCase):

     def test_final_result(self):
        args = ["python", "opdr4_6.py"]
        # This runs the student's code in a new process and returns the output
        process = subprocess.check_output(args)
        # This decodes the byte string into a string
        output = process.decode('utf-8')
        # This splits the string into a list containing each separate print statement
        output = output.split('\r\n')
        # This removes an empty string from the end of the list
        output = output[:-1]
        # Check if the final result is correct
        self.assertEqual(output, ['u', 'i', 'o', 'a', 'o', 'u', 'e', 'e', 'o', 'a', 'e', 'e', 'a', 'a', 'o', 'e', 'a'])


def run_tests(file_name):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFinalResult)
    unittest.TextTestRunner(file_name).run(suite)


if __name__ == '__main__':
    with open('test_results.txt', "w+") as f:
        run_tests(f)