import time , io
import contextlib

def decorator_1(fun):
    count = 0
    def wrapper(*args,**kwargs): 
        nonlocal count #it gives access to the variable outside the function in a nested function
        count += 1 
        start_time = time.perf_counter() 
        with contextlib.redirect_stdout(io.StringIO()) as f: #it takes care of text inside (does not print it) and store it in another variable
            fun(*args,**kwargs) 
        end_time = time.perf_counter() 
        exectime= end_time - start_time    
        print(f"{fun.__name__} call {count} executed in {exectime} sec") 
    return wrapper 
        
