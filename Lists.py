N = int(input())
L = list()

statement = str(input())
    
for i in range(0, N):
    if statement == "print":
        print(L)
    elif statement == "sort":
        L = L.sort()
    elif statement == "pop":
        L = L.pop()
    elif statement == "reverse":
        L = L.reverse()
    else:
        splt = statement.split()
        if splt[0] == "insert":
            L = L.insert(int(splt[1]), int(splt[2]))
        elif splt[0] == "remove":
            L = L.remove(int(splt[1]))
        elif splt[0] == "append":
            L = L.append(int(splt[1]))
        else:
            print("Invalid statement")