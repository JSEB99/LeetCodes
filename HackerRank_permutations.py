
x = 1
y = 1
z = 2
n = 3

permutations = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

fit_permutations = [permutation for permutation in permutations if sum(permutation)<n]

print(fit_permutations)

    