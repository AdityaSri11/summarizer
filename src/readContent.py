from newspaper import Article

from summarize import generate_summary
from summarize import summarize
#from summarize import buildSummary

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

    summary = summarize(sentencesList, 0.4)

    return summary

