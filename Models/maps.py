from .Automaton import Automaton


def create_automaton(json_infomate: dict) -> Automaton:
    if not 'states' in json_infomate:
        raise Exception('The states field is required')
    if not 'alphabet' in json_infomate:
        raise Exception('The alphabet field is required')
    if not 'sigma' in json_infomate:
        raise Exception('The sigma field is required')
    if not 'initial' in json_infomate:
        raise Exception('The initial field is required')
    if not 'final' in json_infomate:
        raise Exception('The final field is required')
    states = json_infomate['states']
    alphabet = json_infomate['alphabet']
    sigma = json_infomate['sigma']
    initial = json_infomate['initial']
    final = json_infomate['final']
    actual = [initial]
    return Automaton(states=states, alphabet=alphabet, sigma=sigma, initial=initial, final=final, actual=actual)


def validate_automaton(automaton: Automaton) -> bool:
    if not automaton.exist_status(automaton.initial):
        raise Exception('The initial state is not in the states')
    if not automaton.set_actual_status(automaton.actual):
        raise Exception('The initial state is not in the states')
    for state in automaton.final:
        if not automaton.exist_status(state):
            raise Exception(f'The state {state} is not in the states')
    for state in automaton.states:
        if state not in automaton.sigma:
            raise Exception(f'The state {state} is not in the sigma')
    for state in automaton.sigma:
        if not automaton.exist_status(state):
            raise Exception(f'The state {state} is not in the states')
        letter = automaton.sigma[state]
        for l in letter:
            if not l in automaton.alphabet and l != 'epsilon':
                raise Exception(f'The letter {l} is not in the alphabet')
            for s in letter[l]:
                if not automaton.exist_status(s):
                    raise Exception(f'The state {s} is not in the states')
    return True