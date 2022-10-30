a = lambda x: x == x + 'Гений'
b = lambda x: x == x + 'Сврхразум'
c = lambda x: x == 'Просто' + x

d = input()
if d[-1] == 'а' or 'я' or 'г' or 'м':
    print(a(d))
elif d[-1] == 'о' or 'ь' or "л" or 'н':
    print(b(d))
else:
    print(c(d))
