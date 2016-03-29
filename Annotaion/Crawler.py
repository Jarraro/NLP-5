import re, urllib
from stripogram import html2text
from nltk.stem.isri import ISRIStemmer


class Crawler:
    maxUrlVisited = 0
    PagesContent = ""

    def RetriveTextFormHtmlDocument(self,
                                    HTML):  # this function to return a pure text from HTML document, will be enhanced to remove header(css,JavaScript)
        HTML = html2text(HTML)
        return HTML

    def GoThroughURL(self, URL):
        print url

        Crawler.maxUrlVisited = Crawler.maxUrlVisited + 1
        if Crawler.maxUrlVisited > 4:
            return Crawler.PagesContent
        Request0 = urllib.urlopen(url).read()
        Request0_ = Crawler.RetriveTextFormHtmlDocument(self, Request0)

        Crawler.PagesContent = Crawler.PagesContent + url + '\n' + Request0_ + '\n'
        Crawler.PagesContent = Crawler.PagesContent + '------------------------------------------------' + '\n'
        for i in re.findall('''href=["'](.[^"']+)["']''', Request0, re.I):
            if i.find("http") == -1:
                i = url + i

            print i
            try:
                GoThroughURL(i)
            except:
                pass


Linkstextfile = file('Linkstextfile_20148006.txt', 'wt')
LinkContentstextfile = file('LinkContentstextfile_20148006.txt', 'wt')
StemmedLinkContentstextfile = file('StemmedLinkContentstextfile_20148006.txt', 'wt')

url = 'http://www.aljazeera.net/portal'  # my url

CrawlerInstance = Crawler()
PageContents = CrawlerInstance.GoThroughURL(url)

print PagesContent
LinkContentstextfile.write(PagesContent)
try:
    # part of stemming
    PagesContentasWords = PagesContent.split()
    st = ISRIStemmer()
    StemmingPagesContent = ''
    PagesContentasWordsStr = ''

    for i in PagesContentasWords:
        try:
            PagesContentasWordsStr = PagesContentasWordsStr + ' ' + i
            StemmingPagesContent = StemmingPagesContent + ' ' + st.stem(i.decode('utf-8'))
        except:
            pass

    print PagesContentasWordsStr
    print StemmingPagesContent

    StemmedLinkContentstextfile.write("/n/n-------------------------AFTER STEMMING-------------------------")
    StemmedLinkContentstextfile.write(StemmingPagesContent.encode('utf8'))
except:
    pass
