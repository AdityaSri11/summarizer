from newspaper import Article

from summarize import findSummary


def readLink(url):
    article = Article(url)
    article.download()
    article.parse()

    splitArticle = (article.text).split(" ")
    return article.text

def readInputs(result):

    if result[0:4] == "http":
        sentencesList = readLink(result)
    else:
        sentencesList = result

    #summary = buildSummary(sentencesList , 2)
    #summary = generate_summary(sentencesList, 2)

    summary = findSummary(sentencesList)

    return summary

fileV = open("/Users/adityasrikanth/Documents/Projects/summarizer/assets/textSamples/sample03.txt" , "r")
fileContents = fileV.read()
readInputs(fileContents)
