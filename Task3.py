# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


balance = 10000
operations = []


def check_balance(amount):
    if amount <= balance:
        return True
    else:
        return False


def withdraw(amount):
    global balance, operations
    if check_balance(amount):
        balance -= amount
        operations.append(f'Снятие: {amount}')
        return True
    else:
        return False


def deposit(amount):
    global balance, operations
    balance += amount
    operations.append(f'Пополнение: {amount}')


def print_operations():
    global operations
    print('Последние операции:')
    for operation in operations:
        print(operation)


def exit_program():
    print('Программа завершена.')


while True:
    print('Сумма денег:', balance)
    action = input('\nВыберите действие (пополнить, снять, печать, выйти): ')

    if action == 'выйти':
        exit_program()
        break

    elif action == 'пополнить':
        amount = int(input('Введите сумму пополнения: '))
        if amount % 50 != 0:
            print('Сумма пополнения должна быть кратной 50 у.е.')
            continue

        deposit(amount)

        if len(operations) % 3 == 0:
            balance *= 1.03

    elif action == 'снять':
        amount = int(input('Введите сумму снятия: '))
        if amount % 50 != 0:
            print('Сумма снятия должна быть кратной 50 у.е.')
            continue

        if not withdraw(amount):
            print('Недостаточно средств на счете.')

    elif action == 'печать':
        print_operations()

    else:
        print('Некорректное действие. Попробуйте снова.')
        continue
