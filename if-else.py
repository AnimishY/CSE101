n = float(input())
if n in  range (0,100):
    if n%2==0:
        if n>20:
            print("Not Weird")
        elif n>5:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")