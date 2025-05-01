import random

questions = [
    # Questions 1 to 20 (as you already have)
    {
        "question": "Which of the following represents a set of all natural numbers?",
        "options": [
            "A. {1, 2, 3, 4, 5, ...}",
            "B. {0, 1, 2, 3, 4, ...}",
            "C. {1, 2, 3, 4}",
            "D. {0, 1, 2, 3}"
        ],
        "answer": "A",
        "explanation": "The natural numbers are represented as {1, 2, 3, 4, 5, ...}."
    },
    {
        "question": "Which of the following sets is a subset of {1, 2, 3, 4}?",
        "options": [
            "A. {1, 2}",
            "B. {5, 6}",
            "C. {1, 5}",
            "D. {}"
        ],
        "answer": "A",
        "explanation": "A subset of a set consists of elements that are contained in the original set. {1, 2} is a subset of {1, 2, 3, 4}."
    },
    {
        "question": "What is the cardinality of the set {a, b, c, d}?",
        "options": [
            "A. 3",
            "B. 4",
            "C. 2",
            "D. 5"
        ],
        "answer": "B",
        "explanation": "The cardinality of a set is the number of elements it contains. The set {a, b, c, d} has 4 elements."
    },
    {
        "question": "What is the union of the sets {1, 2, 3} and {3, 4, 5}?",
        "options": [
            "A. {1, 2, 3, 4, 5}",
            "B. {3}",
            "C. {1, 2}",
            "D. {3, 4}"
        ],
        "answer": "A",
        "explanation": "The union of two sets includes all the elements from both sets without duplication. The union of {1, 2, 3} and {3, 4, 5} is {1, 2, 3, 4, 5}."
    },
    {
        "question": "What is the intersection of the sets {1, 2, 3} and {2, 3, 4}?",
        "options": [
            "A. {1, 2}",
            "B. {3}",
            "C. {2, 3}",
            "D. {1, 4}"
        ],
        "answer": "C",
        "explanation": "The intersection of two sets consists of elements that are common to both sets. The intersection of {1, 2, 3} and {2, 3, 4} is {2, 3}."
    },
    {
        "question": "What is the difference between the sets {1, 2, 3} and {2, 3, 4}?",
        "options": [
            "A. {1}",
            "B. {4}",
            "C. {1, 2, 3, 4}",
            "D. {1, 4}"
        ],
        "answer": "A",
        "explanation": "The difference between two sets consists of the elements that are in the first set but not in the second. The difference between {1, 2, 3} and {2, 3, 4} is {1}."
    },
    {
        "question": "What is the symmetric difference between {1, 2, 3} and {3, 4, 5}?",
        "options": [
            "A. {1, 2, 4, 5}",
            "B. {2, 3}",
            "C. {3, 4}",
            "D. {1, 5}"
        ],
        "answer": "A",
        "explanation": "The symmetric difference between two sets consists of elements that are in either set, but not both. The symmetric difference between {1, 2, 3} and {3, 4, 5} is {1, 2, 4, 5}."
    },
    {
        "question": "If A = {1, 2, 3} and B = {3, 4, 5}, what is the complement of A in the universal set U = {1, 2, 3, 4, 5}?",
        "options": [
            "A. {4, 5}",
            "B. {1, 2, 3}",
            "C. {2, 3}",
            "D. {}"
        ],
        "answer": "A",
        "explanation": "The complement of A in the universal set U consists of the elements in U that are not in A. The complement of A = {1, 2, 3} in U = {1, 2, 3, 4, 5} is {4, 5}."
    },
    {
        "question": "In a Venn diagram, what does the intersection of two sets represent?",
        "options": [
            "A. The elements that are in both sets",
            "B. The elements that are in either set",
            "C. The elements that are only in the first set",
            "D. The elements that are in neither set"
        ],
        "answer": "A",
        "explanation": "The intersection of two sets in a Venn diagram represents the elements that are common to both sets."
    },
    {
        "question": "What is the Venn diagram for the union of two sets A and B?",
        "options": [
            "A. A diagram showing two circles that overlap",
            "B. A diagram showing one large circle",
            "C. A diagram with one circle inside another",
            "D. A diagram with no overlap"
        ],
        "answer": "A",
        "explanation": "The Venn diagram for the union of two sets A and B shows two circles that overlap, representing all elements in A or B."
    },
    {
        "question": "Which of the following represents De Morgan's law for sets?",
        "options": [
            "A. (A ∩ B)' = A' ∪ B'",
            "B. A ∩ B = A' ∪ B'",
            "C. A ∪ B = A' ∩ B'",
            "D. A' ∩ B = A ∪ B'"
        ],
        "answer": "A",
        "explanation": "De Morgan's law states that the complement of the intersection of two sets is the union of their complements: (A ∩ B)' = A' ∪ B'."
    },
    {
        "question": "Which law states that the union of a set with the universal set is the universal set?",
        "options": [
            "A. Identity law",
            "B. Complement law",
            "C. Domination law",
            "D. Complementary law"
        ],
        "answer": "C",
        "explanation": "The domination law states that the union of a set with the universal set is the universal set: A ∪ U = U."
    },
    {
        "question": "Which of the following is a correct example of the identity law in set theory?",
        "options": [
            "A. A ∪ Ø = A",
            "B. A ∩ Ø = A",
            "C. A ∪ A = Ø",
            "D. A ∩ A = Ø"
        ],
        "answer": "A",
        "explanation": "The identity law states that the union of a set A with the empty set is A: A ∪ Ø = A."
    },
    {
        "question": "What is the complement of the set A = {1, 2, 3} in the universal set U = {1, 2, 3, 4, 5, 6}?",
        "options": [
            "A. {4, 5, 6}",
            "B. {1, 2}",
            "C. {2, 3}",
            "D. {1, 5, 6}"
        ],
        "answer": "A",
        "explanation": "The complement of A = {1, 2, 3} in the universal set U = {1, 2, 3, 4, 5, 6} is {4, 5, 6}."
    },
    {
        "question": "Which of the following is the correct statement about idempotent laws?",
        "options": [
            "A. A ∪ A = A",
            "B. A ∩ A = Ø",
            "C. A ∪ Ø = Ø",
            "D. A ∩ Ø = A"
        ],
        "answer": "A",
        "explanation": "The idempotent law states that the union of a set with itself is the set: A ∪ A = A."
    },
    {
        "question": "Which of the following is a correct statement of the domination law?",
        "options": [
            "A. A ∪ U = U",
            "B. A ∩ U = A",
            "C. A ∩ Ø = Ø",
            "D. A ∪ Ø = A"
        ],
        "answer": "A",
        "explanation": "The domination law states that the union of a set A with the universal set is the universal set: A ∪ U = U."
    },
    {
        "question": "Which of the following is true about a symmetric difference of two sets?",
        "options": [
            "A. It contains the elements that are in either of the sets, but not both",
            "B. It contains the elements that are in both sets",
            "C. It contains the elements that are in neither of the sets",
            "D. It is the intersection of the two sets"
        ],
        "answer": "A",
        "explanation": "The symmetric difference of two sets contains the elements that are in either of the sets, but not both."
    },
    {
        "question": "Which of the following is an example of an equivalence relation?",
        "options": [
            "A. Reflexive, symmetric, and transitive relations",
            "B. Reflexive and asymmetric relations",
            "C. Symmetric relations only",
            "D. Transitive relations only"
        ],
        "answer": "A",
        "explanation": "An equivalence relation is one that is reflexive, symmetric, and transitive."
    },
    {
        "question": "What is the complement of the set A = {a, b, c} in the universal set U = {a, b, c, d, e}?",
        "options": [
            "A. {d, e}",
            "B. {a, b}",
            "C. {c, d}",
            "D. {e}"
        ],
        "answer": "A",
        "explanation": "The complement of A = {a, b, c} in U = {a, b, c, d, e} is {d, e}."
    },
    {
        "question": "What is the symmetric difference between the sets {1, 3, 5} and {2, 3, 4}?",
        "options": [
            "A. {1, 2, 4, 5}",
            "B. {3}",
            "C. {1, 2}",
            "D. {4, 5}"
        ],
        "answer": "A",
        "explanation": "The symmetric difference between {1, 3, 5} and {2, 3, 4} is {1, 2, 4, 5}."
    }
]

# Shuffle the questions for randomness
random.shuffle(questions)
score = 0

# Loop through all the questions
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
