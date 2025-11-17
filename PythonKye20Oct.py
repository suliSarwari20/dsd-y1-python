age = int(input("Enter your age"))
medical_clearence = input("Do you have a medical clearence? (yes/no): ").strip().lower()

if age > 18 or medical_clearence == "yes":
    print("Access granted: you may enter the immersive zone.")
else:
    print("Access denied: you cannot enter the imersive zone.")