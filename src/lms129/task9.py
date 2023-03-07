from to_do import TODO


def task9(temperature):

    if 'C' in temperature:
        c = int(temperature[:len(temperature)-1])
        f = (c * 9 / 5) + 32
        return str(f) + 'F'
    elif 'F' in temperature:
        print()


if __name__ == "__main__":
    print(task9('15C'))

