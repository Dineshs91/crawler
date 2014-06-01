#! /usr/bin/env python

import unittest
from crawler.crawlerDFS import Crawler

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.START_URL = 'http://www.facebook.com/'
        self.BRANCHING_FACTOR = 10
        self.c = Crawler(self.START_URL, self.BRANCHING_FACTOR)

    def test_checkUrl(self):
        ans = self.c.checkUrl(self.START_URL, [])
        #print ans
        self.assertTrue(len(ans) > 0)

    def test_startDFS(self):
        ans = self.c.startDFS()
        #print ans
        self.assertTrue(len(ans) > 0)
        #print 'No of links', len(ans)
        
    def test_startBFS(self):
        ans = self.c.startBFS()
        #print ans
        self.assertTrue(len(ans) > 0)
        #print 'No of links', len(ans)       
        
if __name__ == "__main__":
    unittest.main()
