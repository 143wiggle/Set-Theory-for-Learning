import random

questions = [
    {
        "question": "Which law states that A ∪ B = B ∪ A?",
        "options": [
            "A. Commutative Law of Union",
            "B. Associative Law of Union",
            "C. Identity Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Commutative Law of Union states that A ∪ B = B ∪ A, meaning the order of sets in union does not matter."
    },
    {
        "question": "Which law states that A ∩ B = B ∩ A?",
        "options": [
            "A. Commutative Law of Intersection",
            "B. Distributive Law",
            "C. Identity Law",
            "D. De Morgan's Law"
        ],
        "answer": "A",
        "explanation": "The Commutative Law of Intersection states that A ∩ B = B ∩ A, meaning the order of sets in intersection does not matter."
    },
    {
        "question": "Which law describes A ∪ (B ∪ C) = (A ∪ B) ∪ C?",
        "options": [
            "A. Commutative Law",
            "B. Associative Law of Union",
            "C. Identity Law",
            "D. De Morgan's Law"
        ],
        "answer": "B",
        "explanation": "The Associative Law of Union states that the way we group sets in union does not affect the result."
    },
    {
        "question": "Which of the following is an example of the Distributive Law?",
        "options": [
            "A. A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
            "B. A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
            "C. A ∩ B = B ∩ A",
            "D. A ∪ B = B ∪ A"
        ],
        "answer": "A",
        "explanation": "The Distributive Law states that A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C). This allows distribution of operations."
    },
    {
        "question": "Which law states that A ∪ ∅ = A?",
        "options": [
            "A. Identity Law of Union",
            "B. Complement Law",
            "C. Domination Law",
            "D. Idempotent Law"
        ],
        "answer": "A",
        "explanation": "The Identity Law of Union states that the union of any set A with the empty set ∅ is always A."
    },
    {
        "question": "Which law states that A ∩ U = A?",
        "options": [
            "A. Identity Law of Intersection",
            "B. De Morgan's Law",
            "C. Domination Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Identity Law of Intersection states that the intersection of any set A with the universal set U is always A."
    },
    {
        "question": "Which law describes A ∪ A = A?",
        "options": [
            "A. Idempotent Law of Union",
            "B. Complement Law",
            "C. Commutative Law",
            "D. Identity Law"
        ],
        "answer": "A",
        "explanation": "The Idempotent Law of Union states that the union of a set A with itself is always A."
    },
    {
        "question": "Which law states that A ∩ A = A?",
        "options": [
            "A. Idempotent Law of Intersection",
            "B. Identity Law",
            "C. De Morgan's Law",
            "D. Domination Law"
        ],
        "answer": "A",
        "explanation": "The Idempotent Law of Intersection states that the intersection of a set A with itself is always A."
    },
    {
        "question": "Which law states that A ∪ A' = U?",
        "options": [
            "A. Complement Law",
            "B. Domination Law",
            "C. Identity Law",
            "D. Double Complement Law"
        ],
        "answer": "A",
        "explanation": "The Complement Law states that the union of a set A and its complement A' is the universal set U."
    },
    {
        "question": "Which law states that A ∩ A' = ∅?",
        "options": [
            "A. Complement Law",
            "B. Identity Law",
            "C. Idempotent Law",
            "D. Domination Law"
        ],
        "answer": "A",
        "explanation": "The Complement Law states that the intersection of a set A and its complement A' is always the empty set ∅."
    },
    {
        "question": "Which law is described by the equation (A ∪ B)' = A' ∩ B'?",
        "options": [
            "A. De Morgan's Law",
            "B. Complement Law",
            "C. Distributive Law",
            "D. Identity Law"
        ],
        "answer": "A",
        "explanation": "De Morgan's Law states that the complement of the union of two sets is equal to the intersection of their complements."
    },
    {
        "question": "Which law is described by the equation (A ∩ B)' = A' ∪ B'?",
        "options": [
            "A. De Morgan's Law",
            "B. Complement Law",
            "C. Idempotent Law",
            "D. Domination Law"
        ],
        "answer": "A",
        "explanation": "De Morgan's Law states that the complement of the intersection of two sets is equal to the union of their complements."
    },
    {
        "question": "Which law states that A ∪ (A ∩ B) = A?",
        "options": [
            "A. Absorption Law of Union",
            "B. Distributive Law",
            "C. Identity Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Absorption Law of Union states that the union of a set A with the intersection of A and B is always A."
    },
    {
        "question": "Which law states that A ∩ (A ∪ B) = A?",
        "options": [
            "A. Absorption Law of Intersection",
            "B. Complement Law",
            "C. Identity Law",
            "D. Idempotent Law"
        ],
        "answer": "A",
        "explanation": "The Absorption Law of Intersection states that the intersection of a set A with the union of A and B is always A."
    },
    {
        "question": "Which law states that A ∪ U = U?",
        "options": [
            "A. Domination Law of Union",
            "B. Identity Law",
            "C. Complement Law",
            "D. Double Complement Law"
        ],
        "answer": "A",
        "explanation": "The Domination Law of Union states that the union of any set A with the universal set U is always U."
    },
    {
        "question": "Which law states that A ∩ ∅ = ∅?",
        "options": [
            "A. Domination Law of Intersection",
            "B. Identity Law",
            "C. Complement Law",
            "D. Double Complement Law"
        ],
        "answer": "A",
        "explanation": "The Domination Law of Intersection states that the intersection of any set A with the empty set ∅ is always ∅."
    },
    {
        "question": "Which law describes the relationship A'' = A?",
        "options": [
            "A. Double Complement Law",
            "B. De Morgan's Law",
            "C. Idempotent Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Double Complement Law states that the complement of the complement of a set A is always A."
    },
    {
        "question": "Which law states that A ∪ (A' ∩ B) = A ∪ B?",
        "options": [
            "A. Absorption Law",
            "B. De Morgan's Law",
            "C. Identity Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Absorption Law states that A ∪ (A' ∩ B) = A ∪ B."
    },
    {
        "question": "Which law states that A ∩ (A' ∪ B) = A ∩ B?",
        "options": [
            "A. Absorption Law",
            "B. Distributive Law",
            "C. Identity Law",
            "D. Complement Law"
        ],
        "answer": "A",
        "explanation": "The Absorption Law states that A ∩ (A' ∪ B) = A ∩ B."
    },
    {
        "question": "Which law states that (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C)?",
        "options": [
            "A. Distributive Law of Intersection over Union",
            "B. Distributive Law of Union over Intersection",
            "C. Associative Law",
            "D. Commutative Law"
        ],
        "answer": "A",
        "explanation": "The Distributive Law of Intersection over Union states that (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C)."
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
