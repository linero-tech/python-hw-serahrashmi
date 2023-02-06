from to_do import TODO


def task4():
    return """
START
INPUT x 
INPUT y
OUTCOME
IF x=y
    OUTCOME "Equal"
    END
IF x>y
    OUTCOME = x
ELSE 
    OUTCOME = y
print(OUTCOME)
END
"""
