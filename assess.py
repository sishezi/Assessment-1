def grade_average(grades):
    """ Write a program that returns the average number of a given list of grades.
    It should not add any negative grades to the average.

    Args:
        grades (list): List of grades to calculate
    """
    for grade in grades:
        if grade < 0:
            return "Unexpected output"
        if grade > 0:
            return sum(grades)/len(grades)
print(grade_average([1,2,3,4,5]))
        
        


def find_prime_factors(number):
    """Write code to return the prime factors of the number. 

    Args:
        number (int): Number to find the prime factors of
    """
    prime_factors = []
    if number == 1 and number % number == 0:
        return number
    else:
        return number + 1
print(find_prime_factors(6))



def calculate_interest(principal, rate, years):
    """Write a program that returns the compound interest

    Args:
        principal (int): The principal amount
        rate (int): The interest rate
        years (int): The amount of years to calculate the interest for
    """
    compound_per_year = 6
    total_amount = principal * (1 +(rate/compound_per_year)) ** (years*compound_per_year)

    compound_interest = total_amount - principal
    return compound_interest
print(calculate_interest(650,0.07,3))


def code_word(code):
    """Write a program that returns the word given a code.

    e.g. Given code: [3,1,20]
    Expected Word: "cat"

    Args:
        code (list): The code to decipher
    """
    codes = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
        10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
        18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

    word = ''.join([codes[num] for num in code])
    return word
print(code_word([3, 1, 20]))


def triangles(length):
    """Write a program that returns a triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    ***
    ****
    *****

    Args:
        length (int): The ;ength your triangle should be
    """


def hollow_triangle(length):
    """Write a program that returns a hollow triangle of a certain length

    e.g. Input length = 5

    Expected Output: 
    *
    **
    * *
    *  *
    *****

    Args:
        length (int): The ;ength your triangle should be
    """


# There are no tests for this function so test by running the program. 
def number_guessing(number):
    """Write a guessing game. The player has 10 opprtunites to guess.

    e.g. Number: 4
         User Input: 5
         Output: Incorrect

         Number: 4
         User Input: 4
         Output: Correct

    Args:
        number (int): The number to be guessed
    """

