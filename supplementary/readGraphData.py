import pickle
from ChordGraph import *
from ChordVertex import *
from ChordLink import *
from music21 import *
from random import randint

# Open the analysis file
pkl_file = open('data/bachChoraleData.pkl', 'rb')
chordGraph = pickle.load(pkl_file)
#for c in chordGraph.chordSet.values():
#	print "The chord: " + c.chordStr
#	c.printLinks()
#	print ""

# Initialization
musicStream = stream.Stream()

# Enter a starting chord
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

# play the final result
#musicStream.show('midi')
musicStream.show()

# IDEAS
# average number of times before it returns to i
# chord that stems the most possibilities
# chord that stems the least possibilities
# chord that has the highest chance of being chosen
# chord that has the least chance of being chosen
# graph algorithms (minimum spanning tree, dijktras etc)
# use chords to generate harmony/melody