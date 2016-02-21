import pickle
import os

counter = 0
isctr = 0
INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\BX-CSV-Dump\\BX-Books.csv"

books = open(INPUT_DIR, 'r')

novels = pickle.load( open( "E:\\MSProject\\nametofile2.p", "rb" ) )

isbns = dict()

for line in books:
	if line.startswith("ISBN"):
		continue
	counter += 1
	if counter % 100 == 0:
		print(counter)
	#if counter > 5000:
	#	break
	words = line.split(";")
	name = words[1][1:-1]
	if name.endswith("."):
		name = name[:-1]
	name = name.lower()
	if name in novels:
		isbns[words[0]] = name
		isctr += 1

print(isctr)
books.close()
pickle.dump( isbns, open( "E:\\MSProject\\isbntoname.p", "wb" ) )
print("Success")