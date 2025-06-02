# Mini Quiz App

# Predefined multiple-choice quiz questions
quiz = {
    "What is the capital of Philippines?": {
        "options": ["A. Manila", "B. London", "C. Rome", "D. Madrid"],
        "answer": "A"
    },
    "How many island in Philippines?": {
        "options": ["A. 1", "B. 5,687", "C. 7,641", "D. 6,987"],
        "answer": "C"
    },
    "What is the largest ocean on Earth?": {
        "options": ["A. Atlantic", "B. Pacific", "C. Indian", "D. Arctic"],
        "answer": "B"
    },
    "Which language was used to code for this quiz?": {
        "options": ["A. HTML", "B. Python", "C. Java", "D. C++"],
        "answer": "B"
    },
    "Who wrote 'El Filibusterismo'?": {
        "options": ["A. Dr. Jose Rizal", "B. William Shakespeare", "C. Mark Twain", "D. J.K. Rowling"],
        "answer": "A"
    }
}

def run_quiz():
    score = 0
    print("\n--- Welcome to the Mini Quiz App ---")
    for question, data in quiz.items():
        print(f"\n{question}")
        for option in data["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == data["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {data['answer']}.")
    print(f"\n🎉 Quiz complete! Your final score is {score}/{len(quiz)}")

if __name__ == "__main__":
    run_quiz()
