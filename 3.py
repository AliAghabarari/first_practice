def abstract(x):
    if x < 0:
        x = -x
    return x

x = float(input("enter x: "))
y = float(input("enter y: "))

sign = input("enter sign: ")

if sign == 'sum':
    print(x + y)
elif sign == 'difference':
    print(abstract(x - y))
elif sign == 'multiple':
    print(x * y)
elif sign == 'divide':
    print(max(x, y) / min(x, y))