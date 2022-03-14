
# instructions
def print_instructions():
    print("""
        Hello and Welcome! 

        [1] to swap two input numbers
        [2] to check number type (even/odd)
        [3] to get summation of a series
        [4] to look for prime numbers 
        [5] to get the factorial of number
        [0] to exit
    
    """)


# number 1
def swap_numbers():
    first_num = int(input('input 1st number: '))
    second_num = int(input('input 2ns number: '))
    print(f'Before swapping: 1st = {first_num}, 2nd = {second_num}')
    first_num, second_num = second_num, first_num
    print(f'After swapping: 1st = {first_num}, 2nd = {second_num}')


# number 2
def checkNumberType(num: int):
    if num % 2 == 0:
        print('Expected Output: The entered number is EVEN')
    else:
        print('Expected Output: The entered number is ODD')


# number 3
def getSummation(series_range: int):
    series = [i+1 for i in range(series_range)]
    print(series)
    summation = sum(series)
    return summation


# number 4
def lookPrimeNumbers(num: int):
    prime_numbers = [1]
    is_prime = False
    for i in range(num+1):
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break 
            is_prime = True
        if is_prime:
            prime_numbers.append(i)

    return prime_numbers


# number 5
def factorial(num: int):
    if num == 1:
        return num
    return (num * (factorial(num-1)) )


