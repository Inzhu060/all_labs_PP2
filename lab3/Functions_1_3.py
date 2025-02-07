def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if chickens * 2 + rabbits * 4 == numlegs:
            return chickens, rabbits
    return "no solution"
    
numheads = 45
numlegs = 114
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens -> {chickens} and rabbits -> {rabbits}")