n = 13
factors = [n]

# Finding the smallest multiple
smallest_multiple = 1
for i in range(2, n+1):
    smallest_multiple *= i

# Finding the factors
for i in range(n, 1, -1):
    if smallest_multiple % i == 0:
        factors.append(i)

print(f"The factors of the smallest multiple of the first {n} numbers are: {factors}")
print(f"The smallest multiple of the first {n} numbers is: {smallest_multiple}")