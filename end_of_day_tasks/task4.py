# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE

while user_prompt:
    age = input("What is your age? ")

    if age.isdigit() and int(age) < 117:
        print(f"Your age is {age}")
        user_prompt = False
    else:
        print("There is a problem with your input")
