import enchant
import os


UG_HEADINGS = ["[Intro]", "[Verse]", "[Pre-chorus]", "[Chorus]", "[Interlude]", "[Bridge]", "[Solo]", "[Outro]"] 

def wordExistsInLanguage(word : str, wordlist : [str]):
  return 0

def main (filename : str):
  file = open("./words.txt", 'r')
  englishWords = file.read().splitlines()
  file.close()

  doesRowContainWords = []

  file = open(filename, 'r')
  rows = file.read().splitlines()
  file.close()

  for row in rows:
    rowContainsAWord = False
    words = row.split(' ')
    for word in words:
      if word in englishWords:
        rowContainsAWord = True
        break
    doesRowContainWords.append(rowContainsAWord)
  

  """ for debugging
  file = open("./result.txt", 'w')
  for i in range(len(rows)):
    file.write("[" + str(doesRowContainWords[i]) + "] " + rows[i] + "\n")
  """
  
  return 0

main('./lockedoutofheaven.txt')