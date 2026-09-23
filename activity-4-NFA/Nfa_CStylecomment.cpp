#include <iostream>
#include <set>
#include <string>

using namespace std;

enum State {
    Q0,
    Q1,
    Q2,
    Q3,
    Q4
};

// Returns the possible next states
set<State> moveNFA(set<State> states, char input)
{
    set<State> nextStates;

    for (State state : states)
    {
        switch (state)
        {
            case Q0:
                if (input == '/')
                    nextStates.insert(Q1);
                break;

            case Q1:
                if (input == '*')
                    nextStates.insert(Q2);
                break;

            case Q2:
                if (input == 'a' || input == '/')
                {
                    nextStates.insert(Q2);
                }

                if (input == '*')
                {
                    // NFA has two possible choices
                    nextStates.insert(Q2);
                    nextStates.insert(Q3);
                }
                break;

            case Q3:
                if (input == 'a')
                {
                    nextStates.insert(Q2);
                }

                if (input == '*')
                {
                    nextStates.insert(Q3);
                }

                if (input == '/')
                {
                    // Continue inside the comment
                    nextStates.insert(Q2);

                    // Or accept the comment
                    nextStates.insert(Q4);
                }
                break;

            case Q4:
                // No transitions from accepting state
                break;
        }
    }

    return nextStates;
}


bool isAccepted(string input)
{
    // Start at q0
    set<State> currentStates;
    currentStates.insert(Q0);

    for (char c : input)
    {
        // Check alphabet
        if (c != 'a' && c != '*' && c != '/')
        {
            return false;
        }

        // Find all possible next states
        currentStates = moveNFA(currentStates, c);

        // No possible path remains
        if (currentStates.empty())
        {
            return false;
        }
    }

    // Accept if q4 is one of the possible states
    return currentStates.count(Q4) > 0;
}


int main()
{
    string input;

    cout << "NFA FOR C-STYLE COMMENTS" << endl;
    cout << "Alphabet: {a, *, /}" << endl;
    cout << endl;

    cout << "Enter a string: ";
    cin >> input;

    if (isAccepted(input))
    {
        cout << "Result: ACCEPTED" << endl;
    }
    else
    {
        cout << "Result: REJECTED" << endl;
    }

    return 0;
}