import datetime
import unittest
import inspect
import subprocess

import cf


class cfaTest(unittest.TestCase):
    def setUp(self):
        self.test_only = ()

    def test_cfa(self):
        if self.test_only and inspect.stack()[0][3] not in self.test_only:
            return

        try:
            subprocess.run(' '.join(['.', './cfa_test.sh']),
                           shell=True, check=True)
        except subprocess.CalledProcessError as e:
            self.fail(
                "A cfa command failed (see the cfa_test.sh line exiting with "
                "value of {})".format(e.returncode)
            )


# --- End: class

if __name__ == '__main__':
    print('Run date:', datetime.datetime.now())
    cf.environment()
    print()
    unittest.main(verbosity=2)
