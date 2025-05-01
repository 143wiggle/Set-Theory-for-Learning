def implication():
    # Prompting if you have a ticket
    you_have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower() == 'yes'
    party_happening = input("Is the party happening? (yes/no): ").strip().lower() == 'yes'
    
    # Checking the implication (If you have a ticket, you get in)
    if not you_have_ticket or party_happening:
        print("You can get in if you have a ticket, or if the party is happening. It is implication.")
    else:
        print("You don't have a ticket, and the party isn't happening. It is not implication.")

# Test with user input
implication()
