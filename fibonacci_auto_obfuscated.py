def _a(_b):
    if _b <= 1:
        return _b
    else:
        return _a(_b-1) + _a(_b-2)

print(_a(5))  # Output: 5
