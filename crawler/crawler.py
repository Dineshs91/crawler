#! /usr/bin/env python

import urllib2
import re
from BeautifulSoup import BeautifulSoup 
from util.calc import calc_time

class Crawler():
    """
    Crawler has methods checkUrl and start. start function is the actual entry 
    point. checkUrl finds the links and returns them.
    """
    def __init__(self, url, branchingFactor):
        self.url = url
        self.branchingFactor = branchingFactor

    def getUrl(self, currUrl, foundUrl):
        """
        Checks the urls in the link currUrl and returns those found urls.
        """
        urls = set([])
        try:
            response = urllib2.urlopen(currUrl)
        except:
            print 'Unable to connect to internet or Invalid link. Please check'
            return urls
        soup = BeautifulSoup(response.read())
        newLink = soup.findAll('a')
        for link in newLink:
            try:
                link = str(link.get('href'))
                m = re.match(r'http+', link)
                if not m:
                    link = currUrl + link
                if link not in foundUrl:
                    urls.add(str(link))
            except UnicodeEncodeError as e:
                print 'Error ---> ', e
        return urls
        
    @calc_time
    def startDFS(self):
        """
        Crawls to find the links in the given link and the depth is determined
        by the branching factor. DFS algorithm is used.
        """
        stack = []
        foundUrl = set([])
        stack.append(self.url)
        count = 0
        while count < self.branchingFactor and stack:
            currentUrl = stack.pop()
            print 'Checking page[%s]: %s' %(count + 1, currentUrl)
            foundUrls = self.getUrl(currentUrl, foundUrl)
            print '[%s] links found in %s' %(len(foundUrls), currentUrl)
            for i in foundUrls:
                stack.append(i)
                foundUrl.add(i)
            count += 1
        return foundUrl
        
    @calc_time
    def startBFS(self):
        """
        Uses BFS search technique.
        """
        queue = []
        foundUrl = set([])
        queue.append(self.url)
        count = 0
        while count < self.branchingFactor and queue:
            currentUrl = queue.pop(0)
            print 'Checking page[%s]: %s' %(count + 1, currentUrl)
            foundUrls = self.getUrl(currentUrl, foundUrl)
            print '[%s] links found in %s' %(len(foundUrls), currentUrl)
            for i in foundUrls:
                queue.append(i)
                foundUrl.add(i)
            count += 1
        return foundUrl
