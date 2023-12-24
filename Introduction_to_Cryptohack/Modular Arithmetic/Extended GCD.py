def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

p = 26513
q = 32321

gcd_value, u, v = extended_gcd(p, q)

print(f"The GCD of {p} and {q} is: {gcd_value}")
print(f"u: {u}, v: {v}")

flag = min(u, v)
print(f"The flag is: {flag}")
