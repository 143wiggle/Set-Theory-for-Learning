def bi_conditional():
    # Prompting both friends
    you_have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower() == 'yes'
    friend_have_ticket = input("Does your friend have a ticket? (yes/no): ").strip().lower() == 'yes'
    
    # Checking the bi-conditional (both must have tickets, or neither must have tickets)
    if you_have_ticket == friend_have_ticket:
        print("You both have tickets, or neither of you does. It is a bi-conditional!")
    else:
        print("One of you has a ticket and the other doesn't. It is not a bi-conditional.")

# Test with user input
bi_conditional()
