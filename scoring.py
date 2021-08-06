import language_tool_python as lt
from spellchecker import SpellChecker


def scoreTextForSpellingCorrectness(article):
    score = 0
    articleChecker = SpellChecker()
    wordsInArticle = article.split()
    totalWords = len(wordsInArticle)
    numIncorrectWords = len(articleChecker.unknown(wordsInArticle))
    correctlySpelledWords = articleChecker.known(wordsInArticle)
    for word in correctlySpelledWords:
        score += len(word) # Reward a text for having longer words
    score -= numIncorrectWords
    score /= totalWords
    return score

def scoreTextForGrammaticalCorrectness(article): # The higher the score, the better (although never greater than 0)
    tool = lt.LanguageTool('en-US')
    return -1 * len(tool.check(article))