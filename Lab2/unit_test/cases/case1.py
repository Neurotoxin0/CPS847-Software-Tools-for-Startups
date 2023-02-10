def fizzbuzz(number):
    """
    This function return specific string based on input number
    :param number: number to determine
    :return: result string
    """

    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

    return str(number)