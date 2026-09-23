# DFA Minimization Example 1
# Based on the DFA example from class

states = {"A", "B", "C", "D", "E", "F"}

alphabet = {"0", "1"}

start_state = "A"

accept_states = {"E"}

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


def minimize_dfa():

    # Initial partition
    partitions = [
        set(accept_states),
        states - accept_states
    ]

    partitions = [group for group in partitions if group]

    print("INITIAL PARTITION")
    print(partitions)

    while True:

        state_group = {}

        for index, group in enumerate(partitions):

            for state in group:
                state_group[state] = index

        new_partitions = []

        for group in partitions:

            groups = {}

            for state in group:

                signature = tuple(
                    state_group[transitions[state][symbol]]
                    for symbol in sorted(alphabet)
                )

                if signature not in groups:
                    groups[signature] = set()

                groups[signature].add(state)

            new_partitions.extend(groups.values())

        if len(new_partitions) == len(partitions):
            break

        partitions = new_partitions

        print("NEXT PARTITION")
        print(partitions)

    return partitions


def print_minimized_dfa(partitions):

    print("\nMINIMIZED DFA")
    print("=============")

    state_group = {}

    for index, group in enumerate(partitions):

        name = "{" + ",".join(sorted(group)) + "}"

        for state in group:
            state_group[state] = name

    for group in partitions:

        representative = sorted(group)[0]

        group_name = state_group[representative]

        zero_destination = state_group[
            transitions[representative]["0"]
        ]

        one_destination = state_group[
            transitions[representative]["1"]
        ]

        print(
            f"{group_name}: "
            f"0 -> {zero_destination}, "
            f"1 -> {one_destination}"
        )


def main():

    partitions = minimize_dfa()

    print_minimized_dfa(partitions)


if __name__ == "__main__":
    main()