def decorator_func(func):
    
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    
    return decorator_func(func)
def add(a, b):
    return a + b

decorated_add = apply_decorator(add)
result = decorated_add(2, 3)
print(result)  

