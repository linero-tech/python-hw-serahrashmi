from to_do import TODO


def task2(number):
    for i in range(2,number):
        if number % i == 0:
            print(i)
            result = False
            return result
    return True



if __name__ == "__main__":
    print(task2(17))
    print(task2(5))
    print(task2(9))