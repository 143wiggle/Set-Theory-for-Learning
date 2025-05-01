# Sets_theory_types_of_sets_quiz20.py

quiz = [
    {
        "question": "1. What is a singleton set?",
        "options": {
            "A": "A set with exactly one element",
            "B": "A set with no elements",
            "C": "A set with infinite elements",
            "D": "A set with all natural numbers"
        },
        "answer": "A",
        "explanation": "A singleton set contains exactly one element."
    },
    {
        "question": "2. Which of the following sets is a singleton set?",
        "options": {
            "A": "{1, 2, 3}",
            "B": "{}",
            "C": "{0}",
            "D": "{a, b}"
        },
        "answer": "C",
        "explanation": "{0} contains only one element, hence it is a singleton set."
    },
    {
        "question": "3. What are disjoint sets?",
        "options": {
            "A": "Sets with some common elements",
            "B": "Sets with no common elements",
            "C": "Sets with one element",
            "D": "Sets that are subsets of each other"
        },
        "answer": "B",
        "explanation": "Disjoint sets do not share any elements."
    },
    {
        "question": "4. Which of the following is an example of disjoint sets?",
        "options": {
            "A": "{1, 2} and {2, 3}",
            "B": "{1, 3} and {3, 5}",
            "C": "{2, 4} and {6, 8}",
            "D": "{a, b} and {b, c}"
        },
        "answer": "C",
        "explanation": "{2, 4} and {6, 8} have no common elements, making them disjoint sets."
    },
    {
        "question": "5. What are overlapping sets?",
        "options": {
            "A": "Sets with no elements",
            "B": "Sets with at least one common element",
            "C": "Sets with exactly the same elements",
            "D": "Sets that are subsets of each other"
        },
        "answer": "B",
        "explanation": "Overlapping sets share at least one common element."
    },
    {
        "question": "6. Which of these is an example of overlapping sets?",
        "options": {
            "A": "{1, 2} and {3, 4}",
            "B": "{a} and {b}",
            "C": "{2, 4} and {4, 6}",
            "D": "{x} and {y}"
        },
        "answer": "C",
        "explanation": "{2, 4} and {4, 6} share the element 4, so they overlap."
    },
    {
        "question": "7. What is a complementary set?",
        "options": {
            "A": "A set that includes all elements",
            "B": "A set that is disjoint",
            "C": "A set that contains elements not in another set",
            "D": "A set with common elements"
        },
        "answer": "C",
        "explanation": "The complement of set A (A') includes all elements not in A, relative to a universal set."
    },
    {
        "question": "8. If A = {1,2,3} and U = {1,2,3,4,5}, what is the complement of A?",
        "options": {
            "A": "{1, 2, 3} ",
            "B": "{4, 5} ",
            "C": "{1, 2, 3, 4, 5} ",
            "D": "{}"
        },
        "answer": "B",
        "explanation": "Complement of A includes elements in the universal set U that are not in A."
    },
    {
        "question": "9. What are equivalent sets?",
        "options": {
            "A": "Sets that have the same elements",
            "B": "Sets that have the same number of elements",
            "C": "Sets that are subsets",
            "D": "Empty sets only"
        },
        "answer": "B",
        "explanation": "Equivalent sets have the same cardinality, meaning the same number of elements."
    },
    {
        "question": "10. Are sets {a, b} and {1, 2} equivalent?",
        "options": {
            "A": "Yes, because they have the same elements",
            "B": "No, because they are not numeric",
            "C": "Yes, because both have two elements",
            "D": "No, because one is alphabetic"
        },
        "answer": "C",
        "explanation": "They are equivalent because they each have two elements."
    },
    {
        "question": "11. Can singleton sets be disjoint?",
        "options": {
            "A": "Yes, if they contain different elements",
            "B": "No, singleton sets always overlap",
            "C": "Yes, if they contain numbers",
            "D": "No, singleton sets must be equal"
        },
        "answer": "A",
        "explanation": "Singleton sets are disjoint if they contain different elements."
    },
    {
        "question": "12. Which of the following best describes an overlapping relationship?",
        "options": {
            "A": "A ∩ B = ∅",
            "B": "A ∪ B = ∅",
            "C": "A ∩ B ≠ ∅",
            "D": "A = B"
        },
        "answer": "C",
        "explanation": "Overlapping sets have a non-empty intersection."
    },
    {
        "question": "13. What is the complement of a universal set?",
        "options": {
            "A": "The empty set",
            "B": "Itself",
            "C": "Any subset",
            "D": "An infinite set"
        },
        "answer": "A",
        "explanation": "The complement of a universal set is an empty set since no elements exist outside it."
    },
    {
        "question": "14. Which statement is true about equivalent sets?",
        "options": {
            "A": "They must have the same elements",
            "B": "They always overlap",
            "C": "They are disjoint",
            "D": "They have equal cardinality"
        },
        "answer": "D",
        "explanation": "Equivalent sets have equal cardinality."
    },
    {
        "question": "15. Which of the following best describes complementary sets?",
        "options": {
            "A": "Sets that share some common elements",
            "B": "Sets with only one element",
            "C": "Two sets that together make up the universal set with no overlap",
            "D": "Two identical sets"
        },
        "answer": "C",
        "explanation": "Complementary sets are two sets whose union is the universal set and whose intersection is the empty set."
    },
    {
        "question": "16. What is the result of the intersection of two disjoint sets?",
        "options": {
            "A": "The universal set",
            "B": "The larger of the two sets",
            "C": "An empty set",
            "D": "A singleton set"
        },
        "answer": "C",
        "explanation": "Disjoint sets have no elements in common, so their intersection is the empty set (∅)."
    },
    {
        "question": "17. If set A = {2} and set B = {2}, which statement is true?",
        "options": {
            "A": "A and B are overlapping sets",
            "B": "A and B are disjoint sets",
            "C": "A and B are equivalent and equal sets",
            "D": "A is a subset of B but not equal"
        },
        "answer": "C",
        "explanation": "Both sets contain the same single element, so they are equal and equivalent."
    },
    {
        "question": "18. Two sets with no elements in common are called:",
        "options": {
            "A": "Overlapping sets",
            "B": "Disjoint sets",
            "C": "Singleton sets",
            "D": "Complementary sets"
        },
        "answer": "B",
        "explanation": "By definition, disjoint sets have no shared elements."
    },
    {
        "question": "19. What makes a singleton set unique?",
        "options": {
            "A": "It contains infinite elements",
            "B": "It has only one element",
            "C": "It cannot be a subset",
            "D": "It is equal to the universal set"
        },
        "answer": "B",
        "explanation": "A singleton set has exactly one element, making it unique."
    },
    {
        "question": "20. Which of the following sets are equivalent?",
        "options": {
            "A": "{1, 2, 3} and {1, 3, 2}",
            "B": "{1, 2} and {2, 3}",
            "C": "{4, 5, 6} and {7, 8, 9}",
            "D": "{0} and {}"
        },
        "answer": "C",
        "explanation": "Equivalent sets have the same number of elements, regardless of the actual values. Both {4,5,6} and {7,8,9} have 3 elements."
    }
]

score = 0

for i, q in enumerate(quiz, 1):
    print(f"\nQuestion {i}: {q['question']}")
    for key, value in q['options'].items():
        print(f"  {key}. {value}")
    answer = input("Your answer: ").strip().upper()
    if answer == q['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")
    print(f"Explanation: {q['explanation']}")

print("\nQuiz complete!")
print(f"Your score: {score}/20")
if score == 20:
    print("Excellent! Perfect score.")
elif score >= 15:
    print("Great job! You understand the concepts well.")
elif score >= 10:
    print("Good effort, but review the material again.")
else:
    print("Consider revisiting the lessons and trying again.")
