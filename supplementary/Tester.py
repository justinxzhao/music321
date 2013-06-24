from music21 import *
from MusicGenerator import MusicGenerator
import os

### SETTING ENVIRONMENT VARIABLES
environment.set('musicxmlPath', '/usr/bin/mscore')
environment.set('midiPath', '/usr/bin/timidity')
environment.set('graphicsPath', '/usr/bin/eog')


mg = MusicGenerator()

### TEST FOR RANDOM EQUAL RHYTHM NOTE GENERATOR
"""
numNotes = 10
numParts = 4
durRes = 4
midiLow = 20
midiHigh = 80
s = mg.genRandEqRhyth(numNotes, numParts, durRes, midiLow, midiHigh)
s.show()
"""

### TEST FOR RANDOM INDEPENDENT RHYTHM NOTE GENERATOR
"""
numNotes = 10
numParts = 4
durRes = 4
midiLow = 20
midiHigh = 80
s = mg.genRandIndRhyth(numNotes, numParts, durRes, midiLow, midiHigh)
s.show()
"""

### TESTING CHORDIFY
"""
b = corpus.parse('bwv66.6')
bChords = b.chordify()

for c in bChords.flat:
    if 'Chord' not in c.classes:
        continue
    c.closedPosition(forceOctave=4, inPlace=True)

for c in bChords.flat.getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, key.Key('A'))
    c.addLyric(str(rn.figure))
    print c.lyric

#b.insert(0, bChords)
#b.show()
"""

#readFile = 'Recording.wav'
#frequencyList = audioSearch.getFrequenciesFromAudioFile(waveFilename = readFile)
#print frequencyList

b = converter.parse('totoroShort.xml')
bChords = b.chordify()
k = b.analyze('key')

for c in bChords.flat:
    if 'Chord' not in c.classes:
        continue
    c.closedPosition(forceOctave=4, inPlace=True)

for c in bChords.flat.getElementsByClass('Chord'):
    rn = roman.romanNumeralFromChord(c, k)
    c.addLyric(str(rn.figure))
    print c.lyric

b.insert(0, bChords)
b.show()

#b.plot('histogram', 'pitch')