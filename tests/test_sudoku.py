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
