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
"""
1. Input the number x 
2. Input the value y 
3. if x is greater than y 
   print x
4. else print y 
"""