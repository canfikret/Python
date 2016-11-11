def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

if (__name__ == "__main__"):
    g = gen246()
    next(g)
