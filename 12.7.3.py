
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("введите сумму депозита:")

tkb = abs((per_cent['ТКБ'] * int(money) / 100))
skb = abs((per_cent['СКБ'] * int(money) / 100))
vtb = abs((per_cent['ВТБ'] * int(money) / 100))
sbr = abs((per_cent['СБЕР'] * int(money) / 100))

deposit = [tkb, skb, vtb, sbr]
print("ТКБ, СКБ, ВТБ, СБЕР =", str(deposit).strip('[]'))
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
