""" fibbinachi rabbits. I really need to stop spelling italian words
with h's after the c's..... oh well."""

Months = 6
life_span = 3

pop = [1]
born = [1]
dead = [0,] * (life_span - 1)
dead.append(1)

for i in range(1,Months):
    nextpop = born[i-1] - dead[i]
    nextborn = sum(born[i-life_span:i])
    nextdead = born[i-life_span]
    pop.append(nextpop)
    born.append(nextborn)
    dead.append(nextdead)