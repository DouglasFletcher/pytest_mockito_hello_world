from mockito import spy2, when
import module1.generic_functions as generics

def test_some_function1():
    # input
    var1 = "test1"
    var2 = 1
    exp_result = ["test1_append", 3]
    # run
    act_result = generics.some_function1(variable1=var1, variable2=var2)
    # tests
    assert exp_result[0] == act_result[0]
    assert exp_result[1] == act_result[1]