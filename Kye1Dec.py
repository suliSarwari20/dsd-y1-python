import random
score = random.randint (1000)
username = input("enter name")
with open ("scores.txt","a") as file:
    data = score , " " , username,"\n"
    file.write(str(data))