import os
import string
import json

#todo: this will download the lyrics and populate the lyrics directory, some day 
def downloadLyrics():
    pass

def createArtistDocs():
    artists = {}
    for (dir_name, subdirs, _) in os.walk('lyrics'):
        for subdir in subdirs:
            print("working on artist:" + subdir)
            artistLyrics = ""
            for subdir_path, _, filenames in os.walk(os.path.join(dir_name, subdir)):
                for filename in filenames:
                    print("   reading: "+filename)
                    with open(os.path.join(subdir_path, filename), "r") as lyric_file:
                        #todo: this will lead to unnecessary copying, is there a python stringbuilder?
                        artistLyrics +=" "+lyric_file.read()
            artists[subdir] = artistLyrics
    return artists


def cleanWord(word):
    word = word.lower()
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for char in punctuation:
        word = word.replace(char, "")
    return word
# returns a dict - artist name to dict - term to count  
def computeArtistTf(artistDocs):
    artistTf = {}
    for artist in artistDocs:
        artistTf[artist]={}
        for word in artistDocs[artist].split():
            cleaned = cleanWord(word)
            if cleaned not in artistTf[artist]:
                artistTf[artist][cleaned]=0
            artistTf[artist][cleaned]+=1
    return artistTf
    
# takes output of artistTf, returns a dict - term to number of artists
def computeGlobalDocFrequency(artistTf):
    globalWords = {}
    for artist in artistTf:
        for word in artistTf[artist]:
            if word not in globalWords:
                globalWords[word]=0
            globalWords[word]+=1
    return globalWords
# takes output of artistTf, globalDocFrequency, returns dictionary to artist name to dict - term to tfidf (float)
def computeTfidf(artistFreq, globalFreq):
    artistTfidf = {}
    for artist in artistFreq:
        artistTfidf[artist]={}
        for word in artistFreq[artist]:
            artistTfidf[artist][word]=float(artistFreq[artist][word])/globalFreq[word]
    return artistTfidf
# produces map of artist name to ordered list of tuples (term, tfidf) given artistTfidf; this is mostly a presentation step
def orderTfidf(artistTfidf):
    pass
def computeArtistVocabSize(artistTfidf):
    artistVocabSize = {}
    for artist in artistTfidf:
        artistVocabSize[artist]=len(artistTfidf[artist])
    return artistVocabSize
def computeArtistUniqueWords(artistTfidf, globalWords):
    artistUniqueWords = {}
    for artist in artistTfidf:
        artistUniqueWords[artist]=[]
        for word in artistTfidf[artist]:
            if globalWords[word]==1:
                artistUniqueWords[artist].append(word)
artistDocs = createArtistDocs()
#print(artistDocs)
artistTf = computeArtistTf(artistDocs)
print(json.dumps(artistTf, indent=True))
globalDocFrequency = computeGlobalDocFrequency(artistTf)
print(json.dumps(globalDocFrequency, indent=True))
artistTfidf = computeTfidf(artistTf, globalDocFrequency)
print(json.dumps(artistTfidf, indent=True))
artistVocabSize = computeArtistVocabSize(artistTfidf)
print(json.dumps(artistVocabSize, indent=True))
artistUniqueWords = computeArtistUniqueWords(artistTfidf, globalDocFrequency)
print(json.dumps(artistUniqueWords, indent=True))
