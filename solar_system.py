def solar_system_quiz():
    questions = {
        "1. What is the largest planet in our solar system?": "Jupiter",
        "2. Which planet is known as the Red Planet?": "Mars",
        "3. Which planet is closest to the Sun?": "Mercury",
        "4. What planet is known for its beautiful rings?": "Saturn",
        "5. Which planet is known as the Earth's twin?": "Venus",
        "6. Which dwarf planet is located in the asteroid belt?": "Ceres",
        "7. Which planet has the most moons?": "Saturn",
        "8. What is the name of the largest moon of Saturn?": "Titan",
        "9. Which planet's day is longer than its year?": "Venus",
        "10. What is the smallest planet in our solar system?": "Mercury"
    }
    
    score = 0
    print("Welcome to the Solar System Quiz!")
    print("Please answer the following questions:\n")

    for question, correct_answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.\n")
    
    print(f"Quiz completed!")
    print(f"Your final score is {score} out of 10.")
    if score == 10:
        print("Perfect score! You're a solar system expert!")
    elif score >= 7:
        print("Great job! You know a lot about our solar system!")
    elif score >= 5:
        print("Not bad, but consider brushing up on your solar system knowledge.")
    else:
        print("It looks like you could use some more study on the solar system.")

if __name__ == "__main__":
    solar_system_quiz()
