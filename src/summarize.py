from venv import create
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

def freqMatrix(text) -> dict:
    stopWords = set(stopwords.words("english"))

    words = word_tokenize(text)
    portStemmer = PorterStemmer()

    frequencies = dict()

    for word in words:
        word = portStemmer.stem(word)

        if word in stopWords:
            continue
        elif word in frequencies: 
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies

def sentenceScores(sentences, frequencies):

    sentValue = dict()

    for s in sentences:
        wordCount = len(word_tokenize(s))

        for f in frequencies:
            if f in s.lower():
                if s[:10] in sentValue:
                    sentValue[s[:10]] += frequencies[f]
                else:
                    sentValue[s[:10]] = frequencies[f]
                
        sentValue[s[:10]] = sentValue[s[:10]] // wordCount

    return sentValue

def avgScore(scores):

    sumValues = 0

    for i in scores:
        sumValues += scores[i]

    average = int(sumValues / len(scores))

    return average

def createSummary(sentences, scores, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in scores and scores[sentence[:10]] > (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary

def findSummary(text):

    frequencies = freqMatrix(text)
    sentences = sent_tokenize(text)

    scores = sentenceScores(sentences, frequencies)
    threshold = avgScore(scores)
    summary = createSummary(sentences, scores, threshold)

    return summary