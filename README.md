# NFA for C-Style Comments

**Renier Apal**  
**3 BSCS-A**  
**CS 13a — Automata Theory and Formal Language**

A C++ implementation of a nondeterministic finite automaton (NFA) that recognizes strings representing a C-style comment.

The alphabet is `{a, *, /}`, where `a` represents some character that is not `*` or `/`.

The machine is divided into three parts connected by ε-transitions:

1. Opening delimiter `/*`
2. Comment body
3. Closing delimiter `*/`

Because an NFA can have multiple possible transitions for the same input, the machine can keep multiple possible computation paths at the same time.

---

## NFA Visualization

<img width="677" height="220" alt="Nfapic" src="https://github.com/user-attachments/assets/e08ceb98-c99e-422f-a2a3-6eedfcd41329" />

---
## State
| State | Meaning                                                               |
| ----- | --------------------------------------------------------------------- |
| `q0`  | Start state; nothing has been read                                    |
| `q1`  | `/` has been read; expecting `*`                                      |
| `q2`  | `/*` has been read; currently inside the comment                      |
| `q3`  | `*` has just been read; may be the beginning of the closing delimiter |
| `q4`  | `*/` has been read; accepting state                                   |
---
## Formula Definition
N = (Q, Σ, δ, q₀, F)

Q  = {q0, q1, q2, q3, q4}

Σ  = {a, *, /}

q₀ = q0

F  = {q4}

δ : Q × Σ → P(Q)

Where:

Q is the set of states.
Σ is the input alphabet.
δ is the transition function.
q0 is the initial state.
F is the set of accepting states.
P(Q) is the power set of Q.
---
## Transition Table
| **δ**  | **a**  | *****      | **/**  |
| ------ | ------ | ---------- | ------ |
| → `q0` | `∅`    | `∅`        | `{q1}` |
| `q1`   | `∅`    | `{q2}`     | `∅`    |
| `q2`   | `{q2}` | `{q2, q3}` | `{q2}` |
| `q3`   | `{q2}` | `{q3}`     | `{q4}` |
| * `q4` | `∅`    | `∅`        | `∅`    |

→ marks the start state.

* marks the accepting state.

The braces indicate that the transition function returns a set of possible states.

---
## Where the Nondeterminism Is

The nondeterminism occurs at state q2 when the input symbol is *.

q2 --*--> q2

q2 --*--> q3

When the NFA reads * inside the comment, it has two possible choices.

## First possibility

q2 --*--> q2

The * is treated as part of the comment body.

## Second possibility

q2 --*--> q3

The NFA assumes that the * might be the beginning of the closing delimiter */.

The NFA keeps both possible paths.

If the next character is /, the path through q3 reaches the accepting state:

q3 --/--> q4

Therefore, the string is accepted.
---
## Acceptance

A string is accepted if, after reading the entire input, at least one possible NFA path reaches q4.

For example:

/*a*/

The NFA follows:

q0 --/--> q1
q1 --*--> q2
q2 --a--> q2
q2 --*--> q3
q3 --/--> q4

Since the input finishes at q4, the string is:

ACCEPTED

On the other hand:

/**

ends at q3.

There is no / after the *, so the NFA cannot reach q4.

Therefore:

REJECTED
---
## NFA Simulation

The C++ program simulates the NFA by maintaining a set of currently active states.

For every input character:

The program checks all current states.
It finds every possible transition for the input character.
It stores all possible next states.
The process continues until the entire input is read.
The program checks whether q4 is in the final set of states.

The basic idea is:

for (State state : currentStates)
{
    // Find all possible next states
}

currentStates = nextStates;

If there are no possible states remaining, the input is rejected.
--- 
## C++ Implementation

The program is written in C++ and uses the Standard Template Library.

Main libraries:

#include <iostream>
#include <set>
#include <string>

The states are represented using an enumeration:

enum State
{
    Q0,
    Q1,
    Q2,
    Q3,
    Q4
};

The complete program is available in:

Nfa_CStylecomment.cpp
---
## Compile

Using g++:

## Windows

g++ -Wall -Wextra -std=c++17 Nfa_CStylecomment.cpp -o nfa

## Linux / macOS

g++ -Wall -Wextra -std=c++17 Nfa_CStylecomment.cpp -o nfa

## Run

## Windows

.\nfa.exe

## Linux / macOS

./nfa

---
## Sample Runs

Example 1 — Accepted

Input: /* */

Result: ACCEPTED

Example 2 — Accepted

Input: /* a */

Result: ACCEPTED

Example 3 — Accepted

Input: /* aaa*aaa */

Result: ACCEPTED

Example 4 — Rejected

Input: /**

Result: REJECTED

Example 5 — Rejected

Input: aaa/**/aa

Result: REJECTED

--- 
## Test Case

| Input         | Expected Result |
| ------------- | --------------- |
| `/**/`        | ACCEPTED        |
| `/*a*/`       | ACCEPTED        |
| `/***/`       | ACCEPTED        |
| `/*aaa*aaa*/` | ACCEPTED        |
| `/*a/a*/`     | ACCEPTED        |
| `/**`         | REJECTED        |
| `/**a`        | REJECTED        |
| `aaa/**/aa`   | REJECTED        |
| `//aaaa`      | REJECTED        |
| `**`          | REJECTED        |

---
## HandWritten Solution
<img width="2326" height="3018" alt="09230343-6fad-4ba7-aa4b-38c5899c9838" src="https://github.com/user-attachments/assets/ac98c90c-709d-419b-92cd-2a1b78379327" />


---
