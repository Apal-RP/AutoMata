# Activity 1 — DFA Example

**Renier Apal**  
**3 BSCS-A**  
**CS 13a — Automata Theory and Formal Language**

## Problem

Implement the DFA example discussed in class using Python.

The DFA uses the alphabet `{0, 1}` and contains six states.

## States

```text
Q = {A, B, C, D, E, F}


**Transition Table**

| State | 0 | 1 |
| ----- | - | - |
| → A   | B | C |
| B     | A | D |
| * C   | C | F |
| * D   | E | F |
| * E   | E | F |
| F     | F | F |
