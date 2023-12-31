def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 66528
b = 52920

result = gcd(a, b)

print(f"The GCD of {a} and {b} is: {result}")
