def input_taker(typ, text):
    inp = input(text)
    if typ == 'int':
        return int(inp)
    else:
        return inp


def action_picker():
    print('choose action: 1- check balance 2- withdraw 3- deposit 4- close')
    action = input_taker(typ='', text='>>> ')
    return action


def check_user(users):
    login = input_taker('', 'write your login: ')
    password = input_taker('', 'write your password: ')
    if login == users['login'] and password == users['password']:
        return True
    else:
        print('login or password incorrect')
        return False


def main():
    print('Hello from Alatoo bank')
    balance_kg = 5000
    done = True
    user_data = {'login': 'johnny', 'password': '1234', 'name': 'John', 'surname': 'Smith', 'age': 20}
    while done:
        if check_user(user_data):
            action = action_picker()
        else:
            continue
        if action == '1':
            print(f'you have {balance_kg}c in your balance')
            done = func()

        elif action == '2':
            print(f'your latest balance is {balance_kg}')
            money2with = int(input('write amount: '))
            balance_kg = balance_kg - money2with
            print(f'your latest balance is {balance_kg}')
            done = func()

        elif action == '3':
            add = int(input('Write amount: '))
            balance_kg = balance_kg + add
            print(f'your latest balance is {balance_kg}')
            done = func()
        else:
            done = False


def func():
    ask = input('Do you want to continue? yes/no: ')
    if ask == 'yes':
        return True
    else:
        return False


if __name__ == '__main__':
    main()
