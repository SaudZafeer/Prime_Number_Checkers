#created a function to check prime numbers
def check_prime(number : int):
    flag = False
    if number > 1:
        for previous_numbers in range(2,number):
            if (number % previous_numbers) == 0:
                flag = True
                break
    if flag:
        print('Not a prime number') 
    else:
        print('Prime number')    

user_input = int(input('please enter a numebr to check if it is prime or not: '))
check_prime(user_input)
