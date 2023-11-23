x=int(input())
a=int(input())
b=int(input())

if x%a==0:
    if x%b==0:
        print('Foobar')
    else:
        print('Foo')
elif x%b==0:
    print('Bar')
else:
    print