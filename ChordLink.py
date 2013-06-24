from ChordVertex import *

class ChordLink:

	def __init__(self, chordVertex):
		self.destination = chordVertex
		self.weight = 1

	def __str__(self):
		return "To: " + self.destination.chordStr + " of chord weight: " + str(self.weight)

	def addWeight(self):
		print "Adding weight!"
		self.weight = self.weight + 1
		print self.weight