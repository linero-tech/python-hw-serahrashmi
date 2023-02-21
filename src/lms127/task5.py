from to_do import TODO


def task5(value_for_a, value_for_b):
    c = value_for_a
    value_for_a = value_for_b
    value_for_b = c
    return value_for_a, value_for_b


if __name__ == "__main__":
    print(task5(1, 2))
