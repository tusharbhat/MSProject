import pickle
import os

counter = 0
isctr = 0
rectr = 0
INPUT_DIR = "C:\\Users\\Tushar-PC\\Downloads\\BX-CSV-Dump\\BX-Book-Ratings.csv"

reviews = open(INPUT_DIR, 'r')

isbns = pickle.load( open( "E:\\MSProject\\isbntoname.p", "rb" ) )

users = dict()

good_rev = open("E:\\MSProject\\goodrev.csv", "w")

good_rev.write(reviews.readline())

for line in reviews:
	if line.startswith("User"):
		continue
	counter += 1
	if counter % 1000 == 0:
		print(counter)
	words = line.split(";")
	if words[1] in isbns:
		good_rev.write(line)
		isctr += 1
		if int(words[2].strip()[1:-1]) > 0:
			rectr += 1
		if words[0] in users:
			users[words[0]] += 1
		else:
			users[words[0]] = 1

reviews.close()
print("Success")
print(isctr)
print(rectr)
print(max([users[word] for word in users]))
print(min([users[word] for word in users]))
print(sum([users[word] for word in users])/len(users))
print(len(users))
goodctr = 0
for word in users:
	if users[word] > 9 and users[word] < 300:
		goodctr += 1
print(goodctr)
good_rev.close()
pickle.dump( users, open( "E:\\MSProject\\users.p", "wb" ) )