

def sayHello(name):
    return f"Hello {name}"

def sayBye(name):
    return "Bye {}".format(name)

def speak(func):
    return func("salman")

print(speak(sayHello))
print(speak(sayBye))


