def process_file(file_name):
    with open(file_name, "r") as dataf:
        list0 = [line.strip().split(",") for line in dataf.readlines()]

    for i in range(len(list0)):
        list0[i][1] = list0[i][1].strip("\n")
        list0[i][1] = int(list0[i][1])

    batlist = [[i[0], i[1]] for i in list0]

    for i in range(11):
        for j in range(11):
            if batlist[i][1] == batlist[j][1] and batlist[i][0] < batlist[j][0]:
                batlist[i], batlist[j] = batlist[j], batlist[i]
            elif batlist[i][1] > batlist[j][1]:
                batlist[i], batlist[j] = batlist[j], batlist[i]

    for i in batlist:
        print(f"{i[0]},{i[1]}")

process_file("ind.txt")
process_file("rsa.txt")