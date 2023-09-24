import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import module1.generic_functions as generics

def run_app():
    variable1 = "some_name"
    variable2 = 1
    result = generics.some_function1(variable1, variable2)
    return result

if __name__ == '__main__':
    result = run_app()
    print("result[0]=%s\nresult[1]=%s" % (result[0], result[1]))