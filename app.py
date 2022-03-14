
import listOfFunctions as funcs



while True:

    funcs.print_instructions()
    try:
        option = int(input(':: '))

        if option == 1:
            funcs.swap_numbers()
            continue

        if option == 2:
            number = int(input('Input any number: '))
            funcs.checkNumberType(number)
            continue

        if option == 3:
            number = int(input('Input number: '))
            summation = funcs.getSummation(number)
            print(f'The sum of the series is: {summation}')
            continue

        if option == 4:
            number = int(input('Input lowest search limit of prime numbers: '))
            prime_numbers = funcs.lookPrimeNumbers(number)
            print(f'The prime numbers between 1 to {number} are: {prime_numbers}')
            continue

        if option == 5:
            number = int(input('Input number: '))
            factorial = funcs.factorial(number)
            print(f'The product of the series is: {factorial}')

        if option == 0:
            print('Closing App')
            break
        else:
            print('Invalid Input')
            continue
    except ValueError:
        print('\nInvalid input type please input only within the given range of instructions')
        continue