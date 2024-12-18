print("Welcome")
money = 0
Correct_answer = True
def correct(money):
    if Correct_answer == True:
        money += 100
        return money
def incorrect(money):
    correct_answer=False
    if Correct_answer == False:
        money -= 100
        return money
if money := correct(money):
    print(f"Money after correct answer: {money}")
Correct_answer = False
if money := incorrect(money):
    print(f"Money after incorrect answer; {money}")