def is_primitive_element(g, p):
    for q in prime_factors(p - 1):
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def find_primitive_element(p):
    for g in range(2, p):
        if is_primitive_element(g, p):
            return g

p = 28151
primitive_element = find_primitive_element(p)
print(f"The smallest primitive element of F_{p} is: {primitive_element}")
