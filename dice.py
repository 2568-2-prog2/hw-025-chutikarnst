import random

class BiasedDice:
    def __init__(self, prob):
        if len(prob) != 6:
            raise Exception("Not the right number of face for probability")
        elif not 0.99 < sum(prob) < 1.01:
            raise Exception("Probability not 100%")
        self.faces = [1,2,3,4,5,6]
        self.prob = prob

    def roll(self, n_roll=1):
        return random.choices(self.faces, weights=self.prob, k=n_roll)