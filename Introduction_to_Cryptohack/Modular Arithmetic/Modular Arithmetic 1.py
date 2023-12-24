def find_x(a, m):
    for x in range(m):
        if x % m == a % m:
            return x

a1 = 11
m1 = 6

x = find_x(a1, m1)

a2 = 8146798528947
m2 = 17

y = find_x(a2, m2)

solution = min(x, y)

print(f"The solution is: {solution}")
