import mockito as mockito
from .test_context import app
from .test_context import generics

def test_main_code_coverage():
    # mocks
    mockito.when(generics).some_function1(any, any).thenReturn(["example",2])
    # run
    app
    # tests
    #mockito.verify(generics.some_function1, times=1)
    #mockito.verifyNoMoreInteractions(generics.some_function1)
    mockito.unstub()
