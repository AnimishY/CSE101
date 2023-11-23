a = True
b = False
c = False
d = False

x = bool(not b) 
y = bool(not d) 
z = bool(a and x) 
w = bool((c or b) and y and c) 

result = bool(z or w) 
print(result)