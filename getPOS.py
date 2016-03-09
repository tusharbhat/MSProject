import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from heapq import heappop, heappush
from collections import Counter

pos = [pickle.load( open( "E:\\MSProject\\isbntoposdict.p", "rb" ) ), pickle.load( open( "E:\\MSProject\\isbntoposdict2.p", "rb" ) )]
isbns = pickle.load( open( "E:\\MSProject\\isbntoname.p", "rb" ) )
bookno = pickle.load( open( "E:\\MSProject\\bookarr.p", "rb" ) )

goodrev = open( "E:\\MSProject\\goodrev.csv", "r" )

pos_set = set()

pos_best = dict()

for p in pos:
	for key in p:
		for value in p[key]:
			if value not in pos_best:
				pos_best[value] = 0
			pos_best[value] += p[key][value]

#print([ k for k, v in Counter(pos_best).most_common(8)])
tag_list = [ k for k, v in Counter(pos_best).most_common(8)]
#tag_list.append('.')
#tag_list.append(',')
#exit(0)

for p in pos:
	for key in p:
		for value in p[key]:
			pos_set.add(value)

tag_set = {'VBN', 'RP', 'SYM', 'EX', 'VBZ', 'FW', 'WRB', 'WP', 'NN', 'JJS', 'PDT', 'CC', 'RBR', 'UH', 'JJ', 'RBS', 'NNPS', 'JJR', 'IN', '.', 'CD', 'DT', 'RB', 'LS', 'PRP', 'PRP$', 'MD', 'VBD', 'NNS', 'NNP', 'WDT', 'POS', 'VBP', 'VB', ',', 'WP$', 'TO', 'VBG'}
#tag_list = ['VBN', 'RP', 'SYM', 'EX', 'VBZ', 'FW', 'WRB', 'WP', 'NN', 'JJS', 'PDT', 'CC', 'RBR', 'UH', 'JJ', 'RBS', 'NNPS', 'JJR', 'IN', '.', 'CD', 'DT', 'RB', 'LS', 'PRP', 'PRP$', 'MD', 'VBD', 'NNS', 'NNP', 'WDT', 'POS', 'VBP', 'VB', ',', 'WP$', 'TO', 'VBG']
#tag_list = ['NN', 'IN', 'DT', 'PRP', ',', 'JJ', 'VBD', '.', 'RB', 'NNP', 'CC', 'NNS']

fullstop = tag_list.index('.')
comma = tag_list.index(',')

pos_feat = np.ndarray((len(isbns), len(tag_list)+2), dtype = int)

for i in range(len(bookno)):
	isbn = bookno[i]
	for j in range(len(tag_list)):
		if tag_list[j] in pos[0][isbn]:
			pos_feat[i, j] = pos[0][isbn][tag_list[j]]
		if tag_list[j] in pos[1][isbn]:
			pos_feat[i, j] += pos[1][isbn][tag_list[j]]
		pos_feat[i, -1] = pos_feat[i, fullstop] + pos_feat[i, comma]
		pos_feat[i, -2] = sum(pos_feat[i, :-2]) - pos_feat[i, -1]

#print(pos_feat[:5])

sim = cosine_similarity(pos_feat, pos_feat)
#sim = euclidean_distances(pos_feat, pos_feat)
#for i in sim:
#	for j in i:
#		j = 1 - j

nn = list()
for i in range(len(bookno)):
	scoreh = []
	for j in range(len(bookno)):
		if i == j:
			continue
		heappush(scoreh, (sim[i, j], j))
		if len(scoreh) > 10:
			heappop(scoreh)
	nn.append(scoreh)

print("Success")

users = dict()

for line in goodrev:
	if line.startswith("User"):
		continue
	words = line.split(";")
	if words[0] not in users:
		users[words[0]] = set()
	users[words[0]].add(words[1])

total = 0
correct = 0

for user in users:
	revs = users[user].copy()
	if len(revs) > 1:
		total += 1
		cand = revs.pop()
		book_cand = dict()
		for train in revs:
			nbs = nn[bookno.index(train)]
			for nb in nbs:
				if nb[1] in book_cand:
					book_cand[nb[1]] += nb[0]
				else:
					book_cand[nb[1]] = nb[0]
		for k, v in Counter(book_cand).most_common(10):
			if bookno[k] == cand:
				correct += 1

print(correct/total)
print(correct)
print(total)
print("Complete")
