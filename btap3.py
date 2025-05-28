from sympy import symbols
x, y = symbols('x y')
bieuthuc = x + y 
giatri = bieuthuc.subs({y: x}).subs({x: 3})
print("Gia tri bieu thuc sau khi thay the: ", giatri)
