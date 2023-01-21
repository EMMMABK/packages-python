first_number = int(input('Введите число:'))
second_number = int(input('Введите число:'))
operation = input('Введите действие(-,+,/,*) <- Я могу выполнить только вот эти действия')
def operation():
    if operation == '-':
        return first_number - second_number
    elif operation == '+':
        return first_number + second_number
    elif operation == '/':
        return first_number // second_number
    elif operation == '*':
        return first_number * second_number
    else:
        return 'Я не понимаю знак который вы написали'

operation()
