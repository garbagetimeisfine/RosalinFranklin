lifespan = 3
months = 6

pop_start = [ 1]
bourn = [ 1]
mature = [ 0]
dying = [ 0,] * (lifespan)
i = 0

while i < lifespan - 1:
    bourn.append(mature[i])
    mature.append(bourn[i] + mature[i])
    pop_start.append(mature[i + 1] + bourn[i + 1])
    i += 1
    
j = lifespan - 1
while j <= months:
    bourn.append(mature[j])
    dying.append(bourn[j - (lifespan)])
    mature.append(bourn[j] + mature[j] - dying[j])
    pop_start.append(mature[j + 1] + bourn[j + 1] - dying[j + 1])
    j += 1

print("Total bunnies ", pop_start)
print("Mature Rabbits", mature)
print("Bunnies bourn ", bourn)
print("Dead rabbits  ", dying)