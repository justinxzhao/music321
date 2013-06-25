class ChordLink:

	def __init__(self, chordVertexStr):
		self.destination = chordVertexStr
		self.weight = 1

	def __str__(self):
		return "To: " + self.destination + " of chord weight: " + str(self.weight)

	def addWeight(self):
		self.weight = self.weight + 1