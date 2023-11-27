def main():
    try:
        number = int(input("Is it a prime number?:"))  # User inputs a number.
        prime_checker(number)  # Calls function to check if the number is prime.
    except ValueError:
        print("Please enter an integer.")  # Error message if input is not an integer.

def prime_checker(number):
    is_prime = True  # Assumes the number is prime until proven otherwise.
    if number <= 1:  # Numbers less than or equal to 1 are not prime.
        is_prime = False
    for i in range(2, number):  # Check divisibility of number from 2 to one less than the number.
        if number % i == 0:  # If divisible, number is not prime.
            is_prime = False
    # Display result.
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

if __name__ == "__main__":
    main()  # Starts the program.
