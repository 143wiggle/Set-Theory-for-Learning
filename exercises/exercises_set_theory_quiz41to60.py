import random

questions = [
    # Questions 41 to 60
    {
        "question": "What is the union of the sets {1, 2} and {2, 3, 4}?",
        "options": [
            "A. {1, 2, 3, 4}",
            "B. {1, 2}",
            "C. {3, 4}",
            "D. {2, 3}"
        ],
        "answer": "A",
        "explanation": "The union of two sets includes all elements from both sets, without duplication. The union of {1, 2} and {2, 3, 4} is {1, 2, 3, 4}."
    },
    {
        "question": "Which of the following is a proper subset of {a, b, c}?",
        "options": [
            "A. {a, b}",
            "B. {a, b, c}",
            "C. {d}",
            "D. {a, b, c, d}"
        ],
        "answer": "A",
        "explanation": "A proper subset is a set that contains some, but not all, of the elements of the original set. {a, b} is a proper subset of {a, b, c}."
    },
    {
        "question": "Which operation results in a set of all elements that are in either set but not both?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Symmetric Difference",
            "D. Complement"
        ],
        "answer": "C",
        "explanation": "The symmetric difference of two sets includes all the elements that are in either set, but not both."
    },
    {
        "question": "Which set is the universal set if A = {1, 2, 3} and B = {2, 3, 4}?",
        "options": [
            "A. {1, 2, 3, 4}",
            "B. {1, 2, 3, 4, 5}",
            "C. {2, 3}",
            "D. {1, 2, 3}"
        ],
        "answer": "A",
        "explanation": "The universal set U should contain all elements that are present in any of the sets. For A and B, U = {1, 2, 3, 4}."
    },
    {
        "question": "Which of the following is an example of an equivalence relation?",
        "options": [
            "A. Reflexive, symmetric, and transitive relations",
            "B. Reflexive only",
            "C. Symmetric only",
            "D. Transitive only"
        ],
        "answer": "A",
        "explanation": "An equivalence relation is one that is reflexive, symmetric, and transitive."
    },
    {
        "question": "Which of the following is a result of applying the complement of a set twice?",
        "options": [
            "A. The original set",
            "B. An empty set",
            "C. The universal set",
            "D. A null set"
        ],
        "answer": "A",
        "explanation": "Applying the complement twice will bring you back to the original set, since the complement of the complement of a set is the set itself."
    },
    {
        "question": "What is the difference between the sets {a, b, c} and {b, c, d}?",
        "options": [
            "A. {a}",
            "B. {d}",
            "C. {a, d}",
            "D. {a, c, d}"
        ],
        "answer": "A",
        "explanation": "The difference between two sets consists of the elements in the first set that are not in the second set. The difference between {a, b, c} and {b, c, d} is {a}."
    },
    {
        "question": "Which of the following represents the identity element for the intersection operation?",
        "options": [
            "A. The universal set",
            "B. The empty set",
            "C. The set itself",
            "D. A non-empty set"
        ],
        "answer": "A",
        "explanation": "The identity element for the intersection operation is the universal set, as the intersection of any set with the universal set will give the original set itself."
    },
    {
        "question": "What does the symbol '⊆' represent in set theory?",
        "options": [
            "A. Subset",
            "B. Superset",
            "C. Union",
            "D. Intersection"
        ],
        "answer": "A",
        "explanation": "'⊆' represents a subset. If A ⊆ B, it means A is a subset of B."
    },
    {
        "question": "Which of the following is a true statement about disjoint sets?",
        "options": [
            "A. They have no common elements",
            "B. They have some common elements",
            "C. They are identical",
            "D. They are subsets of each other"
        ],
        "answer": "A",
        "explanation": "Disjoint sets are sets that do not share any common elements."
    },
    {
        "question": "If A = {1, 2, 3} and B = {2, 3, 4}, what is the symmetric difference of A and B?",
        "options": [
            "A. {1, 2, 4, 5}",
            "B. {3}",
            "C. {1, 2, 3, 4, 5}",
            "D. {4, 5}"
        ],
        "answer": "A",
        "explanation": "The symmetric difference between A and B consists of the elements that are in either A or B but not both. Hence, A Δ B = {1, 2, 4, 5}."
    },
    {
        "question": "Which of the following sets is a power set of {a, b}?",
        "options": [
            "A. { {}, {a}, {b}, {a, b} }",
            "B. { {a}, {b} }",
            "C. { {a, b} }",
            "D. {a, b}"
        ],
        "answer": "A",
        "explanation": "The power set of a set is the set of all subsets of that set, including the empty set and the set itself. The power set of {a, b} is { {}, {a}, {b}, {a, b} }."
    },
    {
        "question": "What does the symbol '∩' represent in set theory?",
        "options": [
            "A. Union",
            "B. Intersection",
            "C. Difference",
            "D. Complement"
        ],
        "answer": "B",
        "explanation": "'∩' represents the intersection of two sets. The intersection contains all elements common to both sets."
    },
    {
        "question": "If A = {1, 2, 3} and B = {2, 3, 4}, what is A ∩ B?",
        "options": [
            "A. {1, 2, 3, 4}",
            "B. {2, 3}",
            "C. {1}",
            "D. {3, 4}"
        ],
        "answer": "B",
        "explanation": "The intersection of two sets contains only the elements that are in both sets. A ∩ B = {2, 3}."
    },
    {
        "question": "What is the set of all subsets of a set called?",
        "options": [
            "A. Complement",
            "B. Power set",
            "C. Universal set",
            "D. Symmetric difference"
        ],
        "answer": "B",
        "explanation": "The power set of a set is the set of all its subsets, including the empty set and the set itself."
    },
    {
        "question": "Which of the following is a correct example of the associative law in set theory?",
        "options": [
            "A. (A ∪ B) ∪ C = A ∪ (B ∪ C)",
            "B. A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
            "C. A ∩ B = A ∪ B",
            "D. A ∪ Ø = Ø"
        ],
        "answer": "A",
        "explanation": "The associative law in set theory states that the grouping of sets in union or intersection does not affect the result. For example, (A ∪ B) ∪ C = A ∪ (B ∪ C)."
    },
    {
        "question": "What is the difference between the sets {1, 2, 3, 4} and {3, 4, 5, 6}?",
        "options": [
            "A. {1, 2}",
            "B. {5, 6}",
            "C. {1, 2, 5, 6}",
            "D. {1, 2, 3, 4, 5, 6}"
        ],
        "answer": "A",
        "explanation": "The difference between two sets consists of the elements that are in the first set but not in the second set. The difference between {1, 2, 3, 4} and {3, 4, 5, 6} is {1, 2}."
    },
    {
        "question": "What does the symbol '∅' represent in set theory?",
        "options": [
            "A. The universal set",
            "B. The empty set",
            "C. The complement of a set",
            "D. The set of all natural numbers"
        ],
        "answer": "B",
        "explanation": "'∅' represents the empty set, which is the set that contains no elements."
    },
    {
        "question": "What is the set of all possible outcomes in an experiment called?",
        "options": [
            "A. Sample space",
            "B. Power set",
            "C. Subset",
            "D. Universal set"
        ],
        "answer": "A",
        "explanation": "The sample space is the set of all possible outcomes in a given experiment."
    },
    {
        "question": "What is the result of A ∪ (A ∩ B)?",
        "options": [
            "A. A",
            "B. B",
            "C. A ∩ B",
            "D. Ø"
        ],
        "answer": "A",
        "explanation": "The result of A ∪ (A ∩ B) is A, because the intersection A ∩ B is already contained within A."
    }
]

# Shuffle the questions for randomness
random.shuffle(questions)
score = 0

# Loop through all the questions
for i, q in enumerate(questions):
    print(f"\nQuestion {i+41}: {q['question']}")
    for option in q['options']:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")
    print("Explanation:", q['explanation'])

# Final results
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
