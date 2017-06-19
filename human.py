import numpy as np

class Human:

	'''
	The Human class defines the human player in the CIRL game. It specifies the entire action set of the human based on the input hyperparameters.
	'''

	def __init__(self, _theta, _num_objects, _human_prod_cap, _policy):
		'''
        Initializes an instance of the Human class.
        
        :param _theta: the reward parameter from the CIRL game.
        :param _num_objects: the number of different objects in the instance of
            the game.
        :param _human_prod_cap: the number of items a human player can make
            at every turn
		:param _policy: the policy that the human will follow during this game
        '''

		self._theta = _theta
		self._num_objects = _num_objects
		self._human_prod_cap = _human_prod_cap
		self._policy = _policy
		self.action_list = self.create_action_list()

	def create_action_list(self):
		'''
		This method creates the entire set of possible human actions, based on input hyperparameters.

		We use the compositions method. As an example, if we have 5 objects, but only want to select a total of 3, then we want to return compositions(3, 5), so n = 3 and k = 5. So, we want compositions(_human_prod_cap, _num_objects)

		This method returns a Python list of numpy arrays, where each numpy array corresponds to a single action.
		'''
		action_list_old = list(compositions(_human_prod_cap, _num_objects))
		action_list_numpy = []

		for list_old in action_list_old:
			list_numpy = np.array(list_old)
			action_list_numpy.append(list_numpy)

		return action_list_numpy

		


	def compositions(n,k):
		'''
		borrowed from http://dandrake.livejournal.com/83095.html

		This method splits the integer n into k different ordered sets, such that the sum of the elements in the set is n.

		This method returns a generator object. Converting it to a list returns a list of lists, where each internal list is a single action (one action corresponds to a composition).

		For example: list(compositions(4,2)) returns [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]].
		'''
		if n < 0 or k < 0:
			return
		elif k == 0:
			if n == 0:
				yield []
			return
		elif k == 1:
			yield [n]
			return
		else:
			for i in range(0, n + 1):
				for comp in compositions(n - i, k - 1):
					yield [i] + comp

