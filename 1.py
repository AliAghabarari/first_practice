value = input("write your input: ")

h = 0

print(value)
x = len(value)
if value[0] == '[' and value[x - 1] == ']':
    print('the value is a list')
    h = 1

else:
    p = 0
    for i in value:
        if 48 <= ord(i) and ord(i) <= 57:
            p += 1
    if p == x:
        print('value is an integer')
        h = 1
    
    else:
        s = 0
        for i in range (x):
            if value[i] == '.':
                s += 1
                r = i
        if s == 1:
            value1 = value
            value1 = list(value1)
            value1.pop(r)
            value2 = value1[0]
            for i in range(1, x - 1):
                value2 += value1[i]
            print(value2)
            s = 0
            for i in value2:
                if 48 <= ord(i) and ord(i) <= 57:
                    s += 1
            if s == len(value2):
                print('value is a float')
                h = 1

if h == 0:
    print('value is a string')

