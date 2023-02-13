from to_do import TODO


def task9():
    return """
INPUT 
IF the ATM is out of service 
   THAN cant access ATM
ELSE Continue
    Insert the card in the slot 
    select the language on the screen
    Enter the four digit PIN 
    select the option as withdrawal 
    Enter the amount to be withdrawn
    Confirm the amount - (Step Continue)
    IF the PIN is correct
    IF amount is léss than or equal to the account balance  
    THEN release the money 
    ELSE No balance
    Print receipt 
    ELSE 
    PRINT(Incorrect PIN)
END 
"""
1. Insert card
2. INPUT CC code
3. IF code is invald
    1, OUTPUT error
    2. Return card
4. Output options to the user
5. IF option selected is withdraw
    3.Input the amount to withdraw
    4.IF the account balance is less than amount to withdraw
        1.OUTPUT Error
    5. ELSE
         1. Dispense money to user
         2. update user's' balance
         3. OUTPUT receipt
         4. Return the card
"""
