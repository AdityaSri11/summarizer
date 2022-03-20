from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx
import numpy as np
import ast
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

'''
def similarities(firstSentence, secondSentence, stopwords = None):
    if stopwords is None:x
        stopwords = []

    firstSentence = [word.lower() for word in firstSentence]
    secondSentence = [word.lower() for word in secondSentence]

    dictionaryOfWords = set(firstSentence + secondSentence)
    dictionaryOfWords = list(dictionaryOfWords)

    l1 = [0] * len(dictionaryOfWords)
    l2 = [0] * len(dictionaryOfWords)

    for x in firstSentence:
        if x in stopwords:
            continue
        l1[dictionaryOfWords.index(x)] += 1
 
    for y in secondSentence:
        if y in stopwords:
            continue
        l2[dictionaryOfWords.index(y)] += 1

    similarityMetric = cosine_distance(l1,l2)

    return (1 - similarityMetric)

def buildMatrix(sentenceList, stopWords):

    similarityMatrix = np.zeros((len(sentenceList), len(sentenceList)))

    for i in range(0, len(sentenceList)):
        for j in range(0, len(sentenceList)):
            if i == j:
                continue
            else:
                similarityMatrix[i][j] = similarities(sentenceList[i], sentenceList[j], stopWords)

    return similarityMatrix

def buildSummary(sentenceList, n = 5):

    stopWords = stopwords.words('english')
    #print(stopWords)

    similarityMatrix = buildMatrix(sentenceList, stopWords)

    similarityGraph = nx.from_numpy_array(similarityMatrix)
    scores = nx.pagerank(similarityGraph)

    rankedValues = sorted(((scores[i],j) for i,j in enumerate(sentenceList)), reverse = True)    

    print(rankedValues)

    ini_list = (str(rankedValues[0]))[6:-1]
    res = ast.literal_eval(ini_list)
    
    return(' '.join(res))
'''

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
 
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

    return similarity_matrix


def generate_summary(sentences, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
  
    print(ranked_sentence)

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary