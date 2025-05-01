# Sets_theory_set_operations_quiz20.py

import random

questions = [
    {
        "question": "What does the union of two sets A and B contain?",
        "options": [
            "A. Only the elements common to both A and B",
            "B. All elements in A but not in B",
            "C. All elements in A or B or both",
            "D. Elements not in A or B"
        ],
        "answer": "C",
        "explanation": "The union of sets A and B contains all elements that are in A, in B, or in both."
    },
    {
        "question": "What is the symbol for intersection of sets?",
        "options": [
            "A. ∪",
            "B. ∩",
            "C. −",
            "D. ⊆"
        ],
        "answer": "B",
        "explanation": "The symbol ∩ represents the intersection of two sets, meaning elements common to both."
    },
    {
        "question": "Which of the following describes the difference A − B?",
        "options": [
            "A. Elements in B but not in A",
            "B. Elements in both A and B",
            "C. Elements in A but not in B",
            "D. All elements in A and B"
        ],
        "answer": "C",
        "explanation": "A − B includes all elements in A that are not in B."
    },
    {
        "question": "What is the symmetric difference of sets A and B?",
        "options": [
            "A. Elements in A or B, but not in both",
            "B. Elements only in A",
            "C. Elements in both A and B",
            "D. All elements in the universal set"
        ],
        "answer": "A",
        "explanation": "The symmetric difference includes elements in A or B, but not in both."
    },
    {
        "question": "Which operation finds all elements not in a set?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Complement",
            "D. Difference"
        ],
        "answer": "C",
        "explanation": "The complement of a set contains all elements not in the set, assuming a universal set."
    },
    {
        "question": "If A = {1,2,3} and B = {3,4,5}, what is A ∪ B?",
        "options": [
            "A. {3}",
            "B. {1,2,3,4,5}",
            "C. {1,2,4,5}",
            "D. {1,2,3}"
        ],
        "answer": "B",
        "explanation": "The union A ∪ B includes all elements from both sets without duplicates: {1,2,3,4,5}."
    },
    {
        "question": "If A = {1,2,3} and B = {3,4,5}, what is A ∩ B?",
        "options": [
            "A. {3}",
            "B. {1,2,3,4,5}",
            "C. {1,2}",
            "D. {4,5}"
        ],
        "answer": "A",
        "explanation": "The intersection A ∩ B contains only the elements common to both sets: {3}."
    },
    {
        "question": "What is (A ∪ B) − (A ∩ B) called?",
        "options": [
            "A. Complement",
            "B. Symmetric Difference",
            "C. Intersection",
            "D. Power Set"
        ],
        "answer": "B",
        "explanation": "The symmetric difference is defined as (A ∪ B) − (A ∩ B)."
    },
    {
        "question": "If U = {1,2,3,4,5} and A = {2,4}, what is the complement of A?",
        "options": [
            "A. {1,2,3,4,5}",
            "B. {2,4}",
            "C. {1,3,5}",
            "D. {1,2,4}"
        ],
        "answer": "C",
        "explanation": "The complement of A relative to U includes elements in U not in A: {1,3,5}."
    },
    {
        "question": "What is the result of A − A?",
        "options": [
            "A. A",
            "B. Empty Set",
            "C. Universal Set",
            "D. A ∪ A"
        ],
        "answer": "B",
        "explanation": "A − A is the set of elements in A that are not in A, which is an empty set."
    },
    {
        "question": "Which operation results in elements common to both sets?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Complement"
        ],
        "answer": "B",
        "explanation": "Intersection results in elements common to both sets."
    },
    {
        "question": "What is the complement of the universal set?",
        "options": [
            "A. Empty set",
            "B. Universal set",
            "C. Singleton set",
            "D. Set itself"
        ],
        "answer": "A",
        "explanation": "The complement of the universal set is the empty set since it includes everything."
    },
    {
        "question": "Which of these is always a subset of any set A?",
        "options": [
            "A. A itself",
            "B. Universal set",
            "C. Empty set",
            "D. Complement of A"
        ],
        "answer": "C",
        "explanation": "The empty set is a subset of every set."
    },
    {
        "question": "What symbol represents union?",
        "options": [
            "A. ∪",
            "B. ∩",
            "C. ⊂",
            "D. −"
        ],
        "answer": "A",
        "explanation": "The union of two sets is represented by the symbol ∪."
    },
    {
        "question": "If A = {1, 2, 3} and B = {3, 4}, what is A Δ B (symmetric difference)?",
        "options": [
            "A. {1, 2, 4}",
            "B. {3}",
            "C. {1, 2, 3, 4}",
            "D. {2, 4}"
        ],
        "answer": "A",
        "explanation": "Symmetric difference removes common elements: {1, 2, 4}."
    },
    {
        "question": "Which operation is not commutative?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Symmetric Difference"
        ],
        "answer": "C",
        "explanation": "Set difference A − B is not the same as B − A, so it's not commutative."
    },
    {
        "question": "What does A ∪ ∅ equal?",
        "options": [
            "A. A",
            "B. ∅",
            "C. A ∩ ∅",
            "D. Universal set"
        ],
        "answer": "A",
        "explanation": "Union with an empty set results in the original set."
    },
    {
        "question": "If A ∩ B = ∅, what does that mean?",
        "options": [
            "A. A and B are equal",
            "B. A is a subset of B",
            "C. A and B are disjoint",
            "D. B is a subset of A"
        ],
        "answer": "C",
        "explanation": "Disjoint sets have no elements in common."
    },
    {
        "question": "The complement of a complement of a set A is:",
        "options": [
            "A. ∅",
            "B. U",
            "C. A",
            "D. A ∪ A"
        ],
        "answer": "C",
        "explanation": "The complement of a complement returns the original set A."
    },
    {
        "question": "Which is true for any set A?",
        "options": [
            "A. A ∩ A = ∅",
            "B. A ∪ A = A",
            "C. A − A = A",
            "D. A ∩ ∅ = A"
        ],
        "answer": "B",
        "explanation": "Union of a set with itself is the set itself."
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
