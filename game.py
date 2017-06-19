import numpy as np

class Game:
    """
    The Game class defines the dynamics of the game and contains the specific
    parameters of the game being played.
    """
    def __init__(self, _theta, _num_objects, _human_prod_cap, _robot_prod_cap,
        _delta):
        """
        Initializes an instance of the Game class.

        :param _theta: the reward parameter from the CIRL game.
        :param _num_objects: the number of different objects in the instance of
            the game.
        :param _human_prod_cap: the number of items a human player can make
            at every turn
        :param _robot_prod_cap: the number of items of a single object a robot
            player can make at every turn
        :param _delta: the extra item parameter
        :param _human_policies: the restricted set of human policies that the
            human may choose his policy from
        :param _max_T: the length of the horizon of the game
        :param _gamma: the discount factor
        """
        self.state = np.zeros(_num_objects) # current state
        self.last_human_action = None # last human action taken
        self._theta = _theta
        self._human_prod_cap = _human_prod_cap
        self._robot_prod_cap = _robot_prod_cap
        self._delta = _delta

    def respond(self, human_action, robot_action):
        """
        Updates the game's state.
        Sets the last human action to be human_action.

        Returns the reward for the human taking human_action and the robot
        taking robot_action.

        :param human_action:
        :param robot_action:
        """
        self.state += (human_action + robot_action)
        self.last_human_action = human_action
        return (human_action + robot_action).dot(self._theta)

    def totalReward(self):
        """
        Returns the total reward accumulated in the game.
        """
        return self.state.dot(self._theta)
