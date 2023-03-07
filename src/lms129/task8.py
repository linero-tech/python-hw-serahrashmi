from to_do import TODO


def task8(number):
    result = 0

    while number != 0:
        result = result + number % 10
        number = number // 10
    return result


if __name__ == "__main__":
    print(task8(123))
    print(task8(124))
