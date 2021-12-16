import time , io
import contextlib	
import inspect

def decorator_2(fun):
    count = 0
    def wrapper(*args,**kwargs): 
        nonlocal count #it gives access to the variable outside the function in a nested function
        count += 1 
        start_time = time.perf_counter() 
        with contextlib.redirect_stdout(io.StringIO()) as f: #it takes care of text inside (does not print it) and store it in another variable
            fun(*args,**kwargs) 
        end_time = time.perf_counter() 
        exectime= end_time - start_time    
        s = f.getvalue()
        
        print(f"{fun.__name__} call {count} executed in {exectime} sec") 
        print(f"Name:   {fun.__name__}")
        print(f"Type:   {type(fun)}")
        print(f"Sign:   {inspect.signature(fun)}")  
        print(f"Args:   positional ({fun.__defaults__}) key=worded ({fun.__kwdefaults__})") 
        print(f"Doc:    {fun.__doc__}")
        print(inspect.getsource(fun))
        print(f"Output: {s}") 
        
    return wrapper 
        
