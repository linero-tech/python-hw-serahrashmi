from to_do import TODO


def task9(sentence, character):
    result = sentence.lower().count(character.lower())
    if result > 0:
        return "true"
    else:
        return "false"


if __name__ == "__main__":
    print(task9("I code in KOTLIN", "I"))
    print(task9("summer is beautiful", "y"))
