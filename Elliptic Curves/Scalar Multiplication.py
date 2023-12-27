from Crypto.Util.number import inverse

a = 497
b = 1768
p = 9739

P = (2339, 2213)

def point_addition(P, Q):
    O = (0, 0)

    if P == O:
        return Q
    if Q == O:
        return P

    x1, y1 = P[0], P[1]
    x2, y2 = Q[0], Q[1]

    if P != Q:
        if x1 == x2:
            return O
        lam = ((y2 - y1) * inverse(x2 - x1, p)) % p
    else:
        lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

def point_doubling(P):
    return point_addition(P, P)

Q = P
for _ in range(7862):
    Q = point_addition(Q, P)

assert (Q[1]**2 - Q[0]**3 - a * Q[0] - b) % p == 0, "Q is not on the curve"

print("Point Q:", Q)
