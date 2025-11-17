def run_quiz(questions):
    score = 0
    for question, options, correct_answer in questions:
        print("\n" + question)
        for option in options:
            print(option)

        answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    return score

quiz_questions = [ 
    (
        
        "what is the world's most reliable car brand?",
        ["A) Honda", "B) Toyota","C) Nissan","D) Mazda"],
        "B"
    ),
    
    (
        "what is the world's best selling car?",
        ["A) Ford Focus", "B) Volkswagen Golf", "C) Honda Civic", "D) Toyota Corolla"],
        "D"
    ),
    
    (
        "what is the worlds most reliable car?",
        ["A) Toyota Camry", "B) Toyota Prius", "C) Toyota Corolla", "D) Toyota Yaris"],
        "A"
    ),

    (
        "What is toyotas fastest car",
        ["A) Toyota GR Corolla", "B) Toyota GR Yaris", "C) Toyota Supra", "D) Toyota GR86"],
        "C"
    ),

    (
        "What was Toyotas first hybrid car",
        ["A) Toyota Tundra","B) Toyota Hilux","C) Toyota Prius", "D) Toyota Aygo"],
        "C"
    ),
]

print("Welcome to the Python Quiz! ")
print("You’ll be asked 5 questions. Let’s see how many you can get right!")

score = run_quiz(quiz_questions)

print(f"\nYour final score is {score} out of {len(quiz_questions)} ")

if score == len(quiz_questions):
 


