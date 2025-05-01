def xor():
    # Prompting both friends
    you_have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower() == 'yes'
    friend_have_ticket = input("Does your friend have a ticket? (yes/no): ").strip().lower() == 'yes'
    
    # Checking XOR (Exactly one must have a ticket)
    if you_have_ticket != friend_have_ticket:  # Exactly one must be True
        print("Only one of you has a ticket! It is XOR!")
    else:
        print("Either both have tickets or neither has a ticket. It is not XOR.")

# Test with user input
xor()
