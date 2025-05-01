import random

questions = [
    {
        "question": "In database queries, which set operation is commonly used to combine the results of two queries?",
        "options": [
            "A. Intersection",
            "B. Union",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "B",
        "explanation": "The Union operation is used in database queries to combine the results of two queries, ensuring no duplicates in the final result."
    },
    {
        "question": "Which logic gate corresponds to the intersection of two sets?",
        "options": [
            "A. AND Gate",
            "B. OR Gate",
            "C. XOR Gate",
            "D. NOT Gate"
        ],
        "answer": "A",
        "explanation": "The AND gate corresponds to the intersection of two sets, as it outputs true only when both inputs are true (common elements in both sets)."
    },
    {
        "question": "Which set operation is often used in programming to find the common elements between two lists or arrays?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "B",
        "explanation": "In programming, the Intersection operation is used to find the common elements between two lists or arrays."
    },
    {
        "question": "In probability theory, the union of two events A and B represents which of the following?",
        "options": [
            "A. The probability of either event A or B happening",
            "B. The probability of both events A and B happening",
            "C. The complement of event A",
            "D. The difference between events A and B"
        ],
        "answer": "A",
        "explanation": "The Union of two events A and B represents the probability of either event A or event B happening."
    },
    {
        "question": "In survey analysis, which set operation is used to find individuals who belong to both groups being analyzed?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Complement",
            "D. Difference"
        ],
        "answer": "B",
        "explanation": "In survey analysis, the Intersection operation is used to find individuals who belong to both groups being analyzed."
    },
    {
        "question": "When analyzing exam-style problems, which set operation is commonly used to identify common questions in two different exam sets?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "B",
        "explanation": "The Intersection operation is used to find common questions in two different exam sets."
    },
    {
        "question": "Which set operation would be used to find students who are in one group but not the other in survey analysis?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Complement",
            "D. Difference"
        ],
        "answer": "D",
        "explanation": "The Difference operation is used to find students who are in one group but not in the other."
    },
    {
        "question": "Which operation can be used in programming to remove duplicates from two sets?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "A",
        "explanation": "The Union operation can be used in programming to combine two sets and remove duplicates, resulting in a set with unique elements."
    },
    {
        "question": "In probability theory, the complement of event A represents what?",
        "options": [
            "A. The event that A does not occur",
            "B. The event that A occurs",
            "C. The intersection of A and B",
            "D. The union of A and B"
        ],
        "answer": "A",
        "explanation": "The complement of event A represents the event that A does not occur, i.e., all outcomes that are not in A."
    },
    {
        "question": "Which set operation is used in programming to find elements that belong to either of two sets but not both?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Symmetric Difference",
            "D. Difference"
        ],
        "answer": "C",
        "explanation": "The Symmetric Difference operation is used to find elements that belong to either of two sets but not both."
    },
    {
        "question": "In a database query, which operation is used to find records that are in one set but not in another?",
        "options": [
            "A. Union",
            "B. Difference",
            "C. Intersection",
            "D. Symmetric Difference"
        ],
        "answer": "B",
        "explanation": "The Difference operation is used in database queries to find records that are in one set but not in another."
    },
    {
        "question": "In logic gates, which set operation is represented by an OR gate?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Symmetric Difference",
            "D. Complement"
        ],
        "answer": "A",
        "explanation": "The OR gate corresponds to the Union of sets, as it outputs true when at least one of the inputs is true."
    },
    {
        "question": "Which set operation is used in probability theory to find the likelihood that at least one of two events occurs?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "A",
        "explanation": "The Union operation in probability theory is used to calculate the probability that at least one of two events occurs."
    },
    {
        "question": "In programming, what does the difference between two sets A and B represent?",
        "options": [
            "A. The elements in A but not in B",
            "B. The common elements of A and B",
            "C. All elements in both A and B",
            "D. The elements in both A and B but not in A"
        ],
        "answer": "A",
        "explanation": "The Difference operation between two sets A and B represents all the elements in A but not in B."
    },
    {
        "question": "In survey analysis, which set operation would be used to find individuals who are in either group but not both?",
        "options": [
            "A. Intersection",
            "B. Symmetric Difference",
            "C. Difference",
            "D. Union"
        ],
        "answer": "B",
        "explanation": "The Symmetric Difference operation helps find individuals who are in either group but not both."
    },
    {
        "question": "In programming, if you need to identify elements that are common in two lists, which set operation would you use?",
        "options": [
            "A. Intersection",
            "B. Union",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "A",
        "explanation": "The Intersection operation in programming is used to find the common elements between two lists or sets."
    },
    {
        "question": "In probability theory, what does the intersection of two events A and B represent?",
        "options": [
            "A. The probability that both events A and B occur",
            "B. The probability that either event A or B occurs",
            "C. The complement of event A",
            "D. The difference between events A and B"
        ],
        "answer": "A",
        "explanation": "The Intersection operation in probability theory represents the probability that both events A and B occur."
    },
    {
        "question": "In a database query, which operation is used to find records that exist in both of two sets?",
        "options": [
            "A. Intersection",
            "B. Union",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "A",
        "explanation": "The Intersection operation is used in database queries to find records that exist in both of two sets."
    },
    {
        "question": "Which set operation would you use in survey analysis to find people who belong to either Group A or Group B but not both?",
        "options": [
            "A. Intersection",
            "B. Symmetric Difference",
            "C. Difference",
            "D. Union"
        ],
        "answer": "B",
        "explanation": "The Symmetric Difference operation helps find people who belong to Group A or Group B, but not both."
    },
    {
        "question": "Which set operation can be used to find the set of all outcomes that are not part of a given event A?",
        "options": [
            "A. Union",
            "B. Complement",
            "C. Difference",
            "D. Intersection"
        ],
        "answer": "B",
        "explanation": "The Complement operation is used to find the set of all outcomes that are not part of event A."
    }
]

random.shuffle(questions)
score = 0

for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")
    print("Explanation:", q['explanation'])

print("\nQuiz Complete!")
print(f"Your Score: {score}/20")
percentage = (score / 20) * 100
if percentage == 100:
    grade = "A+ (Perfect!)"
elif percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F (Try Again)"
print("Grade:", grade)
