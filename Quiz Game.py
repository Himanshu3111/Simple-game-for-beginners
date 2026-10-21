questions = [
    ("What is the capital of India?", "delhi"),
    ("How many days are in a week?", "7"),
    ("What color is the sky on a clear day?", "blue"),
    ("What is 5 + 3?", "8"),
    ("Which animal is called the king of the jungle?", "lion"),
]

score = 0

print("Welcome to the Quiz Game!")
print()

for question, answer in questions:
    reply = input(question + " ").lower()

    if reply == answer:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong. The answer is", answer)
    print()

print("Your score is", score, "out of", len(questions))

if score == len(questions):
    print("Great! You got everything right!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
