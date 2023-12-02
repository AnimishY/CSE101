def is_power(a, b):
    if a == b:
        return True
    elif a/b == int(a/b):
        return is_power(a/b, b)
    else:
        return False

a = int(input())
b = int(input())

if a>1 and a>=b>1:
    print(is_power(a, b))
