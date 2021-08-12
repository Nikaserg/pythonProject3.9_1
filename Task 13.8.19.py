ticket = int(input("Введите необходимое кол-во билетов: "))

sum = 0
sum1 = 0
sum2 = 990
sum3 = 1390

for i in range (ticket):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum = sum + sum1
    elif 18 <= age < 25:
        sum = sum + sum2
    elif 25 <= age:
        sum = sum + sum3
if ticket > 3:
    sum = sum * (1 - 0.1)

print("Общая сумма к оплате составляет:", sum, "рублей")

