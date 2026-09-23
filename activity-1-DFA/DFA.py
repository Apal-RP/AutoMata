
# Alphabet: {0, 1}

states = {"A", "B", "C", "D", "E", "F"}

alphabet = {"0", "1"}

start_state = "A"

accept_states = {"E"}


# DFA transition table
transitions = {
    "A": {
        "0": "B",
        "1": "C"
    },

    "B": {
        "0": "A",
        "1": "D"
    },

    "C": {
        "0": "C",
        "1": "F"
    },

    "D": {
        "0": "C",
        "1": "E"
    },

    "E": {
        "0": "F",
        "1": "F"
    },

    "F": {
        "0": "F",
        "1": "F"
    }
}


def accepts(input_string):

    current_state = start_state

    for symbol in input_string:

        if symbol not in alphabet:
            return False

        current_state = transitions[current_state][symbol]

    return current_state in accept_states


def main():

    print("DFA EXAMPLE")
    print("Alphabet: {0, 1}")

    input_string = input("Enter a string: ")

    if accepts(input_string):
        print("ACCEPTED")
    else:
        print("REJECTED")


if __name__ == "__main__":
    main()