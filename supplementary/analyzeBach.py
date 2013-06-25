from music21 import *
from ChordGraph import *
from ChordVertex import *
from ChordLink import *
import pickle
import re
import os

def parseChords(filePath, chordGraph):
	#parsing the file
	sample = converter.parse(filePath)
	sampleChords = sample.chordify()
	sampleKey = sample.analyze('key')

	#flattening and placing them correctly
	for c in sampleChords.flat:
	    if 'Chord' not in c.classes:
	        continue
	    c.closedPosition(forceOctave=4, inPlace=True)

	chordList = []
	#finding the roman numeral chord
	for c in sampleChords.flat.getElementsByClass('Chord'):
	    rn = roman.romanNumeralFromChord(c, sampleKey)
	    #normalize the key to C Major
	    rn.key = key.Key('C')
	    chordList.append(rn)
	    #chordGraph.addChord(rn)
	    #chordGraph.addChordPath(previous, str(rn.figure))

	#go through array and map out graph
	for x in xrange(0, len(chordList)-1):
		chordFrom = chordList[x]
		chordTo = chordList[x+1]

		#add chords to graph
		#duplicate checking is done inside ChordGraph
		chordGraph.addChord(chordFrom)
		chordGraph.addChord(chordTo)

		#update the path for chordFrom
		chordGraph.addChordPath(str(chordFrom.figure), str(chordTo.figure))

paths = corpus.getComposer('bach')
chordGraph = ChordGraph()

logfile = open("log.txt", "w");

""""""
for p in paths:	
	if re.match(r'(.*)bach/bwv(.*)mxl', p):
	#if 'bach/bwv' in p:
		print("Currently processing " + os.path.basename(p))
		logfile.write("Currently processing " + os.path.basename(p))
		parseChords(p, chordGraph)
		logfile.write("Finished processing " + os.path.basename(p))
		output = open('data/data.pkl', 'wb')
		pickle.dump(chordGraph, output)
		output.close()


#parseChords(paths[22], chordGraph)
#parseChords(paths[23], chordGraph)
#parseChords(paths[24], chordGraph)

for c in chordGraph.chordSet.values():
	print "The chord: " + c.chordStr
	#c.printLinks()
	#print ""

print "ALL PROCESSING FINISHED"

#serialize the chordGraph
output = open('data/data.pkl', 'wb')
pickle.dump(chordGraph, output)
output.close()