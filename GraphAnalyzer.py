import pickle
from ChordGraph import *
from ChordVertex import *
from ChordLink import *
from music21 import *
from random import randint

class GraphAnalyzer:

	def __init__(self, pickedGraphFile):
		pkl_file = open('data/bachChoraleData.pkl', 'rb')
		self.chordGraph = pickle.load(pkl_file)

	def generateChordProgression(self):

		musicStream = stream.Stream()

		s = raw_input("Enter a starting chord: ")
		startChord = chordGraph.chordSet[s]
		print startChord.chordStr
		musicStream.append(startChord.rnChord)

		# Generate x random chords from starting chord
		currentChord = startChord
		for x in xrange(24):
			#find weight sum of all possibilities
			weightSum = 0
			for cl in currentChord.chordLinks.values():
				weightSum = weightSum + cl.weight

			choice = randint(0, weightSum)

			#find chord corresponding to that random choice
			sum = 0
			for cl in currentChord.chordLinks.values():
				sum = sum + cl.weight
				if sum > choice:
					nextChord = chordGraph.chordSet[cl.destination]
					break

			print nextChord
			musicStream.append(roman.RomanNumeral(nextChord.chordStr))
			currentChord = nextChord
		
		return musicStream

	def printOutgoingChords(self):
		s = raw_input("Enter the chord: ")
		c = chordGraph.chordSet[s]
		c.printLinks()