
firstName = input("Enter your first name")
print("hello" + firstName)

surname = input("enter your surname")
print("your surname is" + surname")

print("hello" + firstName + "  " + surname)

print("your initials are: " + firstName[0] + "  " + surname[0])

fullName = firstName + surname

print(surname.upper() + firstName)

print("you have " + str(len(firstName)) + "letters in your first name. In your surname you have "      + str(len(surname)) + " letters")

def createUserName():
     return surname[0:3] + firstName[0] + str(len(surname))


userName = createUserName()

print(username)









