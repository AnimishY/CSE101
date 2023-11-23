num = int(input())
a = int(input())
b = int(input())

if num%a==0:
    if num%b==0:
        print("FooBar")
    else:
        print("Foo")
elif num%b==0:
    print("Bar")
else:
    print