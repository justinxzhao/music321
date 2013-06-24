import pickle
from ChordGraph import *
from ChordVertex import *
from ChordLink import *

pkl_file = open('data/data.pkl', 'rb')

chordGraph = pickle.load(pkl_file)
for c in chordGraph.chordSet.values():
	print "The chord: " + c.chordStr
	c.printLinks()
	print ""