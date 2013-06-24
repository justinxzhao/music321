from music21 import *
from random import randint

class MusicGenerator:

	def __init__(self):
		print "### MusicGenerator initialized"

	def genRandEqRhyth(self, numNotes, numParts, durRes, midiLow, midiHigh):
		"""Return a Stream of randomly generated notes with equal rhythms"""
		#to determine length of the smallest note
		#for example, 4 = 16th note resolution, 2 = eigth note resolution
		parts = []
		for i in xrange(numParts): #number of parts
			parts.append(stream.Part())

		for i in xrange(numNotes): #number of notes

			#determining note duration
			noteDur = randint(1, 4*durRes)
		
			# for every part, generate a note
			for j in xrange(numParts):
				n = note.Note(randint(midiLow, midiHigh))
				n.duration.quarterLength = noteDur*1.0 / durRes
				parts[j].append(n)
		
		#returns a Stream
		return stream.Stream(parts)

	def genRandIndRhyth(self, numNotes, numParts, durRes, midiLow, midiHigh):
		"""Return a Stream of randomly generated music with independently generated rhythms"""

		parts = []
		for i in xrange(numParts):
			parts.append(stream.Part())

		#generate notes for the first voice
		for i in xrange(numNotes):
			noteDur = randint(1, 4*durRes)
			
			n = note.Note(randint(midiLow, midiHigh))
			n.duration.quarterLength = noteDur*1.0 / durRes
			parts[0].append(n)

		totalLength = parts[0].duration.quarterLength

		#for the remaining parts
		for i in xrange(numParts-1):
			remainingLen = totalLength*durRes

			while (remainingLen != 0):

				noteDur = randint(1, 4*durRes)

				#change the note duration to what's left if it is too large
				if noteDur >= remainingLen:
					noteDur = remainingLen

				n = note.Note(randint(midiLow, midiHigh))
				n.duration.quarterLength = noteDur*1.0 / durRes

				#skip the first part
				parts[i+1].append(n)

				#update what remains
				remainingLen = remainingLen - noteDur

		return stream.Stream(parts)

	def genRandChordProg(self, numChords, chordLen):
		print "hello!"
	def genRandMelodyFromChord(self, chordList):
		s = stream.Stream
		return stream.Stream

	def genRandMelodyHarmonyFromChord(self, chordList):
		print "hello!"
	def randHarmonizeMelody(self, chordList):
		print "hello!"