import math
years = int(input())

leapdays = math.trunc(years/4)

days = years*365 + leapdays

print(days)