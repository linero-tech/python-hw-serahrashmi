from to_do import TODO


def task1(a, b):
    result = 0
    if a >= b:
        return 0
    while a <= b:
        result = result + a
        a = a + 1
    return result


if __name__ == "__main__":
    print(task1(1, 5))
    print(task1(3, 3))



