import nltk
from nltk import word_tokenize
import textblob
import pickle
from datetime import datetime

#nltk.download('taggers')
isbns = pickle.load( open( "E:\\MSProject\\isbntoname.p", "rb" ) )
novels = pickle.load( open( "E:\\MSProject\\nametofile2.p", "rb" ) )
INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\ProjectGutenberg\\allnovels\\"

alltags = dict()
failctr = 0
textctr = 0
for key in isbns:
	#print(datetime.now().time())
	#print("Hello")
	textctr += 1
	if textctr % 10 == 0:
		print(textctr)
	#if textctr >= 5:
	#	break
	name = isbns[key]
	filename = novels[name][0]
	thisfile = open(INPUT_DIR + filename, 'r')
	linectr = 0
	tagctr = dict()
	#for line in thisfile:
	while linectr < 400:
		line = "\n"
		try:
			line = thisfile.readline()
		except(Exception):
			failctr += 1
		if line is "":
			break
		if line is not "\n":
			linectr += 1
		if linectr < 350:
			continue
		#if linectr >= 350:
		#	break
		text = word_tokenize(line)
		tags = nltk.pos_tag(text)
		for tag in tags:
			if tag[1] in tagctr:
				tagctr[tag[1]] += 1
			else:
				tagctr[tag[1]] = 1
	alltags[key] = tagctr
pickle.dump( alltags, open( "E:\\MSProject\\isbntoposdict2.p", "wb" ) )
print("Success")
print(failctr)
#print(alltags)
