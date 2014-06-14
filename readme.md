Crawler:

Web Crawler browses the Website address specified and creates an index of all directories and subdirectories present.
Usage Specify the Web Address.

The crawler provides with two options for searching the Subdirectories.

1.Depth First Search (DFS) 
2.Breadth First Search (BFS) algorithm is used for exploring. 

You also have to specify the branching factor.Branching Factor specifies the depth you want to crawl ,i.e if there are a number of subdirectories at what level should the crawler stop indexing.

You can use the check_dependencies.py to see whether all dependancies are satisfied.
Install the dependancies in requirements.txt manually or use the following: pip install -r requirements.txt

Usage: 

Testing:

From the parent directory execute the following command.

$ python -m unittest discover -v tests

This command will run all the tests that are present inside tests directory.

Hacking:

Open interactive python from the main directory.
$ python

>>> from crawler.crawler import Crawler

Create your crawler
>>> my_crawl = Crawler('http://www.test.com', 10)
The first argument is the link and the second is the branching factor.

Run your crawler
>>>my_crawl.startDFS()

The output is a set containing all the url's found while crawling.

Disclaimer:
This project is for development purposes only. We are not responsible for any damage caused by
using this project.