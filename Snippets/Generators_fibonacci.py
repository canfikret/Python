def Fib():
    yield 1
    a=1
    b=1
    while True:
        yield b
        a,b=b,a+b

for x in Fib():
    print(x)
