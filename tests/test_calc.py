#! /usr/bin/env python

from crawler.util.calc import calc_time
from time import sleep
import unittest

class TestCalci(unittest.TestCase):
    def test_all(self):
        self.find()
        self.is_even(10)
        self.just_print('hi', b = 1, a="12")
        self.check_dict({1:1, 2:2})
        
    @calc_time
    def find(self):
        sleep(1)
        print 'success'
   
    @calc_time 
    def is_even(self, n):
        sleep(1)
        print n
    
    @calc_time
    def just_print(self, *args, **kwargs):
        sleep(1)
        #print 'args', av
        for i, j in kwargs.iteritems():
            print i, j
        
    @calc_time
    def check_dict(self, d):
        print d
        
if __name__ == "__main__":
    unittest.main()        
    
#find()  
#is_even(2001)  

# Syntax-error: non-keyword arg after keyword arg
#just_print('hi', b = 1, a="12" )
#check_dict({1:1, 2:2})
