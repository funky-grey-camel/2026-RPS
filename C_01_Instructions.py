
# functions go here

def string_checker(question, valid_ans=('yes', 'no')):

    if valid_ans is None:
        valid_ans = ['yes', 'no']
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a word in the list
            if user_response.lower() == item:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response.lower() == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instruction():
    """Displays instructions"""

    print("""
**** RPS Instructions... ****

Choose rock / paper / scissors.

Try to win
    """)


#Main routine

want_instructions = string_checker("Do you want the instructions? ")

print("we done")
