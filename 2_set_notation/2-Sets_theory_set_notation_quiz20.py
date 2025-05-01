import random

questions = [
    {
        "question": "Which of the following is a correct example of roster form?",
        "options": ["{1, 2, 3, 4}", "{x | x is a vowel in English}", "x > 2", "All integers"],
        "answer": "A",
        "explanation": "Roster form lists each element of the set explicitly."
    },
    {
        "question": "Which is not an example of roster form?",
        "options": ["{a, e, i, o, u}", "{x | x is a vowel in the English alphabet}", "{red, blue, green}", "{1, 2, 3}"],
        "answer": "B",
        "explanation": "This is set-builder notation, which defines a rule instead of listing elements."
    },
    {
        "question": "What does the set {x | x \u2208 \u2115, x < 4} represent?",
        "options": ["{0,1,2}", "{1,2,3,4}", "{1,2,3}", "{2,3,4}"],
        "answer": "C",
        "explanation": "The rule describes all natural numbers less than 4."
    },
    {
        "question": "What is a limitation of roster form?",
        "options": ["It becomes impractical for large or infinite sets", "It is not visual", "It is abstract", "It lacks any rules"],
        "answer": "A",
        "explanation": "Listing too many elements can be tedious or impossible."
    },
    {
        "question": "Which set is not written in set-builder notation?",
        "options": ["{x | x > 3}", "{x | x is even}", "{x | x \u2208 \u2124}", "{January, February, March}"],
        "answer": "D",
        "explanation": "That is roster form since the elements are explicitly listed."
    },
    {
        "question": "Which of the following is written in correct set-builder notation syntax?",
        "options": ["{x; x \u2208 \u2124, x > 0}", "{x | x \u2208 \u2124, x > 0}", "{x : x \u2208 \u2115 and x > 0}", "{All positive integers}"],
        "answer": "B",
        "explanation": "It uses the correct format: a variable, a vertical bar, and a condition."
    },
    {
        "question": "Which of the following best represents the set of even integers using set-builder notation?",
        "options": ["{x | x = 2n, n \u2208 \u2115}", "{x | x mod 2 = 0, x \u2208 \u2124}", "{2,4,6,8,...}", "{x \u2208 \u2124, x/2 \u2208 \u2124}"],
        "answer": "B",
        "explanation": "The condition clearly defines all even integers."
    },
    {
        "question": "The roster form {2,4,6,8,10} corresponds to which set-builder form?",
        "options": ["{x | x = 2n, n \u2208 \u2115, n \u2264 5}", "{x | x \u2208 \u2124, x > 1}", "{x | x \u2208 \u2115, x mod 2 = 0}", "{2n | n \u2208 \u2115 and n \u2264 5}"],
        "answer": "A",
        "explanation": "It generates the elements shown using a formula and domain."
    },
    {
        "question": "Which form is more compact for infinite sets?",
        "options": ["Roster form", "Enumeration", "Set-builder form", "Descriptive form"],
        "answer": "C",
        "explanation": "It uses rules instead of listing infinitely many elements."
    },
    {
        "question": "What does the set {x | x is a letter in the word 'APPLE'} contain?",
        "options": ["{A,P,P,L,E}", "{A,P,L,E}", "{P,L,E}", "{A,L,E}"],
        "answer": "B",
        "explanation": "Duplicate letters are removed in a set."
    },
    {
        "question": "In set-builder notation, what does the vertical bar '|' represent?",
        "options": ["Such that", "Given", "If", "Equals"],
        "answer": "A",
        "explanation": "It separates the variable from its condition."
    },
    {
        "question": "Which set is best expressed using roster form?",
        "options": ["All prime numbers", "All rational numbers", "The months of the year", "All real numbers"],
        "answer": "C",
        "explanation": "Finite, small sets are suited for roster form."
    },
    {
        "question": "Convert {x | x \u2208 \u2115, x \u2264 3} to roster form.",
        "options": ["{1,2,3,4}", "{1,2,3}", "{0,1,2,3}", "{2,3}"],
        "answer": "B",
        "explanation": "It includes natural numbers less than or equal to 3."
    },
    {
        "question": "Which of the following is a valid domain for set-builder notation?",
        "options": ["x in list", "x as integer", "x \u2208 \u2115", "x > 0"],
        "answer": "C",
        "explanation": "You must specify the universe where x belongs."
    },
    {
        "question": "What is the set {x | x \u2208 \u2124, -3 < x < 3} in roster form?",
        "options": ["{-3,-2,-1,0,1,2,3}", "{-2,-1,0,1,2}", "{-3,-2,-1,0,1,2}", "{-2,-1,0,1,2,3}"],
        "answer": "B",
        "explanation": "It includes integers between -3 and 3 exclusive."
    },
    {
        "question": "Which notation helps understand the structure or rule behind a set?",
        "options": ["Set-builder form", "Roster form", "Both", "None"],
        "answer": "A",
        "explanation": "Set-builder notation defines elements by their properties."
    },
    {
        "question": "Which notation is typically preferred for clearly displaying small finite sets?",
        "options": ["Set-builder form", "Roster form", "Both", "None"],
        "answer": "B",
        "explanation": "Roster form is better for small, familiar sets."
    },
    {
        "question": "In {x | x \u2208 \u211d, x\u00b2 = 4}, what is the roster form?",
        "options": ["{2}", "{4}", "{-2,2}", "{-4,4}"],
        "answer": "C",
        "explanation": "These are the real solutions to x\u00b2 = 4."
    },
    {
        "question": "Which form better communicates the pattern or formula for generating a set?",
        "options": ["Roster form", "Listing", "Enumeration", "Set-builder form"],
        "answer": "D",
        "explanation": "Set-builder form communicates rules, not just elements."
    },
    {
        "question": "Which of the following sets in set-builder form defines odd numbers?",
        "options": ["{x | x = 2n + 1, n \u2208 \u2124}", "{x | x mod 2 = 0, x \u2208 \u2124}", "{x | x is even}", "{2n, n \u2208 \u2124}"],
        "answer": "A",
        "explanation": "2n+1 generates all odd integers when n is any integer."
    }
]

def run_quiz():
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestion {idx}: {q['question']}")
        for i, option in enumerate(q['options'], ord('A')):
            print(f"  {chr(i)}. {option}")

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {q['answer']}")
        print("Explanation:", q['explanation'])

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/20")
    percentage = (score / 20) * 100
    print(f"Percentage: {percentage:.2f}%")
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

if __name__ == "__main__":
    run_quiz()
