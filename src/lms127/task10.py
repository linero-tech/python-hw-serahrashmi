from to_do import TODO


def task10_1(assessments):
    result = len(assessments) * 1
    return result


def task10_2(assessments):
    return len(assessments[3])


def task10_3(assessments):
    return int(len(assessments)/2)


def task10_4(assessments):
    result = len(assessments[0:3])
    return result


if __name__ == "__main__":
    print(task10_1("LMHHF"))
    print(task10_2("LMFHMF"))
    print(task10_3("LMFHM"))
    print(task10_4("LMFHM"))
