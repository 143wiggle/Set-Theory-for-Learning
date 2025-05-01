def disjunction():
    # Prompting both friends
    you_have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower() == 'yes'
    friend_have_ticket = input("Does your friend have a ticket? (yes/no): ").strip().lower() == 'yes'
    
    # Checking the disjunction (at least one must have a ticket)
    if you_have_ticket or friend_have_ticket:
        print("At least one of you has a ticket! It is a disjunction!")
    else:
        print("Neither of you has a ticket. It is not a disjunction.")

# Test with user input
disjunction()
