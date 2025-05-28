from sympy import Symbol, sin, cos, simplify, pprint
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print("Biểu thức ban đầu:")
pprint(bt)
print("\nBiểu thức sau khi rút gọn:")
pprint(bt_moi)
