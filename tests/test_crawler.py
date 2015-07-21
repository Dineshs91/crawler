#! /usr/bin/env python

import unittest
from crawler.crawler import Crawler

class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.START_URL = 'http://www.facebook.com/'
        self.BRANCHING_FACTOR = 3
        self.c = Crawler(self.START_URL, self.BRANCHING_FACTOR)

    def test_get_url(self):
        ans = self.c.get_url(self.START_URL, [])
        self.assertTrue(len(ans) > 0)

    def test_start_dfs(self):
        ans = self.c.start_dfs()
        self.assertTrue(len(ans) > 0)
        
    def test_start_bfs(self):
        ans = self.c.start_bfs()
        self.assertTrue(len(ans) > 0)
        
if __name__ == "__main__":
    unittest.main()
