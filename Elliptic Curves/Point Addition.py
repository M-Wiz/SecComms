from Crypto.Util.number import inverse

a = 497
b = 1768
p = 9739

P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

def point_addition(P, Q):
    O = (0, 0)

    if P == O:
        return Q
    if Q == O:
        return P

    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]

    if P != Q:
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
    else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

def point_doubling(P):
    return point_addition(P, P)

S = point_addition(point_addition(point_doubling(P), Q), R)

print("Point S:", S)
