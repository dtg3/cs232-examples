"""Prime Number Checker

This program determines if an input number is
prime or not. If the number is determined not
to be prime, the first factors are shown.
"""


def checkPrime(number):
    """Checks if a number is prime

    Args:
        number (int): Number to be evaluated as prime or not
    Returns:
        None: In the absence of factors
        List: The first two factors if present
    """
    # Assume that we will not have any factors
    factors = None

    # Prime numbers need to be:
    # 1.) greater than one
    # 2.) have factors other than 1 and themselves
    if number > 1:
        # check for factors
        for factor in range(2, number):
            # If a division does not produce a remainder
            # then we have found a valid factor
            if (number % factor) == 0:
                factors = (factor, number // factor)
                break

    return factors


if __name__ == "__main__":
    print("****** PRIME CHECKER ******")

    # By default, input() treats everything like text.
    # We need to use int() to cast the value to an
    # integer type.
    inputNumber = int(input("Please enter an integer: "))
    factors = checkPrime(inputNumber)

    if factors:
        print(f"Factors found: {factors[0]} * {factors[1]} = {inputNumber}")
    else:
        print(f"{inputNumber} is prime")
