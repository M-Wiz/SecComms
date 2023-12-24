def find_inverse(g, p):
    for d in range(1, p):
        if (g * d) % p == 1:
            return d

g = 3
p = 13

inverse_element = find_inverse(g, p)

print(f"The inverse element of {g} in F_{p} is: {inverse_element}")
