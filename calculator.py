def calculate():
    operation=input('''
please type the mathematical operation you would like to complete:
                    + for addition
                    - for subtraction
                    * for multiplication
                    / for division
                    ''')
    
    num1=int(input("Enter First Number : "))
    num2=int(input("Enter Second Number : "))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        if number_2 != 0:
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        else:
            print("Error! Division by zero is not allowed.")

    else:
        print('You have not typed a valid operator, please run the program again.')

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('See you later.')

    else:
        again()

calculate()
