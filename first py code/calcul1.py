x = int(input("Первое число: "))
math = input("Операция: ")
y = int(input("Второе число: "))

if x == 0 or y == 0:
    print("Значение не может быть равна к нулю")
elif math == '+':
    print(x, " + ", y, " = ", (x + y))
elif math == '-':
    print(x, " - ", y, " = ", (x - y))
elif math == '*':
    print(x, " * ", y, " = ", (x * y))
elif math == '/':
    print(x, " / ", y, " = ", (x / y))
else:
    print("Неверная операция")