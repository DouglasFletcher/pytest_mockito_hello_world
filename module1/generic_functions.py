
# some generic function to test
def some_function1(variable1:str, variable2:int) -> list:
    print("variable1: %s \nvariable2: %s" % (variable1, variable2))
    new_variable1 = variable1 + "_append"
    new_variable2 = variable2 + 2
    print("new_variable1: %s \nnew_variable2: %s" % (new_variable1, new_variable2))
    return [new_variable1, new_variable2]