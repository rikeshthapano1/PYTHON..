question = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter"
}

score = 0 
for q, a in question.items():
    user_answer = input(q + " ")
    if user_answer.strip().lower() == a.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {a}.") 
print (f"Your final score is {score}/{len(question)}.") 

