requirements_satisfied = True
try:
	import BeautifulSoup 
except ImportError:
	requirements_satisfied = False


if requirements_satisfied == True:
	print "All dependancies are satisified"
else:
	print "Please install the required dependancies mentioned in requirements.txt"
	
