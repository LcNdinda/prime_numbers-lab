
while True:
    number = input("Please enter a number:") # take inputs from user

    is_prime = True # boolean

    print 3 > 7

    # loop ranges from 2 to number
    for factor in range(2, int(number ** 0.5)):
        if number % factor == 0:
            is_prime = False
            break


    if is_prime == True:
        print "%d is a prime number!" %number

    else:
        print "%d is NOT a prime number" %number
