age = int(input("Enter patients age in years: "))
weight = float(input("Enter patient weight in kg: "))

if age > 12 and weight > 40:
    print("Safe to give medication")
else:
    print("Not safe to give medication")