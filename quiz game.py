"""
Quiz Game with Timer
--------------------
A Python-based multiple-choice quiz game.

Features:
- Shuffles questions every time you play.
- 15-second timer for each question.
- Validates user input (only numbers 1–4 are accepted).
- Shows correct answer if the user chooses wrong or runs out of time.
- Tracks score and gives performance feedback at the end.
"""

import random
import signal

# Function to handle timeout
def timeout_handler(signum, frame):
    raise TimeoutError

# Quiz data stored in a list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Berlin", "2. Paris", "3. Madrid", "4. Rome"],
        "answer": 2
    },
    {
        "question": "Which programming language is known as the 'mother of all languages'?",
        "options": ["1. C", "2. Python", "3. Java", "4. Pascal"],
        "answer": 1
    },
    {
        "question": "What is the square root of 64?",
        "options": ["1. 6", "2. 8", "3. 7", "4. 9"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["1. Charles Dickens", "2. J.K. Rowling", "3. William Shakespeare", "4. Mark Twain"],
        "answer": 3
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["1. CO2", "2. O2", "3. H2O", "4. NaCl"],
        "answer": 3
    }
]

# Function to ask a question and get user's answer with timer
def ask_question(question_data, question_number):
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print(option)

    # Set signal for 15-second timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(15)

    try:
        answer = int(input("Enter your answer (1-4) within 15 seconds: "))
        signal.alarm(0)  # Cancel alarm after input
        if 1 <= answer <= 4:
            return answer
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")
            return None
    except TimeoutError:
        print("\n⏰ Time’s up!")
        return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

# Main function to run the quiz game
def run_quiz():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions (you have 15 seconds each):\n")
    score = 0

    # Shuffle questions for randomness
    random.shuffle(quiz_questions)

    for i, question_data in enumerate(quiz_questions, start=1):
        user_answer = ask_question(question_data, i)
        if user_answer == question_data["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            correct_option = question_data["options"][question_data["answer"] - 1]
            print(f"❌ Wrong! The correct answer was: {correct_option}")

    print(f"\nYour final score is: {score}/{len(quiz_questions)}")
    if score == len(quiz_questions):
        print("🏆 Excellent! You're a genius!")
    elif score >= len(quiz_questions) // 2:
        print("👍 Good job! Keep learning.")
    else:
        print("📘 Better luck next time!")

# Run the game
if __name__ == "__main__":
    run_quiz()
