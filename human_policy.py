import numpy as np

class HumanPolicy:
    """
    Class representing a human policy, i.e. a mapping from states to human
    actions.
    """
    def __init__(self, _state_list, _action_list, _lookup_table):
        """
        Initializes an instance of the HumanPolicy class.

        :param state_list: a Python list containing all possile states. We
            denote by s_i the state at index i of this list.
        :param action_list: a Numpy array containing all possible actions and
            where each row corresponds to an action. We denote by a_j the
            action at index j of this list.
        :param lookup_table: a (|S|, |A^H|) Numpy array where each row
            corresponds to a probability (i.e. each entry is non-negative and
            each row sums to one). Entry (i,j) in this array denotes
            P(a^H_j | s_i).
        """
        self._state_list = _state_list
        self._action_list = _action_list
        if ValidLookupException("").isValid(_lookup_table):
            self._lookup_table = _lookup_table
        else:
            raise ValidLookupException("Not a Valid Lookup Table")

    def getAction(state):
        """
        Returns an action given the human's current state.

        :param state: the current state.
        """
        state_index = self._state_list.index(state)
        action_index = np.random.choice(_action_list.shape[0], size=1,
            p=self._lookup_table[state_index,:])
        return action_list[action_index,:]

class ValidLookupException(Exception):
    """
    Exception that is raised if the lookup table is not well-defined.
    """
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)

    def isValid(self, lookup_table):
        """
        Returns true if the provided lookup_table is well-defined i.e. if every
        entry is non-negative and every row sums to 1

        :param lookup_table:
        """
        nonnegative = lookup_table >= 0
        if not np.all(nonnegative):
            return False
        sum_of_rows = np.sum(lookup_table, axis=1)
        if not np.all(np.isclose(sum_of_rows, np.ones(len(sum_of_rows)))):
            return False
        return True
