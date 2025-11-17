def get_int(x):
    return int(input(x))
               
def get_float(x):
    return float(input(x))

def get_string(x):
    return str(input(x))

name = get_string("enter your name")
age = get_int("enter your age")
testScore = get_float("enter your test score")
passedExam = False

if age >= 16:
    if testScore >= 65:
        passedExam = True 

    elif testScore <= 65:
        passedExam = False

else:
    print(f'invalid test score')

