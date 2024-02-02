import os
import itertools

UG_HEADINGS = ["[Intro]", "[Verse]", "[Pre-chorus]", "[Chorus]", "[Interlude]", "[Bridge]", "[Solo]", "[Outro]"] 
ENGLISH_WORDS = []
CHORD_ROOTS = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'H', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'h'] + \
              ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#', 'H#', 'c#', 'd#', 'e#', 'f#', 'g#', 'a#', 'b#', 'h#'] + \
              ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb', 'Hb', 'cb', 'db', 'eb', 'fb', 'gb', 'ab', 'bb', 'hb'] + \
              ['Cis', 'Dis', 'Eis', 'Fis', 'Gis', 'Ais', 'Bis', 'His', 'cis', 'dis', 'eis', 'fis', 'gis', 'ais', 'bis', 'his'] + \
              ['Ces', 'Des', 'Ees', 'Fes', 'Ges', 'Aes', 'Bes', 'Hes', 'ces', 'des', 'ees', 'fes', 'ges', 'aes', 'bes', 'hes']
CHORD_SYMBOLS = []



def initChordSymbols():
  file = open("./chord-qualities.txt", 'r')
  chordQualities = file.read().splitlines()
  
  for root in CHORD_ROOTS:
    for quality in chordQualities:
      CHORD_SYMBOLS.append(root + quality)

def rowContainsAnyChords(words : [str]):
  for word in words:
    if word in CHORD_SYMBOLS:
      return True
  return False


def rowContainsAnyWords(words : [str], wordlist : [str]):
  for word in words:
    if word in ENGLISH_WORDS:
      return True
  return False

def rowContainsHeading(words : [str]):
  for word in words:
    if word in UG_HEADINGS:
      return True
  return False

def main (filename : str):
  initChordSymbols()
  file = open("./words.txt", 'r')
  ENGLISH_WORDS = file.read().splitlines()
  file.close()

  doesRowContainWords = []

  file = open(filename, 'r')
  rows = file.read().splitlines()
  file.close()

  resultFile = open("./result.txt", 'w')

  for row in rows:
    if len(row) == 0 or len(row) == 1 and row[0] == ' ': continue
    words = row.split(' ')
    if rowContainsAnyChords(words):
      resultFile.write(row + "\n")
      continue

    resultFile.write(row + "\n\n")
    """
    if rowContainsHeading(words):
      resultFile.write(row + "\n\n")
      continue
      
    if rowContainsAnyWords(words):
      resultFile.wirte(row + "\n")

    doesRowContainWords.append(rowContainsAWord)
    """



  
  return 0

main('./lockedoutofheaven.txt')