a = lambda x: x + " Гений"
s = ''
while True:
    s = input()
    if s == "off":
        break
    else:
        print(a(s))

