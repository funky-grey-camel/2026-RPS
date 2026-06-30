import random

from Tools.scripts.generate_sre_constants import sre_constants_header


# check that users have entered a valid
# option based on a list

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

# displays instructions
def instructions():
    print("""

*** R/P/S Instructions ***

- Rock beats scissors
- Scissors beats paper
- Paper beats rock

Try to win.

Good luck

    """)


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return "infinite"

        try:
            response = int(response)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response


        except ValueError:
            print(error)

def rps_compare(user , comp):

   # if the user and computer choice is the same, it's a tie
   if user == comp:
       round_result = "tie"

    # there are three ways to win
   elif user == "paper" and comp == "rock":
       round_result = "win"
   elif user == "rock" and comp == "scissors":
       round_result = "win"
   elif user == "scissors" and comp == "paper":
       round_result = "win"

    # if it's not a win / tie, then it's a loss
   else:
       round_result = "lose"

   return round_result

# main routine starts here

# initialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []


print("🪨📃️✂️ Rock / Paper / Scissors game 🪨📃✂️")
print()

# ask user if they want to see the instructions and display
# them is requested
want_instructions = string_checker("do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# ask user for number of rounds / infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> for infinite mode: ")

print("num rounds", num_rounds)

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # round headings
    if mode == "infinite":
        rounds_heading = f"\n❎❎❎ Round {rounds_played + 1} (infinite mode) ❎❎❎"
    else:
        rounds_heading = f"\n💿💿💿 round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # randomly choose from the rps list (excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("computer choice", comp_choice)

    user_choice = string_checker("choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    # adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔 it's a tie! 👔👔"
    elif result == "lose":
        feedback = "😭😭 you lose. 😭😭"
    else:
        feedback = "🏆🏆 you won. 🏆🏆"

    # set up round feedback and output it user.
    # add it to the game history list (include the round number)
    rounds_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"round: {rounds_played +1} - {rounds_feedback}"

    print(rounds_feedback)
    game_history.append(history_item)


    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / statistics area

if rounds_played > 0:
    # calculate statistics
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost


    print()
    # Output game statistics
    print("🧮🧮🧮 game statistics 🧮🧮🧮")
    print(f"🏆 won: {percent_won:.2f} \t "
          f"😭 lost: {percent_lost:.2f} \t "
          f"👔 Tied: {percent_tied:.2f}")

    print()
    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("/Do you want to see your game history? ")
    if see_history == "yes":
         for item in game_history:
             print(item)

    print()
    print("thanks for playing rock paper Scissors")

else:
    print("🐔🐔 looks like  - you chickened out! 🐔🐔")



