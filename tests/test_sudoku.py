import os
import subprocess
import sys
import unittest

# /path/to/sudoku/
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_dir)


class TestSmoke(unittest.TestCase):
    def test_smoke(self):
        demo_path = os.path.join(project_dir, 'sudoku.py')
        arg = 'problem.txt'

        subprocess.check_output([sys.executable, demo_path, arg])
