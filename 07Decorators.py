
import functools

def doTwice(func):
    #@functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper


@doTwice
def sayHello(name):
    print(f"Helloooooo {name} !")


sayHello("salman")
