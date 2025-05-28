from sympy import symbols
x, y = symbols('x y')
bieuthuc = x + y
giatri = bieuthuc.subs({x: y, y: 3})
print("Giá trị biểu thức sau khi thay thế:", giatri)
