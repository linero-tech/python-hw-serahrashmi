from to_do import TODO


def task4():
    index = 1
    result = 0

    while index <= 1000:
        if index % 9 == 0:
            result = result + index
        index = index + 1
    return result


if __name__ == "__main__":
    print(task4())
