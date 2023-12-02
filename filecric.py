
file_path = "ind.txt"

file = open(file_path, "r")

list = []

for line in file:
    split_line = line.split()
    list.append(split_line)

file.close()
print(list)

