import math


def task3(number):
    result = 1
    initial_number = 1
    while initial_number <= number:
        result = result * initial_number
        initial_number = initial_number + 1
    return result


if __name__ == "__main__":
    print(task3(3))
    print(task3(10))
