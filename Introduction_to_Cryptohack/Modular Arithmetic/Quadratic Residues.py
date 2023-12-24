p = 29
ints = [14, 6, 11]

def legendre_symbol(a, p):
    return pow(a, (p-1)//2, p)

def find_square_roots(a, p):
    legendre = legendre_symbol(a, p)
    
    if legendre == 1:
        for x in range(1, p):
            if pow(x, 2, p) == a:
                return x, p - x
    else:
        return None

for a in ints:
    roots = find_square_roots(a, p)
    
    if roots:
        flag = min(roots)
        print(f"For {a}, the quadratic residue is {flag}")
    else:
        print(f"For {a}, there is no quadratic residue.")
