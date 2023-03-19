qu_ticket = int(input("Укажите, сколько билетов Вы хотите приобрести:"))
prices = []
for i in range(0, qu_ticket, 1):
    age = int(input(f"Введите возраст участника конференции № {i+1}:"))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
    prices.append(price)
full_price = sum(prices)
print("Сумма к оплате: ", full_price)
if qu_ticket > 3:
    full_price = 0.9 * full_price
    print("Сумма к оплате с учетом скидки: ", full_price)
