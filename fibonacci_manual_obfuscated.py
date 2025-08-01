def x1(a):
    if a <= 1:
        return a
    else:
        return x1(a-1) + x1(a-2)

print(x1(5))  # Output: 5
