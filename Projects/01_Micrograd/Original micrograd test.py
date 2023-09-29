from micrograd.engine import Value

a = Value(2)
b = Value(3)
c = Value(4)
d = a + b * c
e = Value.relu(d)
e.backward()
print(a,b,d,c,d,e)

# c.backward()

# print(a, b, c)

# d = a * b + b**3
# c += c + 1
# c += 1 + c + (-a)
# d += d * 2 + (b + a).relu()
# d += 3 * d + (b - a).relu()
# e = c - d
# f = e**2
# g = f / 2.0
# g += 10.0 / f
# print(f'{g.data:.4f}') # prints 24.7041, the outcome of this forward pass
# g.backward()
# print(f'{a.grad:.4f}') # prints 138.8338, i.e. the numerical value of dg/da
# print(f'{b.grad:.4f}') # prints 645.5773, i.e. the numerical value of dg/db