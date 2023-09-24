import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import module1.generic_functions as generics

if __name__ == '__main__':
    variable1 = "some_name"
    variable2 = 1
    generics.some_function1(variable1, variable2)