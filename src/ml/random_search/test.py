
from random_search import RandomSearch

def fn(x, y):
    return x*x + y*y + 2

def sq(x):
    return x*x + 1


print("for f(x) = x^2 + 1")
rs = RandomSearch(sq, 0.05, [3], 2)
value, inputs = rs.run()
print(f"inputs -> {inputs}")
print(f"value -> {value}")


print("\n\nfor f(x, y) = x^2 + y^2 + 2")
rs = RandomSearch(fn, 0.01, [3, 4], 1, step_count=50, guess_count=400)
value, inputs = rs.run()
print(f"inputs -> {inputs}")
print(f"value -> {value}")

