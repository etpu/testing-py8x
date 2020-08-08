balance = 0


def main():
    print("Добро пожаловать в банкомат")
    print("1 Баланс, 2 Внести, 3 Снять")
    x = int(input("Введите число (от 1 до 3):"))
    if x == 1:
        balances()
    elif x == 2:
        add_money()
    elif x == 3:
        remove_money()
    else:
        print("Ошибка. Попробуйте снова.")
        input("")


def balances():
    print(f"На вашем счете {balance} руб.")
    input("")


def add_money():
    global balance
    balance += int(input("Введите сумму которую хотите положить:"))
    input("")


def remove_money():
    global balance
    kredit = int(input("Введите сумму которую хотите снять:"))
    if kredit > balance:
        print("На вашем счете недостаточно средств!")
    else:
        balance -= kredit
    input("")


while True:
    main()
