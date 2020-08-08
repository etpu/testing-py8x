from random import randint
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suits = ["♠", "♥", "♦", "♣"]
nope = ["n", "N", "no", "No", "нет", "Нет", "-", False, 0, "хватит", "стоп", "СТОП", "Хватит"]

cards = []

for value in values:
    for suit in suits:
        cards.append(str(value)+suit)

shuffle = set(cards)

count = 0

while shuffle:
    get = shuffle.pop()
    print("Карта:", get)
    first_simbol = get[0]
    if first_simbol == "J" or first_simbol == "Q" or first_simbol == "K" or first_simbol == "1":
        count += 10
    elif first_simbol == "A" and count > 10:
        count += 1
    elif first_simbol == "A" and count >= 10:
        count += 11
    else:
        count += int(first_simbol)

    print("Ваши очки:", count)
    go_next = input("Ещё? ")
    if go_next in nope:
        break

our = randint(17, 23)
print("У программы:", our)
# text_win = "Вы победили! Поздравляем!" if count > our or our != 21
# print(f"Ваш счет:", {count}, "У программы:", {our})
print("All cards off")
