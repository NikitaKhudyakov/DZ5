def factor(a):
    if a == 0:
        return 1
    else:
        return (a*factor(a-1))

def sum(a):
    if a == 0:
        return a
    else:
        return (a+sum(a-1))

a = int(input("Число:  "))
print(f"Факториал - {factor(a)}")
print(f"Сумма - {sum(a)}")


