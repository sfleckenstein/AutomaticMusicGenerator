from ghmm import *
import numpy as np

def getNoteSeq():
	return [0, 1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':
	# All of the possible observations
	alphabet = IntegerRange(0,7)
	alphaLen = len(alphabet)

	# The transmission matrix
	# Gives the probability of moving from each state to each other state
	transmission = [[0 for col in range(alphaLen)] for row in range(alphaLen)]

	# There is an eqal chance of moving from each state to each other state
	prob = 1.0/(alphaLen**2)
	for p in np.nditer(transmission, op_flags=['readwrite']):
		p[...] = prob

	# The emission matrix
	# Gives the probability of seeing a particular observation given that you
	# are in a certain state. The probabilities are arbitrarily set right now.
	emission = [[0 for col in range(alphaLen)] for row in range(alphaLen)] 
	for i in range(0,alphaLen - 1):
		emission[i][i+1] = 1.0

	# Not entirely sure what purpose this serves yet...
	# GHMM needs it though, so it shall have it's pi
	pi = [1.0/5] * alphaLen

	# Get the useful object
	# We can do all sorts of useful things with this model, liek generate
	# observations, and train it
	model = HMMFromMatrices(alphabet, DiscreteDistribution(alphabet), transmission, emission, pi)

	# Gets some observations from the model
	observations = map(alphabet.external, model.sampleSingle(20))
	print(observations)
