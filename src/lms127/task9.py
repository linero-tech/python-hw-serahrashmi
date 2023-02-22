from to_do import TODO


def task9(sentence, character):
    lower_sentence = sentence.lower()
    lower_character = character.lower()
    result = lower_sentence.count(lower_character)
    if result > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(task9("I code In KOTLIN", "I"))
    print(task9("summer is beautiful", "I"))
