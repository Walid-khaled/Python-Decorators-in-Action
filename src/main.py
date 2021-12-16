from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4
import math

@decorator_1
#@decorator_2
#@decorator_3
#decorator_4       
def palindromes(a):
    '''Return the palindromes word from a list.'''
    res=list(filter(lambda word: word.lower() == "".join(reversed(word.lower())),a))    
    print(res)
    
           
@decorator_1
#@decorator_2
#@decorator_3
#decorator_4  
def even_sum(l):
    '''Return the summation of even numbers in a list'''    
    res = sum(list(filter(lambda i: i%2==0, l)))
    print(res)
    

@decorator_1
#@decorator_2
#@decorator_3
#decorator_4 
def findRoots(a, b, c):
    '''This function is a quadratic equation solver'''        
    if a == 0:  
        print("Input correct quadratic equation")  
      
    else:      
        d = b * b - 4 * a * c  
        sqrt_val = math.sqrt(abs(d))  
      
        if d > 0:  
            print(f"real and different roots: {(-b + sqrt_val) / (2 * a)} and {(-b - sqrt_val) / (2 * a)}")  
      
        elif d == 0:  
            print(f"real and same roots: {-b / (2 * a)}")  
      
        else:  
            print(f"Complex Roots: {- b / (2 * a)} + i {sqrt_val} and {- b / (2 * a)} - i {sqrt_val} ")  
            
@decorator_1
#@decorator_2
#@decorator_3
#decorator_4 
def pascal(n):
    '''return pascal triangle of n rows'''
    top=[1]
    app_val=[0]
    for _ in range(n):
        print(top)
        top = [l+r for l,r in zip(top+app_val, app_val+top)]
        

            
palindromes(["innpolis","Pop","aBc"])
even_sum([1, 2, 3, 4, 5, 6])
findRoots(1,5,6)
pascal(6)
pascal(5)
findRoots(1,-6,9)       

         












