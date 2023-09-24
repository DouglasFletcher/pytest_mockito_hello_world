import mockito as mockito
from .test_context import app
from .test_context import generics

def test_main_code_coverage():
    # data
    exp_0 = "example"
    exp_1 = 2
    # mocks
    mockito.when(generics).some_function1(mockito.any, mockito.any).thenReturn([exp_0,exp_1])
    # run
    act_result = app.run_app()
    # tests
    assert exp_0 == act_result[0]
    assert exp_1 == act_result[1]
    mockito.verify(generics, times=1).some_function1(mockito.any, mockito.any)
    mockito.verifyNoMoreInteractions(generics)
    mockito.unstub()
