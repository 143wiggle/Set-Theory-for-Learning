# Sets_theory_basic_concepts_quiz20.py

def ask_question(question, options, correct_answer, explanation):
    print(question)
    for option in options:
        print(option)
    
    answer = input("\nYour answer (a/b/c/d): ").lower()
    
    if answer == correct_answer:
        print(f"Correct! {explanation}\n")
        return 1  # Correct answer
    else:
        print(f"Incorrect. {explanation}\n")
        return 0  # Incorrect answer

def main():
    score = 0
    total_questions = 20

    # Question 1: Definition of a set
    q1 = "1. What is the correct definition of a set?"
    options1 = ["a) A collection of ordered elements.",
                "b) A well-defined collection of distinct objects.",
                "c) A collection of numbers only.",
                "d) A collection of any type of object without any specific rules."]
    correct1 = 'b'
    explanation1 = "A set is a well-defined collection of distinct objects, which can be numbers, letters, or any other objects."
    
    score += ask_question(q1, options1, correct1, explanation1)

    # Question 2: Elements and Membership
    q2 = "2. Which of the following is NOT a set?"
    options2 = ["a) A = {1, 2, 3}",
                "b) B = {a, b, c}",
                "c) C = (1, 2, 3)",
                "d) D = {a, b, a}"]
    correct2 = 'c'
    explanation2 = "The set C = (1, 2, 3) is not a set notation, it's a tuple (ordered collection), while the other options are valid sets."
    
    score += ask_question(q2, options2, correct2, explanation2)

    # Question 3: Elements and Membership
    q3 = "3. Which of the following is the correct notation for '3 is an element of set A'?"
    options3 = ["a) 3 ∈ A",
                "b) A ∈ 3",
                "c) 3 ∉ A",
                "d) A ⊆ 3"]
    correct3 = 'a'
    explanation3 = "The correct notation for '3 is an element of set A' is '3 ∈ A'."
    
    score += ask_question(q3, options3, correct3, explanation3)

    # Question 4: Finite vs Infinite Sets
    q4 = "4. Which of the following is an example of an infinite set?"
    options4 = ["a) A = {1, 2, 3}",
                "b) B = ℕ (Natural numbers)",
                "c) C = {a, b, c, d}",
                "d) D = {}"]
    correct4 = 'b'
    explanation4 = "The set of natural numbers (ℕ) is infinite, while the other sets are finite."
    
    score += ask_question(q4, options4, correct4, explanation4)

    # Question 5: Equal Sets
    q5 = "5. Are the following two sets equal?\nA = {1, 2, 3}\nB = {3, 2, 1}"
    options5 = ["a) Yes, A = B",
                "b) No, A ≠ B"]
    correct5 = 'a'
    explanation5 = "Sets do not consider the order of elements, so A = {1, 2, 3} and B = {3, 2, 1} are equal sets."
    
    score += ask_question(q5, options5, correct5, explanation5)

    # Question 6: Subsets
    q6 = "6. Which of the following sets is a subset of A = {1, 2, 3}?"
    options6 = ["a) {1, 3}",
                "b) {1, 4}",
                "c) {4, 5}",
                "d) {1, 2, 3, 4}"]
    correct6 = 'a'
    explanation6 = "{1, 3} is a subset of {1, 2, 3} because every element of {1, 3} is also in {1, 2, 3}."
    
    score += ask_question(q6, options6, correct6, explanation6)

    # Question 7: Universal Set
    q7 = "7. What does the universal set U represent?"
    options7 = ["a) A set that contains no elements.",
                "b) A set that contains all possible elements under consideration.",
                "c) A set with only one element.",
                "d) A set that contains only numbers."]
    correct7 = 'b'
    explanation7 = "The universal set contains all the elements under consideration, relative to a particular context."
    
    score += ask_question(q7, options7, correct7, explanation7)

    # Question 8: Empty Set
    q8 = "8. Which of the following is the representation of the empty set?"
    options8 = ["a) {}",
                "b) {}",
                "c) ∅",
                "d) ( )"]
    correct8 = 'c'
    explanation8 = "The empty set is represented as ∅, indicating a set with no elements."
    
    score += ask_question(q8, options8, correct8, explanation8)

    # Question 9: Power Set
    q9 = "9. What is the power set of A = {1, 2}?"
    options9 = ["a) {{1}, {2}, {1, 2}}",
                "b) {1, 2, 3}",
                "c) {{1}, {2}}",
                "d) {1, 2}"]
    correct9 = 'a'
    explanation9 = "The power set of A = {1, 2} is the set of all subsets of A, which includes {1}, {2}, and {1, 2}."
    
    score += ask_question(q9, options9, correct9, explanation9)

    # Question 10: Cardinality
    q10 = "10. What is the cardinality of set A = {a, b, c}?"
    options10 = ["a) 1",
                 "b) 2",
                 "c) 3",
                 "d) 4"]
    correct10 = 'c'
    explanation10 = "The cardinality of a set is the number of elements in the set. A = {a, b, c} has 3 elements."
    
    score += ask_question(q10, options10, correct10, explanation10)

    # Question 11: Set Builder Notation
    q11 = "11. Which of the following is the correct set builder notation for the set {1, 2, 3}?"
    options11 = ["a) {x | x is a natural number less than 4}",
                 "b) {x | x ∈ ℕ, x > 3}",
                 "c) {x | x ≤ 3}",
                 "d) {x | x ∈ ℕ}"]
    correct11 = 'a'
    explanation11 = "The set builder notation {x | x is a natural number less than 4} represents the set {1, 2, 3}."
    
    score += ask_question(q11, options11, correct11, explanation11)

    # Question 12: Disjoint Sets
    q12 = "12. What does it mean if two sets are disjoint?"
    options12 = ["a) They have no elements in common.",
                 "b) They have exactly one element in common.",
                 "c) They have some elements in common.",
                 "d) They are equal sets."]
    correct12 = 'a'
    explanation12 = "Disjoint sets have no elements in common."
    
    score += ask_question(q12, options12, correct12, explanation12)

    # Question 13: Overlapping Sets
    q13 = "13. Which of the following sets are overlapping?"
    options13 = ["a) A = {1, 2}, B = {2, 3}",
                 "b) A = {1, 2}, B = {3, 4}",
                 "c) A = {1, 2}, B = {3, 4}",
                 "d) A = {1, 2}, B = {5, 6}"]
    correct13 = 'a'
    explanation13 = "A and B overlap because they share the element '2'."
    
    score += ask_question(q13, options13, correct13, explanation13)

    # Question 14: Complementary Sets
    q14 = "14. What is the complement of a set A?"
    options14 = ["a) The set of all elements not in A.",
                 "b) The set of all elements in A.",
                 "c) The set of all elements in the universal set.",
                 "d) The empty set."]
    correct14 = 'a'
    explanation14 = "The complement of set A consists of all elements that are not in A, relative to the universal set."
    
    score += ask_question(q14, options14, correct14, explanation14)

    # Question 15: Symmetric Difference
    q15 = "15. What is the symmetric difference of two sets A and B?"
    options15 = ["a) Elements in both A and B.",
                 "b) Elements in either A or B, but not in both.",
                 "c) Elements in A or B.",
                 "d) The intersection of A and B."]
    correct15 = 'b'
    explanation15 = "The symmetric difference of sets A and B includes elements that are in either A or B, but not in both."
    
    score += ask_question(q15, options15, correct15, explanation15)

    # Question 16: Associative Law
    q16 = "16. Which of the following is an example of the associative law of union?"
    options16 = ["a) (A ∪ B) ∪ C = A ∪ (B ∪ C)",
                 "b) A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
                 "c) A ∪ B = B ∪ A",
                 "d) A ∩ B = B ∩ A"]
    correct16 = 'a'
    explanation16 = "The associative law states that the grouping of sets doesn't affect the union result."
    
    score += ask_question(q16, options16, correct16, explanation16)

    # Question 17: Commutative Law
    q17 = "17. Which of the following is an example of the commutative law of intersection?"
    options17 = ["a) A ∩ B = B ∩ A",
                 "b) A ∩ B = A ∪ B",
                 "c) A ∪ B = B ∪ A",
                 "d) A ∩ B = A ∩ C"]
    correct17 = 'a'
    explanation17 = "The commutative law states that the order of sets in intersection does not affect the result."
    
    score += ask_question(q17, options17, correct17, explanation17)

    # Question 18: Identity Law
    q18 = "18. What does the identity law of sets state?"
    options18 = ["a) A ∪ ∅ = A",
                 "b) A ∩ ∅ = A",
                 "c) A ∪ A = A",
                 "d) A ∩ A = ∅"]
    correct18 = 'a'
    explanation18 = "The identity law states that the union of a set with the empty set equals the set itself."
    
    score += ask_question(q18, options18, correct18, explanation18)

    # Question 19: Distribution Law
    q19 = "19. What does the distribution law of sets state?"
    options19 = ["a) A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
                 "b) A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
                 "c) A ∩ (B ∪ C) = A ∩ B ∪ C",
                 "d) A ∪ B = B ∪ A"]
    correct19 = 'a'
    explanation19 = "The distribution law states that the intersection of a set with the union of two sets can be distributed over the union."
    
    score += ask_question(q19, options19, correct19, explanation19)

    # Question 20: De Morgan's Laws
    q20 = "20. What does De Morgan's law state about set complements?"
    options20 = ["a) (A ∪ B)' = A' ∩ B'",
                 "b) (A ∩ B)' = A' ∪ B'",
                 "c) Both a and b",
                 "d) Neither a nor b"]
    correct20 = 'c'
    explanation20 = "De Morgan's laws state that the complement of a union is the intersection of the complements, and vice versa."
    
    score += ask_question(q20, options20, correct20, explanation20)

    print(f"Your total score is: {score}/{total_questions}")

if __name__ == "__main__":
    main()
