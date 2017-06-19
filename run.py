import numpy as np

from game import *
from human import *
from robot import *

class Run:
    """
    Class that runs the game.
    """
    def __init__(self, _num_objects, _human_prod_cap, _robot_prod_cap,
        _delta, _human_policies, _max_T, _gamma):
        """
        Initializes an instance of the Run class.

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
        self._num_objects = _num_objects
        self._human_prod_cap = _human_prod_cap
        self._robot_prod_cap = _robot_prod_cap
        self._delta = _delta
        self._human_policies = _human_policies # TODO: Alternatively, look at constructing the set of policies inside the Run class
        self._max_T = _max_T
        self._gamma = _gamma

    def chooseTheta(self):
        """
        Chooses a value of \theta (the human's reward parameter) randomly. Each
        object is randomly assigned a value from 1-10; this value is then
        normalized to form well-defined probabilities.

        Returns the chosen \theta.
        """
        theta = np.random.randint(10, size = self._num_objects) + 1
        return values/sum(values)

    def run(self):
        """
        Runs the game for self._max_T time steps by initializing instances of
        the game, human player and robot player.

        Returns the total reward accumulated by the robot.
        """
        theta = self.chooseTheta()
        policy = _human_policies[np.random.randint(len(_human_policies))] # TODO: Construct human_policy class

        env = Game(theta, _num_objects, _human_prod_cap,
            _robot_prod_cap, _delta)
        human = Human(theta, _num_objects, _human_prod_cap, policy)
        robot = Robot(_num_objects, _robot_prod_cap)

        for t in range(_max_T):
            if t % 2 == 0:
                human_action = human.pickAction()
                robot_action = robot.nullAction()
            else:
                human_action = human.nullAction()
                robot_action = robot.pickAction()
            reward = env.respond(human_action, robot_action)
            robot.getObservation(human_action)
        return env.totalReward()
