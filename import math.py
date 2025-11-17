import math

def fitness_tracker():
    
    calories_per_min = float(input("Enter calories burned per minute: "))
    workout_minutes = int(input("Enter workout time in minutes: "))
    steps = int(input("Enter number of steps: "))

    total_tablets = int(input("Enter total number of tablets: "))
    pack_size = int(input("Enter number of tablets per pack: "))

    distance_km = (calories_per_min * workout_minutes * steps) / 1300

  
    hours = workout_minutes // 60
    minutes = workout_minutes % 60

    leftover_tablets = total_tablets % pack_size

    recovery_rate = 120 * (0.9 ** 5)

    print("\n--- Fitness Tracker Summary ---")
    print(f"Distance covered: {distance_km:.2f} km")
    print(f"Workout duration: {hours} hour(s) and {minutes} minute(s)")
    print(f"Leftover tablets after packing: {leftover_tablets}")
    print(f"Recovery heart rate after 5 minutes: {recovery_rate:.2f} bpm")


fitness_tracker()
    