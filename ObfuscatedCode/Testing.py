import operator
def a(x):
    ops = {
        "+":operator.add,
        "-":operator.sub
    }

print(a(5+5-5))
print(operator.sub(5, 5))