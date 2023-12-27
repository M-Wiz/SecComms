#i was unable to install primefac

from sympy import factorint

number = 510143758735509025530880200653196460532653147

factors = factorint(number)

primes = list(factors.keys())

smaller_prime = min(primes)

print(smaller_prime)