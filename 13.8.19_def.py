age = []

tnum = int(input("Введите количество билетов:"))
while len(age) < tnum:
    age_imput = int(input("Введите возраст посетителя:"))
    age.append(age_imput)

def summ(bil_def, age_def):
    price = 0
    for age_imput in age_def:
        if 18 <= age_imput < 25:
            price = price + 990
        if age_imput >= 25:
            price = price + 1390
    if bil_def <= 3:
        price_result = price
    else:
        price_result = price * 0.9
    return price_result

print(summ(tnum, age))
