def factorial(x):
    return 1 if x == 0 or x == 1 else x * factorial(x-1)

def vilson(p):
    return (factorial(p-1) + 1) % p == 0

for x in range(2, 100):
    if vilson(x):
        print(x)