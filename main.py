a = input("Номер первого числа: ")
a = int(a)
b = input("Номер второго числа: ")
b = int(b)

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print("Ответ: ", a + b)