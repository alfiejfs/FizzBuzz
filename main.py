"""
This includes extension tasks. 

Noticed ambiguities:

It is not explicitly stated to include the old FizzBuzz rules, just implied through the cases and phrase "new rules". 
Definitely implied and intended, but not explicitly stated.

For the case of multiple of 7, does not say what to do if the number is a multiple of 11, 13 or 17, only when it is 3, 
5 or 7

The number multiple of 11 statement says "Do not print anything else in these cases", and then the multiple of 13 
statement says that it should also apply to those with bong in it.
"""
def start_fizz_buzz():
    rules = {
        3: "Fizz",
        5: "Buzz",
        7: "Bang"
    }

    upper_bound = None
    while upper_bound is None:
        try:
            upper_bound = int(input("Enter an upper limit to count to: "))
            if upper_bound <= 0:
                upper_bound = None
                raise ValueError # Not necessary to raise an exception, just makes code shorter here
        except ValueError:
            print("Please enter a positive integer (whole number >= 0)")

    while True:
        response = input("To add a custom rule, enter a number. Type q to run FizzBuzz: ")

        if response == "q":
            break

        try:
            number = int(response)
            if number <= 0:
                # Same as before, just neater written code. Not an exceptional case, so not exception worthy, but
                # it is nicer to look at
                raise ValueError
        except ValueError:
            print("Please enter a positive integer (whole number >= 0)")
            continue

        if number in rules or number == 11 or number == 13 or number == 17:
            print("That number has already been assigned.")
            continue

        word = input("Enter a word: ")
        word = word[0].upper() + word[1:].lower() # Keep the formatting with upper then lower
        rules[number] = word
        print("Assigned " + word + " to " + str(number))

    handle_fizz_buzz(upper_bound, rules)


def handle_fizz_buzz(upper_bound, rules):
    for i in range(1, upper_bound + 1):
        output = []
        if i % 11 == 0:
            output.append("Bong")
        else:
            for key, value in rules.items():
                if i % key == 0:
                    output.append(value)

        # Handle the Fezz after standard rules
        if i % 13 == 0:
            # Use a step of 4, as all strings are 4 characters
            # Quicker than using find() as we don't need to check every character!

            b_index = -1
            for j in range(len(output)):
                if output[j].startswith("B"):
                    b_index = j
                    break
                    
            if b_index == -1:
                output.append("Fezz")
            else:
                output.insert(b_index, "Fezz")

        # Reverse here using string manipulation. Not the technical fastest solution in terms of execution time
        # but the best looking statement as opposed to over arching if statements with repeating code.

        if i % 17 == 0:
            output.reverse()

        # For cases where no rules apply:
        if not output: # Empty list is not truthy
            print(i)
        else:
            print("".join(output))


start_fizz_buzz()
