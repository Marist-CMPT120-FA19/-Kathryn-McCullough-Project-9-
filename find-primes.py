
#name: Kathryn McCullough
#email: kathryn.mccullough1@marist.edu
#description: using Sieve Eratothenes equation to make a program that outputs the primes below a given number


def main():
    print("This program will output the prime numbers below the entered number.")
    print()
    print("Please enter a number greater than 2")
    print("as 2 is the first prime number in the sequence.")
    max_number= int(input("Insert the number that the list will end at: "))

    primes= []
    start = 2

    if max_number <2:
        print("PLEASE ENTER A NUMBER GREATER THAN 2")

    #range of numbers to search for prime
    #make sure to add +1 so the program includes the entered number if its a prime
    for num in range(start, max_number +1):
        not_prime= 0

        #go through list of known primes 
        for prime in primes:
            #check to see if previous prime divides evenly into current num, yes?>> not a prime
            if (num % prime) == 0:
                not_prime=1
                break

            #if the prime squared is bigger than num>> dont need to check anymore
            if prime*prime > num:
                break

        #add prime to list of known primes
        if not_prime != 1:
            primes.append(num)
            print(num)

main()
    
    
