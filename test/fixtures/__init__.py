from Models import Automaton


def get_main_sigma_dict():
    return {
        'q0': {'0': ['q0'], '1': ['q0', 'q1']},
        'q1': {'0': ['q2'], '1': ['q2']},
        'q2': {'0': ['q1'], '1': ['q1']}
    }

def get_main_sigma_with_epsilon_dict():
    return {
        'q0': {'0': ['q0'], '1': ['q0', 'q1'], 'epsilon': ['q1']},
        'q1': {'0': ['q2'], '1': ['q2'], 'epsilon': ['q2']},
        'q2': {'0': ['q1'], '1': ['q1'], 'epsilon': ['q1']}
    }


def ger_main_automoton(sigma: dict = None):
    if not sigma:
        sigma = get_main_sigma_dict()
    return Automaton(
        states = ['q0', 'q1', 'q2'],
        alphabet = ['0', '1'],
        sigma = sigma,
        initial = 'q0',
        final = ['q2'],
        actual= ['q0']
    )


def get_main_automoton_with_epsilon_transition(sigma: dict = None):
    if not sigma:
        sigma = get_main_sigma_with_epsilon_dict()
    return Automaton(
        states = ['q0', 'q1', 'q2'],
        alphabet = ['0', '1'],
        sigma = sigma,
        initial = 'q0',
        final = ['q2'],
        actual= ['q0']
    )