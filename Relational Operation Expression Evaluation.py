a = int(input())
b = int(input())
c = int(input())
d = int(input())

#a>b AND b==c OR d!=a AND NOT a==c

i = bool(a>b)
j = bool(b==c)
k = bool(d!=a)
l = bool(a==c)
m = bool(not l)
n = bool(i and j)
o = bool(k and m)
p = bool(n or o)

print(p)