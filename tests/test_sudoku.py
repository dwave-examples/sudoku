# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import unittest
from unittest.mock import patch
from io import StringIO

from sudoku import is_correct, build_bqm, solve_sudoku

class TestSudoku(unittest.TestCase):
    def test_is_correct(self):
        bad_matrix = [[1,2,3,2],
                      [3,2,1,4],
                      [4,1,2,3],
                      [2,3,4,1]]

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(is_correct(bad_matrix))
            self.assertIn("Error in row:  [1, 2, 3, 2]", mock_stdout.getvalue())

        good_matrix = [[1,4,3,2],
                       [3,2,1,4],
                       [4,1,2,3],
                       [2,3,4,1]]

        self.assertTrue(is_correct(good_matrix))

    def test_solve_sudoku(self):
        matrix = [[1,0,0,0],
                  [0,0,0,4],
                  [0,0,2,0],
                  [0,3,0,0]]

        target = [[1,4,3,2],
                  [3,2,1,4],
                  [4,1,2,3],
                  [2,3,4,1]]

        bqm = build_bqm(matrix)
        result = solve_sudoku(bqm, matrix)

        self.assertEqual(result, target)
