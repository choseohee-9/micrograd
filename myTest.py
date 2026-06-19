from micrograd.engine import Value

a = Value(-4.0)
b = Value(2.0)

c = a + b
d = a * b + b**3

print(c)
print(d)