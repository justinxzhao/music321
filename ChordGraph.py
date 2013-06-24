from music21 import *
from ChordVertex import *

class ChordGraph:

	def __init__(self):
		#chordSet<Key string, Value ChordVertex>
		self.chordSet = {} #set of ChordVertex

	def addChord(self, rnChord):
		chordStr = str(rnChord.figure)
		if not chordStr in self.chordSet.keys():
			node = ChordVertex(rnChord)
			self.chordSet[chordStr] = node

	def addChordPath(self, chordFrom, chordTo):
		nodeFrom = self.chordSet[chordFrom]
		nodeTo = self.chordSet[chordTo]
		nodeFrom.addLink(nodeTo)

	def printNodes(self):
		print self.chordSet.keys()