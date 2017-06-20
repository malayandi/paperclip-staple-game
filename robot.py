import numpy as np
import itertools

class Robot:

	def __init__(self, _num_objects, _robot_prod_cap, _delta):
		"""
        Initializes an instance of the Robot class.
        
        :param _num_objects: the number of different objects in the instance of
            the game.
        :param _robot_prod_cap: the number of items a robot player can make
            at every turn, if he makes 1 of each type of item.
		:param _delta: the factor which adjusts the total number of items
			created, based on the number of different types of items made.
		"""

		self._num_objects = _num_objects
		self._robot_prod_cap = _robot_prod_cap
		self._delta = _delta
		self.action_list = self.create_action_list()

	def create_action_list(self, _num_objects, _robot_prod_cap, _delta):
		"""
		This method creates the entire set of possible human actions, based on
		input hyperparameters.

		We use the compositions method. As an example, if we have 5 objects, but
		only want to select a total of 3, then we want to return
		compositions(3, 5), so n = 3 and k = 5. Note, however, that we want a
		different number of items to be made for different values of num_types.
		So, we iterate over the different types of 
		So, we want compositions(_robot_prod_cap, _num_objects).

		This method returns a 2D Numpy array, where each row corresponds to a
		single action.
		"""
		action_list = [] #create list of actions

		for num_types in range(1, n + 1): #consider all possible numbers of selection
			num_select = _robot_prod_cap + (num_types - 1)*(_delta)/(num_types) #use our formula to determine the number of elements created of each type
			index_tuples_list = list(itertools.combinations(range(0, _num_objects), num_types)) #create list of tuples of indices to be selected
			for index_tuple in index_tuples_list: #consider each tuple of indices to be changed
				new_array = np.zeros(_num_objects)
				for index in index_tuple: #consider each index in the tuple
					new_array[index] = num_select #change the array's value at the index
				action_list.append(new_array) #add the array to the action list

		return np.array(action_list) #convert Python list to NP array


	def nullAction(self):
		"""
		Returns the null action (i.e. the action of picking no items).
		"""
		return np.zeros(self._num_objects)