#input 4 numbers and print permutation of first 3 numbers and only print those permutation whose sum isn't equal to 4th number

x = int(input())
y = int(input())
z = int(input())
n = int(input())

from itertools import permutations
a = list(permutations([x,y,z]))

for i in a:
    if sum(i) != n:
        print(i)