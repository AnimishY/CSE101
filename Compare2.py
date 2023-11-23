def minTime(T1, T2, T3):
    minT = T1
    if (T2 < minT):
         minT = T2
    if (T3 < minT):
         minT = T3
    print(minT)

minTime(15.0, 17.1, 26)
minTime(17.1, 15.0, 26)
minTime(17.1, 26, 15.0)