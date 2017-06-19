import numpy as np

class Human:
	"""
	The Human class defines the human player in the CIRL game. It specifies the
	entire action set of the human based on the input hyperparameters.
	"""
	def __init__(self, _theta, _num_objects, _human_prod_cap, _policy):
		"""
        Initializes an instance of the Human class.
        
        :param _theta: the reward parameter from the CIRL game.
        :param _num_objects: the number of different objects in the instance of
            the game.
        :param _human_prod_cap: the number of items a human player can make
            at every turn
		:param _policy: the policy that the human will follow during this game
        """

		self._theta = _theta
		self._num_objects = _num_objects
		self._human_prod_cap = _human_prod_cap
		self._policy = _policy
		self.action_list = self.create_action_list()

	def create_action_list(self):
		"""
		This method creates the entire set of possible human actions, based on
		input hyperparameters.

		We use the compositions method. As an example, if we have 5 objects, but
		only want to select a total of 3, then we want to return
		compositions(3, 5), so n = 3 and k = 5. So, we want
		compositions(_human_prod_cap, _num_objects).

		This method returns a 2D Numpy array, where each row corresponds to a
		single action.
		"""
		actions = list(self.compositions(self._human_prod_cap,
			self._num_objects))
		return np.array(actions)

	def compositions(self, n, k):
		"""
		borrowed from http://dandrake.livejournal.com/83095.html

		This method splits the integer n into ordered sets of size k, such
		that the sum of the elements in the set is n.

		This method returns a generator object. Converting it to a list returns
		a list of lists, where each internal list is a single action (one action
		corresponds to a composition).

		For example: list(compositions(4,2)) returns [[0, 4], [1, 3], [2, 2],
		[3, 1], [4, 0]].

		:param n: the number which each set must sum to (i.e. _human_prod_cap)
		:param k: the number of elements in each set (i.e. _num_objects)
		"""
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
				for comp in self.compositions(n - i, k - 1):
					yield [i] + comp

	def pickAction(self, state):
		# QUESTION: Is the state necessary here?
		"""
		Returns an action, as prescribed by the policy, for the state and
		internal \theta value.

		:param state: current world state
		"""
		return self._policy.getAction(state, self._theta) # TODO: Make the policy class

	def nullAction(self):
		"""
		Returns the null action (i.e. the action of picking no items).
		"""
		return np.zeros(self._num_objects)
