m = 12
e = 65537
p = 17
q = 23

n = p * q
ciphertext = pow(m, e, n)

print(ciphertext)