from Models import Automaton, create_automaton, validate_automaton
import json

def ask_for_state(automaton: Automaton):
    print("select the state for which you want to know the epsilon lock")
    for state in automaton.states:
        print(f'-{state}')
    state = input()
    if not automaton.exist_status(state):
        print('The state is not in the states')
    else:
        print(automaton.get_epsilon_lock(state))


def ask_for_string(automaton: Automaton):
    print("select the string you want to validate")
    string = input()
    automaton.set_actual_status([automaton.initial])
    for letter in string:
        if not automaton.change_state(letter):
            print('The string is not accepted by the automaton')
            return
    if automaton.is_final():
        print('The string is accepted by the automaton')
    else:
        print('The string is not accepted by the automaton')

def union_epsilon_ock(automaton: Automaton):
    states = []
    seguir = True
    while seguir:
        print("select the state for which you want to know the epsilon lock")
        for state in automaton.states:
            print(f'-{state}')
        state = input()
        if not automaton.exist_status(state):
            print('The state is not in the states')
        else:
            states.append(automaton.get_epsilon_lock(state))
        print("Do you want to continue? [y/n]")
        seguir = input() == 'y'
    set(states)
    print("This is the union of the epsilon locks")
    print(states)


if __name__ == "__main__":
    with open('automate.json', 'r') as archivo:
        datos = json.load(archivo)
    print(datos)
    automaton = create_automaton(datos)
    validate_automaton(automaton)
    continue_program = True
    while continue_program:
        print("select the option you want to perform")
        print("1. get epsilon lock")
        print("2. know if a string is accepted by the automat")
        print("3. union of epsilon locks")
        print("4. exit")
        option = input()
        if option == '1':
            ask_for_state(automaton)
        elif option == '2':
            ask_for_string(automaton)
        elif option == '3':
            union_epsilon_ock(automaton)
        else:
            continue_program = False