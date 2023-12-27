from Crypto.Util.number import inverse

a = 497
b = 1768
p = 9739

P = (8045, 6936)

def point_negation(P):
    return (P[0], -P[1] % p)

Q = point_negation(P)

print("Point Q:", Q)
