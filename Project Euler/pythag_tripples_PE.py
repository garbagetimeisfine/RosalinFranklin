import math
trip = []
for a in range(1,1001):
    for b in range(1,1001):
        c = math.sqrt((a ** 2) + (b ** 2))
        if math.floor(c) == c:
            trip.append((a,b,c))


#print(trip)

for thing in trip:
    if thing[0] + thing[1] + thing[2] == 1000:
        print(thing)