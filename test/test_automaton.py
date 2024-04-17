import unittest
from Models import  validate_automaton
from fixtures import ger_main_automoton, get_main_automoton_with_epsilon_transition

class TestAutomaton(unittest.TestCase):

    def test_automaton_is_not_final(self):
        automaton = ger_main_automoton()
        assert automaton.change_state('0') == True
        assert automaton.change_state('1') == True
        assert automaton.change_state('0') == True
        assert automaton.change_state('1') == True
        assert automaton.change_state('0') == True
        assert automaton.change_state('0') == True
        assert automaton.is_final() == False

    def test_automaton_is_final(self):
        automaton = ger_main_automoton()
        assert automaton.change_state('0') == True
        assert automaton.change_state('1') == True
        assert automaton.change_state('0') == True
        assert automaton.change_state('1') == True
        assert automaton.change_state('0') == True
        assert automaton.change_state('1') == True
        assert automaton.change_state('0') == True
        assert automaton.is_final() == True

    def test_validate_automaton(self):
        automaton = ger_main_automoton()
        self.assertTrue(validate_automaton(automaton))

    def test_is_not_validated_automaton(self):
        automaton = ger_main_automoton()
        automaton.sigma['q0']['2'] = ['q1']
        with self.assertRaises(Exception):
            validate_automaton(automaton)

        automaton = ger_main_automoton()
        automaton.sigma.pop('q0')
        with self.assertRaises(Exception):
            validate_automaton(automaton)

        automaton = ger_main_automoton()
        automaton.states.pop(1)
        with self.assertRaises(Exception):
            validate_automaton(automaton)

        automaton = ger_main_automoton()
        automaton.sigma['q0']['1'] = ['q3']
        with self.assertRaises(Exception):
            validate_automaton(automaton)
        
        automaton = ger_main_automoton()
        automaton.sigma['q3'] = {'0': ['q1'], '1': ['q1']}
        with self.assertRaises(Exception):
            validate_automaton(automaton)

    def test_get_epsilon_lock(self):
        automaton = get_main_automoton_with_epsilon_transition()
        assert len(automaton.get_epsilon_lock('q0')) > 1
        assert len(automaton.get_epsilon_lock('q1')) > 1
        assert len(automaton.get_epsilon_lock('q2')) > 1
