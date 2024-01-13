def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    N = 1
    for _, mod in congruences:
        N *= mod

    result = 0
    for a, mod in congruences:
        N_i = N // mod
        y_i = modinv(N_i, mod)
        result += a * N_i * y_i

    return result % N

congruences = [(2, 5), (3, 11), (5, 17)]

a = chinese_remainder_theorem(congruences)

print(a)