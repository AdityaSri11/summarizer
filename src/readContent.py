from newspaper import Article


def readLink(url):
    article = Article(url)
    article.download()
    article.parse()

    splitArticle = (article.text).split(" ")
    return [splitArticle]

def readInputs(result):

    if result[0:4] == "http":
        sentencesList = readLink(result)
    else:
        splitValues = result.split(" ")
        sentencesList = [splitValues]

    