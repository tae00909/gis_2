
def decorator(func):
    def decorated(a, b):
        if a>=0 and b>=0:
            return func(a, b)
        else:
            return ValueError('error')
    return decorated

@decorator
def th(a, b):
    return a*b/2

@decorator
def fou(a, b):
    return a*b

print(th(2, 4))
print(fou(-3, 6))