streak = 0
Correct_answer = True
def correct(streak):
    if Correct_answer == True:
        streak += 1
        return streak
def incorrect(streak):
    correct_answer=False
    if Correct_answer == False:
        return streak
if streak := correct(streak):
    print(f"Streak after correct answer: {streak}")
Correct_answer = False
if streak := incorrect(streak):
    print(f"Your Streak, {streak}, Try Again")