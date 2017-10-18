import sys
while True:
    x = sys.stdin.readline().strip()
    a = list(x.split())
    if a[1] == "?":
        break
    else:
        x = int(a[0])
        y = int(a[2])
        if a[1] == "+":
            print(x + y)
        elif a[1] == "-":
            print(x - y)
        elif a[1] == "*":
            print(x * y)
        elif a[1] == "/":
            print(x / y)
