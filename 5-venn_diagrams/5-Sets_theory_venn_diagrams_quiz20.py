import random

questions = [
    {
        "question": "What does the union of two sets A and B in a Venn diagram represent?",
        "options": [
            "A. Elements only in A",
            "B. Elements only in B",
            "C. Elements in A, B, or both",
            "D. Elements common to both A and B"
        ],
        "answer": "C",
        "explanation": "The union of two sets includes all elements in A, in B, or in both."
    },
    {
        "question": "In a Venn diagram, what does the intersection of two sets represent?",
        "options": [
            "A. Elements in A but not in B",
            "B. Elements in B but not in A",
            "C. Elements that are in both sets",
            "D. All elements in A and B"
        ],
        "answer": "C",
        "explanation": "The intersection of two sets represents the elements that are common to both sets."
    },
    {
        "question": "In a Venn diagram, which area represents the complement of a set?",
        "options": [
            "A. The area outside the set",
            "B. The area inside the set",
            "C. The union of two sets",
            "D. The intersection of two sets"
        ],
        "answer": "A",
        "explanation": "The complement of a set includes all elements not in the set, represented by the area outside the set."
    },
    {
        "question": "If A = {1, 2, 3} and B = {2, 3, 4}, what is the intersection of A and B in a Venn diagram?",
        "options": [
            "A. {1, 2}",
            "B. {2, 3}",
            "C. {3, 4}",
            "D. {1, 4}"
        ],
        "answer": "B",
        "explanation": "The intersection of sets A and B is {2, 3}, the common elements."
    },
    {
        "question": "In a Venn diagram with three sets A, B, and C, what does the triple intersection represent?",
        "options": [
            "A. Elements only in A",
            "B. Elements common to A, B, and C",
            "C. Elements in A and B but not C",
            "D. Elements in only one of the sets"
        ],
        "answer": "B",
        "explanation": "The triple intersection represents the elements that are common to sets A, B, and C."
    },
    {
        "question": "What does the symmetric difference of two sets A and B represent in a Venn diagram?",
        "options": [
            "A. The elements in both A and B",
            "B. The elements in A or B but not in both",
            "C. The elements that are only in A",
            "D. The elements that are only in B"
        ],
        "answer": "B",
        "explanation": "The symmetric difference includes elements in A or B, but not in both."
    },
    {
        "question": "What is represented by the area outside of all three sets in a three-set Venn diagram?",
        "options": [
            "A. The union of all sets",
            "B. The complement of all sets",
            "C. The intersection of all sets",
            "D. The difference of sets"
        ],
        "answer": "B",
        "explanation": "The area outside of all three sets represents the complement of all sets, meaning all elements not in A, B, or C."
    },
    {
        "question": "In a Venn diagram, the difference A − B represents which region?",
        "options": [
            "A. Elements in A but not in B",
            "B. Elements in B but not in A",
            "C. Elements common to A and B",
            "D. All elements in A and B"
        ],
        "answer": "A",
        "explanation": "A − B represents elements that are in A but not in B."
    },
    {
        "question": "Which of the following best describes the union of three sets A, B, and C in a Venn diagram?",
        "options": [
            "A. The area where all three sets overlap",
            "B. The area outside the sets",
            "C. The entire area covered by all three sets",
            "D. The intersection of all three sets"
        ],
        "answer": "C",
        "explanation": "The union of three sets includes all elements in A, B, or C, covering the entire area of all three sets."
    },
    {
        "question": "In a Venn diagram with three sets A, B, and C, what does the union of A and the complement of B represent?",
        "options": [
            "A. All elements in A but not B",
            "B. All elements in B but not A",
            "C. Elements in A or not in B",
            "D. The symmetric difference between A and B"
        ],
        "answer": "C",
        "explanation": "The union of A and the complement of B includes elements in A or elements not in B."
    },
    {
        "question": "In a Venn diagram, which operation is represented by the area that includes both A and B but excludes their intersection?",
        "options": [
            "A. A − B",
            "B. B − A",
            "C. (A ∪ B) − (A ∩ B)",
            "D. A ∩ B"
        ],
        "answer": "C",
        "explanation": "This represents the symmetric difference between A and B, which includes elements in A or B but not in both."
    },
    {
        "question": "In a Venn diagram, what does the area inside A but outside B represent?",
        "options": [
            "A. A ∩ B",
            "B. A − B",
            "C. A ∪ B",
            "D. B − A"
        ],
        "answer": "B",
        "explanation": "The area inside A but outside B represents the difference A − B."
    },
    {
        "question": "If A and B are disjoint sets in a Venn diagram, what does that imply?",
        "options": [
            "A. A and B have no elements in common",
            "B. A and B are equal",
            "C. A and B have at least one common element",
            "D. A is a subset of B"
        ],
        "answer": "A",
        "explanation": "Disjoint sets have no elements in common, so their intersection is empty."
    },
    {
        "question": "What does the universal set represent in a Venn diagram?",
        "options": [
            "A. The set of all elements being considered",
            "B. The set that contains no elements",
            "C. A set that contains only one element",
            "D. The intersection of all sets"
        ],
        "answer": "A",
        "explanation": "The universal set contains all the elements being considered in the context of the Venn diagram."
    },
    {
        "question": "In a Venn diagram, what does the region representing the intersection of A and B but excluding C represent?",
        "options": [
            "A. (A ∩ B) − C",
            "B. (A ∪ B) − C",
            "C. A ∩ B ∩ C",
            "D. A − B − C"
        ],
        "answer": "A",
        "explanation": "This region represents the intersection of A and B, excluding any elements in C."
    },
    {
        "question": "If A = {1, 2, 3} and B = {2, 3, 4}, what is the union of A and B in a Venn diagram?",
        "options": [
            "A. {1, 2}",
            "B. {2, 3}",
            "C. {1, 2, 3, 4}",
            "D. {3, 4}"
        ],
        "answer": "C",
        "explanation": "The union of A and B is the set of all elements in A, B, or both, which is {1, 2, 3, 4}."
    },
    {
        "question": "What does the symmetric difference between two sets A and B look like in a Venn diagram?",
        "options": [
            "A. The area inside both A and B",
            "B. The area inside A or B but not both",
            "C. The area outside both A and B",
            "D. The entire area covered by A and B"
        ],
        "answer": "B",
        "explanation": "The symmetric difference includes elements in A or B but not in both."
    },
    {
        "question": "If A = {1, 2} and B = {2, 3}, what is the complement of A in a universal set U = {1, 2, 3, 4}?",
        "options": [
            "A. {1}",
            "B. {2}",
            "C. {3, 4}",
            "D. {1, 2}"
        ],
        "answer": "C",
        "explanation": "The complement of A with respect to the universal set U is {3, 4}, the elements not in A."
    },
    {
        "question": "What is the intersection of a set A with the empty set in a Venn diagram?",
        "options": [
            "A. A",
            "B. ∅",
            "C. U",
            "D. A ∪ ∅"
        ],
        "answer": "B",
        "explanation": "The intersection of any set A with the empty set is always the empty set (∅)."
    },
    {
        "question": "What does the union of a set A with the universal set U represent in a Venn diagram?",
        "options": [
            "A. A",
            "B. U",
            "C. ∅",
            "D. A ∩ U"
        ],
        "answer": "B",
        "explanation": "The union of any set A with the universal set U is always the universal set (U)."
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
