from application.urlparser.BaseUrlParser import BaseUrlParser
import requests


class FetchRelatedUrls(BaseUrlParser):
    """
    Class implementation to parse the fetch the list of related urls from a given search query page
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
            result = outString.find("<span class=\"story-card-heading\">", result + 1)
            if result != -1:
                startParaList.append(result)

        result = 0
        while 0 <= result <= lastIndex:
            result = outString.find("class=\"story-card75x1-text\">", result + 1)
            if result != -1:
                endParaList.append(result)

        for index in range(1, len(startParaList)):
            start = startParaList[index]
            end = endParaList[index]
            formattedString = outString[start: end]
            if formattedString.startswith(
                    "<span class=\"story-card-heading\"> <a class=\"kicker-text hidden-xs\"></a>\n<a href="):
                deltaStart = formattedString.find("</span> <a href=")
                deltaStart += len("</span> <a href=")
                netLength = start - end
                formattedString = formattedString[(netLength + deltaStart):]
                fullContext.append(formattedString)
        return fullContext


if __name__ == "__main__":
    relatedUrlsObj = FetchRelatedUrls()
    content = relatedUrlsObj.urlParser(
        'https://www.thehindu.com/search/?q=article%20370&order=DESC&sort=publishdate&page=3')
    for iter in content:
        print(iter)
