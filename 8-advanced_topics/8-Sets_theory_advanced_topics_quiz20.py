import random

questions = [
    {
        "question": "What is the Cartesian product of two sets A and B?",
        "options": [
            "A. The set of elements that are in both A and B",
            "B. The set of ordered pairs where the first element is from A and the second from B",
            "C. The set of elements that are in A but not in B",
            "D. The set of elements that are in either A or B but not both"
        ],
        "answer": "B",
        "explanation": "The Cartesian product of two sets A and B is the set of ordered pairs where the first element is from A and the second from B."
    },
    {
        "question": "Which of the following is true about a relation in set theory?",
        "options": [
            "A. A relation is a set of ordered pairs",
            "B. A relation is always a function",
            "C. A relation is a subset of the power set of a set",
            "D. A relation always maps every element of one set to exactly one element of another set"
        ],
        "answer": "A",
        "explanation": "A relation between two sets is defined as a set of ordered pairs, where the first element is from the first set and the second from the second set."
    },
    {
        "question": "Which of the following describes a function in set theory?",
        "options": [
            "A. A function is a relation where each element of the first set is related to at least one element of the second set",
            "B. A function is a relation where each element of the first set is related to exactly one element of the second set",
            "C. A function is a set of ordered pairs where the first element is from the second set",
            "D. A function is always surjective"
        ],
        "answer": "B",
        "explanation": "A function is a relation where each element of the first set is related to exactly one element of the second set."
    },
    {
        "question": "Which of the following is an example of a partition of a set?",
        "options": [
            "A. A set divided into non-empty disjoint subsets",
            "B. A set divided into equal-sized subsets",
            "C. A set of all subsets of a given set",
            "D. A set that contains only elements of the universal set"
        ],
        "answer": "A",
        "explanation": "A partition of a set is a collection of non-empty, disjoint subsets that together cover the entire set."
    },
    {
        "question": "What does an indexed set represent?",
        "options": [
            "A. A set that contains only indexed elements",
            "B. A set where each element is associated with an index from a given set",
            "C. A set of ordered pairs",
            "D. A set of functions from one set to another"
        ],
        "answer": "B",
        "explanation": "An indexed set is a set where each element is associated with an index from a given set, often used in defining families of sets or functions."
    },
    {
        "question": "Which of the following is a key axiom in set theory?",
        "options": [
            "A. The Axiom of Choice",
            "B. The Axiom of Pairing",
            "C. The Axiom of Infinity",
            "D. All of the above"
        ],
        "answer": "D",
        "explanation": "The Axiom of Choice, Axiom of Pairing, and Axiom of Infinity are all key axioms in set theory."
    },
    {
        "question": "The Cartesian product of sets A and B is denoted as A × B. What does this product represent?",
        "options": [
            "A. The set of all subsets of A and B",
            "B. The set of all pairs (a, b) where a ∈ A and b ∈ B",
            "C. The union of sets A and B",
            "D. The intersection of sets A and B"
        ],
        "answer": "B",
        "explanation": "The Cartesian product A × B is the set of all ordered pairs (a, b) where a is an element of A and b is an element of B."
    },
    {
        "question": "Which of the following is a characteristic of a surjective function?",
        "options": [
            "A. Each element in the domain has a unique image in the codomain",
            "B. Every element of the codomain is the image of some element of the domain",
            "C. Every element of the domain maps to a different element of the codomain",
            "D. There is a one-to-one correspondence between elements of the domain and the codomain"
        ],
        "answer": "B",
        "explanation": "A surjective function maps every element of the codomain to some element of the domain."
    },
    {
        "question": "Which of the following describes a bijective function?",
        "options": [
            "A. A function that is both injective and surjective",
            "B. A function that is injective but not surjective",
            "C. A function that is surjective but not injective",
            "D. A function that is neither injective nor surjective"
        ],
        "answer": "A",
        "explanation": "A bijective function is one that is both injective (one-to-one) and surjective (onto)."
    },
    {
        "question": "In set theory, a relation on a set is reflexive if...",
        "options": [
            "A. Every element is related to itself",
            "B. The relation is symmetric",
            "C. The relation is transitive",
            "D. Every pair in the relation is ordered"
        ],
        "answer": "A",
        "explanation": "A relation on a set is reflexive if every element of the set is related to itself."
    },
    {
        "question": "A function is injective if...",
        "options": [
            "A. Every element of the domain maps to a different element of the codomain",
            "B. Every element of the codomain is mapped by exactly one element from the domain",
            "C. Every element of the domain maps to at least one element in the codomain",
            "D. There is no relationship between domain and codomain"
        ],
        "answer": "A",
        "explanation": "An injective function (one-to-one) maps each element of the domain to a distinct element in the codomain."
    },
    {
        "question": "What is the Axiom of Choice in set theory?",
        "options": [
            "A. Every set can be uniquely represented by its power set",
            "B. Any set can be paired with another set",
            "C. Given a set of non-empty sets, there exists a choice function that selects one element from each set",
            "D. Every set contains a subset that is itself a set"
        ],
        "answer": "C",
        "explanation": "The Axiom of Choice states that for any set of non-empty sets, there exists a function that selects one element from each set."
    },
    {
        "question": "Which of the following describes a partition of a set?",
        "options": [
            "A. A collection of disjoint sets whose union is the original set",
            "B. A set that divides all elements into two equal parts",
            "C. A set with all elements being equal",
            "D. A set containing only subsets of a given set"
        ],
        "answer": "A",
        "explanation": "A partition of a set is a collection of non-empty disjoint subsets whose union is the original set."
    },
    {
        "question": "Which of the following is true for indexed sets?",
        "options": [
            "A. Each element in the indexed set is associated with a specific index",
            "B. Indexed sets cannot contain functions",
            "C. Indexed sets are always finite",
            "D. Indexed sets are not used in mathematics"
        ],
        "answer": "A",
        "explanation": "In indexed sets, each element is associated with an index from a given index set."
    },
    {
        "question": "What is the set-theoretic definition of a relation?",
        "options": [
            "A. A relation is a function that maps one set to another",
            "B. A relation is a set of ordered pairs",
            "C. A relation is a set of subsets of a set",
            "D. A relation is always symmetric"
        ],
        "answer": "B",
        "explanation": "A relation between two sets is a set of ordered pairs, where the first element is from the first set and the second from the second set."
    },
    {
        "question": "In set theory, the axiom of pairing states that...",
        "options": [
            "A. For any two sets, there exists a set that contains exactly those two sets",
            "B. Every set can be paired with itself",
            "C. Every set has an equal-sized subset",
            "D. Any two sets can be merged into a single set"
        ],
        "answer": "A",
        "explanation": "The Axiom of Pairing asserts that for any two sets, there exists a set that contains exactly those two sets."
    },
    {
        "question": "Which of the following describes the Axiom of Infinity?",
        "options": [
            "A. There exists a set that contains at least one element and is closed under the successor operation",
            "B. Every set is finite",
            "C. Every set has a unique element",
            "D. Sets can be infinitely large"
        ],
        "answer": "A",
        "explanation": "The Axiom of Infinity asserts the existence of a set that contains at least one element and is closed under the successor operation."
    },
    {
        "question": "In the context of functions, what does the term 'domain' refer to?",
        "options": [
            "A. The set of all possible outputs of a function",
            "B. The set of all possible inputs for a function",
            "C. The set of all ordered pairs in a function",
            "D. The range of a function"
        ],
        "answer": "B",
        "explanation": "The domain of a function refers to the set of all possible inputs for that function."
    },
    {
        "question": "Which of the following is true for a transitive relation?",
        "options": [
            "A. If a is related to b and b is related to c, then a is related to c",
            "B. If a is related to b, then b must be related to c",
            "C. If a is related to b, then c must be related to d",
            "D. A transitive relation is always reflexive"
        ],
        "answer": "A",
        "explanation": "A relation is transitive if whenever a is related to b, and b is related to c, then a must also be related to c."
    },
    {
        "question": "What is the power set of a set?",
        "options": [
            "A. The set of all subsets of a given set",
            "B. The set of all elements in a set",
            "C. The set containing only the universal set",
            "D. The set of all functions on the set"
        ],
        "answer": "A",
        "explanation": "The power set of a set is the set of all subsets of the given set, including the empty set and the set itself."
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
