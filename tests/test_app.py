from mockito import spy2, when, any
from .test_context import app
from .test_context import generics

def test_main_code_coverage():
    # mocks
    when(generics).some_function1(any, any).thenReturn(["example",2])
    # run
    app
    # tests
    
