from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl == parse.urljoin(self.baseUrl, value)
                    self.links += [newUrl]

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-type') == 'text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

    def spider(url, word, maxPages):
        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False
        while numberVisited < maxPages and pagesToVisit != [] or not foundWord:
            numberVisited += 1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numberVisited, "Visiting", url)
                parser = LinkParser()
                data, links = parser.getLinks(url)
                if data.find(word)>-1:
                    foundWord = True
                    foundAtUrl = url
                    pagesToVisit += links
                    print("Õnnestus!")
            except:
                print("Halvasti läks")
            if foundWord:
                print("Sõna", word, "leidsime aasdressilt", url)
            else:
                print("Sellist sõna ei leidnud")

LinkParser.spider("http://www.ee", "Postimees", 200)