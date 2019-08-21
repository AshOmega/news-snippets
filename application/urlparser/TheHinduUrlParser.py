import requests
from application.urlparser.BaseUrlParser import BaseUrlParser

class TheHinduUrlParser(BaseUrlParser):
    """
        Class implementation to parse the data from Hindu newspaper.
    """
    def urlParser(self, url):
        response = requests.get(url)
        outString = response.text

        lastIndex = len(outString)
        result = 0
        startParaList = list()
        endParaList = list()
        fullContext = list()

        while 0 <= result <= lastIndex:
            result = outString.find("<p>", result + 1)
            startParaList.append(result)

        result = 0
        while 0 <= result <= lastIndex:
            result = outString.find("</p>", result + 1)
            endParaList.append(result)

        for index in range(1, len(startParaList)):
            start = startParaList[index]
            end = endParaList[index]
            formattedString = outString[start: end]
            if formattedString.startswith("<p>") and not formattedString.startswith("<p>\n"):
                lastMetaCharPos = formattedString.rfind(">")
                fullContext.append(formattedString[lastMetaCharPos + 1:])
        return fullContext


if __name__ == "__main__":
    hinduParserObj = TheHinduUrlParser()
    content = hinduParserObj.urlParser(
        'https://www.thehindu.com/opinion/op-ed/is-the-removal-of-special-status-for-jk-justified/article29103095.ece')
    for iter in content:
        print(iter)
