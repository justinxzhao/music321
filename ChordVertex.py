from ChordLink import *
from music21 import *

class ChordVertex:

	def __init__(self, rnChord):
		self.chordStr = str(rnChord.figure)
		self.rnChord = rnChord
		#chordLinks<Key String, Value ChordLink>
		self.chordLinks = {}

	def __str__(self):
		return self.chordStr

	def addLink(self, chordTo):
		if not chordTo.chordStr in self.chordLinks.keys():
			#create a new link for this vertex
			cl = ChordLink(chordTo)
			self.chordLinks[chordTo.chordStr] = cl
		else:
			#find the link that exists and addweight
			cl = self.chordLinks[chordTo.chordStr]
			cl.addWeight()

	def printLinks(self):
		for cl in self.chordLinks.values():
			print cl
