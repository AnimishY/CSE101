a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
while True:
    if a%b == 0:
        break
    else:
        a, b = b, a % b
print('Result: ', b)