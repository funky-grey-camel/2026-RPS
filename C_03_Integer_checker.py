def int_check(question, exit_code=None):
    """checks for an integer more than 0 (allows <enter>)"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode / exit code
        if response == exit_code:
            return exit_code

        try:
            # tries to make the response into an integer
            response = int(response)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:

                return response

        except ValueError:
            # if the response is not an integer, displays an error
            print(error)

# Main Routine

mode = "regular"

rounds_wanted = int_check("how many rounds? <enter for infinite>: ", "")

if rounds_wanted == "":
    # change mode to infinite if user press <enter>
    mode = "infinite"

    # set rounds_wanted to a number for comparison later.
    rounds_wanted = 5
