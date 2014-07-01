#! /usr/bin/env python

import urllib2
import re
from BeautifulSoup import BeautifulSoup 
from util.calc import calc_time

class Crawler():
    """
    Crawler class
    
    Crawler objects are responsible for crawling webpages.
    """
    def __init__(self, url, branching_factor):
        self.url = url
        self.branching_factor = branching_factor
        self.DFS = 'dfs'
        self.BFS = 'bfs'

    def get_url(self, current_url, urls_found):
        """
        Checks the urls in the link current_url and returns those found urls.
        """
        urls = set([])
        try:
            response = urllib2.urlopen(current_url)
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
                    link = current_url + link
                if link not in urls_found:
                    urls.add(str(link))
            except UnicodeEncodeError as e:
                print 'Error ---> ', e
        return urls
        
    @calc_time
    def start_dfs(self):
        """
        Crawls to find the links in the given link and the depth is determined
        by the branching factor. DFS algorithm is used.
        """
        return self.start(self.DFS)
        
    @calc_time
    def start_bfs(self):
        """
        BFS algorithm is used.
        """
        return self.start(self.BFS)
        
    def start(self, algorithm):
        structure = []
        urls_found = set([])
        structure.append(self.url)
        count = 0
        while count < self.branching_factor and structure:
            if algorithm == self.BFS:
                current_url = structure.pop(0)
            else:
                current_url = structure.pop()
            urls = self.get_url(current_url, urls_found)
            print '[%s] links found in %s' %(len(urls), current_url)
            for i in urls:
                structure.append(i)
                urls_found.add(i)
            count += 1
        return urls_found
        
    def __str__(self):
        return 'url:%s branching_factor:%s' %(self.url, self.branching_factor)
        
