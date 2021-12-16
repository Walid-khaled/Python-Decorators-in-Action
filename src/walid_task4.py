import time , io 
import contextlib	
from datetime import datetime

def decorator_4(fun):           
    count = 0
    def wrapper(*args,**kwargs): 
        nonlocal count #it gives access to the variable outside the function in a nested function
        count += 1 
        start_time = time.perf_counter() 
        try:    
            fun(*args,**kwargs) 
        except Exception as error:
            with open("log file.txt","a") as f:
                print("Error piped to log file")
                f.write(f"Error: {error}  Time: {datetime.now()}")
                f.write('\n') 
        else:
            end_time = time.perf_counter() 
            exectime= end_time - start_time            
            print(f"{fun.__name__} call {count} executed in {exectime} sec") 
          
    return wrapper 
        


