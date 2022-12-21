age = []

tnum = int(input("Введите количество билетов:"))
while len(age) < tnum:
    age_imput = int(input("Введите возраст посетителя:"))
    age.append(age_imput)
price = 0

for age_imput in age:
    if 18 <= age_imput < 25:
        price = price + 990
    if age_imput >= 25:
        price = price + 1390
if tnum <= 3:
    print(price)
else:
    print(price * 0.9)

