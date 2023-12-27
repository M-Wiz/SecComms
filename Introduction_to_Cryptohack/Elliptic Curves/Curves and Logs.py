from Crypto.Util.number import inverse
import hashlib

a = 497
b = 1768
p = 9739

G = (1804, 5368)

QA = (815, 3190)

n_B = 1829

def point_multiplication(n, point):
    result = (0, 0)
    current = point

    while n > 0:
        if n % 2 == 1:
            result = point_addition(result, current)
        current = point_doubling(current)
        n = n // 2

    return result

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

QB = point_multiplication(n_B, G)

S = point_multiplication(n_B, QA)

key = hashlib.sha1(str(S[0]).encode()).hexdigest()

print("Shared Secret:", key)