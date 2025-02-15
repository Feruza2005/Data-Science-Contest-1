import time

def decorator_1(function):
    def wrapper(*a, **b):
        start_time = time.time() 
        function(*a, **b) 
        end_time = time.time()  
        execution_time = end_time - start_time  
        print(function.__name__, "ran in", round(execution_time, 4), "seconds") 
    return wrapper
