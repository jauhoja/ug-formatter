import re

UG_HEADINGS = ["[Intro]", "[Verse]", "[Verse 1]", "[Verse 2]", "[Verse 3]", "[Verse 4]", "[Verse 5]"] + \
              ["[Pre-chorus]", "[Chorus]", "[Interlude]", "[Bridge]", "[Break]", "[Solo]", "[Outro]"] 
CHORD_ROOTS = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'H', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'h'] + \
              ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'H#', 'c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'b#', 'h#'] + \
              ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Hb', 'cb', 'db', 'eb', 'fb', 'gb', 'ab', 'bb', 'hb'] + \
              ['Cis', 'Dis', 'Eis', 'Fis', 'Gis', 'Ais', 'Bis', 'His', 'cis', 'dis', 'eis', 'fis', 'gis', 'ais', 'bis', 'his'] + \
              ['Ces', 'Des', 'Ees', 'Fes', 'Ges', 'Aes', 'Bes', 'Hes', 'ces', 'des', 'ees', 'fes', 'ges', 'aes', 'bes', 'hes']
CHORD_SYMBOLS = []

def initChordSymbols():
  file = open("./chord-qualities.txt", 'r')
  chordQualities = file.read().splitlines()
  file.close()
  for root in CHORD_ROOTS:
    for quality in chordQualities:
      CHORD_SYMBOLS.append(root + quality)
  CHORD_SYMBOLS.append('N.C.') # No chord, any missing symbols can be added here

def rowContainsAnyChords(words : [str]):
  for word in words:
    if word in CHORD_SYMBOLS:
      return True
  return False

def rowContainsHeading(words : [str]):
  for word in words:
    if word in UG_HEADINGS:
      return True
    if '[' in word or ']' in word:
      return True
  return False

def main (filename : str):
  initChordSymbols()

  file = open(filename, 'r')
  rows = file.read().splitlines()
  file.close()

  resultFile = open("./output.txt", 'w')

  for row in rows:
    if len(row) == 0 or len(row) == 1 and row[0] == ' ': continue

    words = re.split("[ \t]", row)
    if rowContainsHeading(words):
      resultFile.write("\n" + '**' + row + '**' + "\n\n")
      continue
    if rowContainsAnyChords(words):
      resultFile.write(row + "\n")
      continue

    resultFile.write(row + "\n\n")

main('./input.txt')