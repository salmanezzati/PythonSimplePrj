



def percent(func):
    def inner(*args, **kwargs):
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    
    return inner

def star(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)
    
    return inner

def repeat(numTimes):
    def decoratorRepeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(numTimes):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decoratorRepeat



@repeat(2)
@star
@percent
@repeat(3)
def printer(msg):
    print(msg)

printer("hello")

