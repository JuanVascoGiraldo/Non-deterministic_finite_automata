# Introduction

Welcome to our Python program for creating and manipulating Non-Deterministic Finite Automata (NFA). This program is designed to allow users to define and work with non-deterministic finite automata in a simple and efficient manner.

Non-deterministic Finite Automata are a fundamental tool in computer theory and computational linguistics, used to model and analyze computational systems and formal languages. Our program provides an intuitive interface for defining states, alphabets, transition functions, and final states of an automaton, as well as for executing input strings and verifying acceptance.

With this program, users can create, visualize, and manipulate non-deterministic finite automata easily and quickly, enabling them to explore and understand fundamental concepts in computer theory and automation.


# Key Features:
## Creation and Manipulation of NFAs:
Easily create and manipulate Non-Deterministic Finite Automata using the intuitive interface provided by the program. Define states, alphabets, transition functions, and final states to construct custom NFAs tailored to your specific requirements.

## Validation of NFAs:
Ensure the correctness of NFAs by validating them against predefined criteria. The program offers validation functions to check the structural integrity and coherence of NFAs, helping users identify and rectify any inconsistencies or errors in their automata designs.

## Input String Acceptance Verification:
Verify whether a given input string is accepted by a specified NFA. Simply input the string and let the program execute it against the NFA, providing immediate feedback on whether the string is accepted or rejected by the automaton.

## Computation of Epsilon Closure Union:
Compute the union of epsilon closures for states within an NFA. This feature allows users to analyze the epsilon transitions within their automata, facilitating a deeper understanding of the computational behavior and structure of the NFA.

# Create Automate
To create the automata, a json file called automata.json will be used where the tuple of the automaton with which you are going to work will be entered.

``` json
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["0", "1"],
    "sigma": {
        "q0": {"0": ["q0"], "1": ["q0", "q1"]},
        "q1": {"0": ["q2"], "1": ["q2"]},
        "q2": {"0": ["q1"], "1": ["q1"]}
    },
    "initial": "q0",
    "final": ["q2"]
}
```
example with epsilon transaction
``` json
{
    "states": ["q0", "q1", "q2"],
    "alphabet": ["0", "1"],
    "sigma": {
        "q0": {"0": ["q0"], "1": ["q0", "q1"], "epsilon": ["q1"]},
        "q1": {"0": ["q2"], "1": ["q2"]},
        "q2": {"0": ["q1"], "1": ["q1"]}
    },
    "initial": "q0",
    "final": ["q2"]
}
```

example with epsilon transaction
``` json
{
    "states": ["q0", "q1", "q2", "q3", "q4"],
    "alphabet": ["a", "b"],
    "sigma": {
        "q0": {"a": ["q3"], "b": [], "epsilon": ["q1"]},
        "q1": {"a": [], "b": [], "epsilon": ["q2"]},
        "q2": {"a": [], "b": []},
        "q3": {"a": [], "b": ["q4"]},
        "q4": {"a": [], "b": ["q0"], "epsilon": ["q1"]}
    },
    "initial": "q0",
    "final": ["q0", "q2"]
}
```

This JSON file represents a non-deterministic finite automaton (NFA).
It defines the states, alphabet, transition function, initial state, final states, and current state of the NFA.

## states 
An array of strings representing the states of the NFA.
## alphabet
An array of strings representing the alphabet symbols of the NFA.
## sigma  
An object representing the transition function of the NFA.
    -The keys are the states, and the values are objects representing the transitions for each symbol in the alphabet.
    -Each transition object has keys as alphabet symbols and values as an array of destination states.
## initial 
A string representing the initial state of the NFA.
## final 
An array of strings representing the final states of the NFA.

# Run Locally

Clone the project

```bash
  git clone ${project_link}
```

Go to the project directory

```bash
  cd ${project_name}
```

Create a virutal environment 

```bash
  python -m venv venv
```

Activate the virutalenv

```bash
  . ./venv/bin/activate
```


Install dependencies

```bash
  python -m pip install -r requirements.txt
```

Start the program

```bash
  python main.py
```

Test

```bash
  pytest
```
