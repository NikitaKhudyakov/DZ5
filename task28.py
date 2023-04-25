def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)

a = int(input("Число 1:  "))
b = int(input("Число 2:  "))
print(f"Сумма - {sum(a,b)}")
