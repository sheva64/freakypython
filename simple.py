def is_simple(x: int):
    assert x > 1
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True

for x in range(999, 9999):
    if is_simple(x):
       print(x, end=" ")