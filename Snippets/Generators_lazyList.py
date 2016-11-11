million_squares = (x*x for x in range(1,1000001))
million_squares

# now runs
list(million_squares)


sum(x*x for x in range(1, 1000001))

sum(x for x in range(1001) if is_prime(x))
