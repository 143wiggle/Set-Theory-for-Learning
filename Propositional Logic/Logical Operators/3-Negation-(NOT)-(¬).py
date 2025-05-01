def negation():
    # Prompting if the light is on
    light_on = input("Is the light on? (yes/no): ").strip().lower() == 'yes'
    
    # Negating the light's state
    if not light_on:
        print("The light is off. Negation turns it on! It is negation.")
    else:
        print("The light is on. Negation turns it off! It is negation.")

# Test with user input
negation()
