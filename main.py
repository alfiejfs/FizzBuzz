def part_one():
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    """

    # Write it nicely - this way is easily extendable with hardcoded simple rules as opposed to the above
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output += i

        print(output)


"""
This includes extension tasks.

LIMITATION: Custom words must be 4 characters.
SOLUTION: Use regex instead of assuming words are 4 characters. Just feels slightly unnecessary 

Noticed ambiguities:

It is not explicitly stated to include the old FizzBuzz rules, just implied through the cases and phrase "new rules". 
Definitely implied and intended, but not explicitly stated.

For the case of multiple of 7, does not say what to do if the number is a multiple of 11, 13 or 17, only when it is 3, 
5 or 7

The number multiple of 11 statement says "Do not print anything else in these cases", and then the multiple of 13 
statement says that it should also apply to those with bong in it.
"""
def part_two():
    standard_rules = {
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

        response = input("Add a custom four letter word. Enter a multiple (cannot be 3, 5, 7, 11, 13 or 17). "
                         "Type q to run the count: ")
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

        if number in standard_rules or number == 11 or number == 13 or number == 17:
            print("That number has already been assigned.")
            continue

        word = ""
        while len(word) != 4:
            word = input("Enter a four letter word to match to multiples of " + str(number) + ": ")
        word = word[0].upper() + word[1:] # Keep the formatting
        standard_rules[number] = word
        print("Assigned " + word + " to " + str(number))

    for i in range(1, upper_bound + 1):
        output = ""
        if i % 11 == 0:
            output = "Bong"

        if output != "Bong":
            for key, value in standard_rules.items():
                if i % key == 0:
                    output += value

        # Handle the Fezz after standard rules
        if i % 13 == 0:
            # Use a step of 4, as all strings are 4 characters
            for c in range(0, len(output), 4):
                if output[c] == "B":
                    output = output[:c] + "Fezz" + output[c:]

        # Reverse here using string manipulation. Not the technical fastest solution in terms of execution time
        # but the best looking statement as opposed to over arching if statements with repeating code.

        if i % 17 == 0:
            # Could use regex to split by characters, but all strings are 4 letters, so for this we can use that.
            new_output = ""
            for i in range(len(output), 0, -4):
                new_output += output[i-4:i]

            output = new_output

        # For cases where no rules apply:
        if output == "":
            output = i

        print(output)

part_two()