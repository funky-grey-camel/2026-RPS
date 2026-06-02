# check that users have entered a valid
# option based on list
def string_checker(user_response, valid_ans):
    while True:
        for item in valid_ans:

            # check if user response is a word in the list
            if user_response.lower() == item:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response.lower() == item[0]:
                print("we have a single letter")
                return item

        return "invalid"


# automated testing is blow in the form (test_case, expected_value)
to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("N", "no"),
    ("YES","yes"),
    ("MAYBE", "invalid"),

]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, ["yes", "no"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
