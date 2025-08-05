from datetime import datetime

def decorator(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

@decorator
def say():  
    print("hello")
