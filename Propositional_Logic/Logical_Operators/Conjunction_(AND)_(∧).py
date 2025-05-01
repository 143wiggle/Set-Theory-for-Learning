def conjunction():
    # Prompting both friends
    you_have_ticket = input("Do you have a ticket? (yes/no): ").strip().lower() == 'yes'
    friend_have_ticket = input("Does your friend have a ticket? (yes/no): ").strip().lower() == 'yes'
    
    # Checking the conjunction (both must have tickets)
    if you_have_ticket and friend_have_ticket:
        print("Both of you have tickets! It is a conjunction!")
    else:
        print("One or both of you don't have tickets. It is not a conjunction.")

# Test with user input
conjunction()
