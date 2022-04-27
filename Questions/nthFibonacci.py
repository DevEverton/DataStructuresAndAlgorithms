def getNthFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    current = 1
    previous = 1

    for i in range(1,n):
        current, previous = previous + current, current
    return previous

print(getNthFib(5))

# 0 1 1 2 3 5 

