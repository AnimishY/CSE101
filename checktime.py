from time import time

start_time = time()

N = 100
fact = 1

for k in range(2, N+1):
    fact = fact * k
print(fact)
end_time = time()
print("Time taken: ", end_time - start_time)