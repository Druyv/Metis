import unittest
import subprocess
import sys


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


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFinalResult)
    unittest.TextTestRunner(sys.stdout, verbosity=2).run(suite)


if __name__ == '__main__':
    run_tests()
