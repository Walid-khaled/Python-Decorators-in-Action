import time , io
import contextlib	
from inspect import signature, getsource


class decorator_3:
    #Class attribute shared for all @profiled functions
    n = 0 
    exectime_dic = {}
    
    def __init__(self,fun):
        self.fun = fun
        self.count = 0       
        
    def __call__(self,*args,**kwargs):   
        self.count +=1
        type(self).n += 1 #Increment n on the type, not the instance
        start_time = time.perf_counter() 
        with contextlib.redirect_stdout(io.StringIO()) as f: #it takes care of text inside (does not print it) and store it in another variable
            self.fun(*args,**kwargs)
        end_time = time.perf_counter() 
        exectime= end_time - start_time 
        type(self).exectime_dic[self.fun.__name__]= exectime        
        s = f.getvalue()
        with open('task3.txt', 'a') as f:
            f.write(f"{self.fun.__name__} call {self.count} executed in {exectime} sec")
            f.write('\n')
            f.write(f"Name:   {self.fun.__name__}")
            f.write('\n')
            f.write(f"Type:   {type(self.fun)}")
            f.write('\n')
            f.write(f"Sign:   {signature(self.fun)}")  
            f.write('\n')            
            f.write(f"Args:   positional ({self.fun.__defaults__}) key=worded ({self.fun.__kwdefaults__})") 
            f.write('\n')            
            f.write(f"Doc:    {self.fun.__doc__}")
            f.write('\n')            
            f.write(getsource(self.fun))
            f.write('\n')            
            f.write(f"Output: {s}") 
            f.write('\n\n')
        
    
        if type(self).n==4:
            print(type(self).exectime_dic)   
            print("FUNCTION   |   RANK   |   TIME ELAPSED")
            z =0
            for tpl in sorted(type(self).exectime_dic.items()):
                print(tpl[0],'\t', z+1,'\t',tpl[1])
                z += 1       
        
        
    