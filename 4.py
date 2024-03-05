def change(x, y, temp):
    if x == 'C' and y == 'F':
        t = (temp * 9 / 5) + 32
    elif x == 'F' and y == 'C':
        t = (temp - 32) * 5 / 9
    return t

temp = int(input("enter temperature: "))
x = input("enter first type: ")
y = input("enter second type: ")

print(change(x, y, temp))