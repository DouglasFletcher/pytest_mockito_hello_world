from mockito import spy2, when, any
from ..context import app

def test_main_code_coverage():
    # mocks
    when(app.module1.generic_functions).some_function1(any, any).thenReturn(["example",2])
    # test
    
