from geometry import Square, Circle, area_stats

s = Square(4)
c = Circle(3)

print(f"Square with side 4 has area: {s.area()}")
print(f"Circle with radius 3 has area: {c.area()}")

stats = area_stats(s, c)
print("Area stats summary:")
print(stats)