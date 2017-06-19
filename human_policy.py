import numpy as np

class HumanPolicy:
    """
    Class representing a convex set of human policies; a human policy is a
    mapping from values of theta to human actions. (In general, it is a mapping
    from states to actions.)

    For any policy in the set, the probability of picking action i given some
    \theta falls in some interval (a_i, b_i) \subseteq [0,1].
    """
    # QUESTION: How should we deal with continuous theta spaces?
    # QUESTION: Use IRL to find \theta?
    # QUESTION: Does the state affect the human policy?
